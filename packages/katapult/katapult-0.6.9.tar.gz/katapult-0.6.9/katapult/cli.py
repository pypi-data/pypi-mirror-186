import katapult
import asyncio
import sys 
import psutil
import subprocess
import multiprocessing 
import time
import copy
import argparse
import os
import re
from katapult.maestroserver import main as server_main
from katapult.maestroclient import maestro_client
from katapult.provider import make_client_command , stream_dump , guess_environment , get_client

# if [[ $(ps aux | grep "katapult.maestroserver" | grep -v 'grep') ]] ; then
#     echo "Katapult server already running"
# else
#     if [[ $(ps -ef | awk '/[m]aestroserver/{print $2}') ]] ; then
#         ps -ef | awk '/[m]aestroserver/{print $2}' | xargs kill 
#     fi
#     echo "Starting Katapult server ..."
#     python3 -u -m katapult.maestroserver
# fi

def katapult_kill(p):
    try:
        p.kill()
    except:
        pass
    try:
        p.terminate()
    except:
        pass

def is_katapult_process(p,name='maestroserver'):
    try:
        if name in p.name():
            return True
        for arg in p.cmdline():
            if name in arg:
                return True
        return False
    except psutil.AccessDenied:
        return False
    except psutil.NoSuchProcess:
        return False

def cli(command):
    start_server() # locally we use python to start the server. maximizes the chance to be Windows complatible
    maestro_client(command)

# basically this: https://dev.to/cindyledev/remote-development-with-visual-studio-code-on-aws-ec2-4cla
# in one CLI ...
async def cli_one_shot():
    argParser = argparse.ArgumentParser(prog = 'katapult.cli',
                    description = 'runs one shot commands',
                    epilog = '--Thanks!')  
    argParser.add_argument('command') 
    argParser.add_argument("-p", "--profile", help="your aws profile name")
    argParser.add_argument("-t", "--type", help="the aws instance type")
    argParser.add_argument("-r", "--region", help="the aws region")
    args = argParser.parse_args()

    instance_type = args.type or 't3.micro'

    env_obj , the_files = guess_environment('vscode','.')
    
    config = {
        'project'      : 'vscode' ,
        'profile'      : args.profile , 
        'debug'        : 1 ,
        'maestro'      : 'local' , # one shot is local
        'auto_stop'    : False ,
        'recover'      : True ,
        'instances'    : [
            {
                'type'         : instance_type ,
                'number'       : 1 ,
                'region'       : args.region
            }
        ] ,
        'environments' : [ env_obj ] ,
        'job' : [
            {
                'run_command' : 'ls' , # foo command ,
                'upload_files' : the_files , # we're using this feature to upload files
                'input_files' : 'foo_in.dat' , # foo
                'output_files' : 'foo_out.dat' # foo
            }
        ]
    }

    kt = get_client(config)
    await kt.start()
    await kt.deploy()

    objs = await kt.get_objects()
    instance = objs['instances'][0]

    key_file_name = kt.get_key_filename(config.get('profile'),instance.get_config('region'))
    key_file_path = os.path.join(os.getcwd(),key_file_name)

    nu_fragment = """Host {0}
    Hostname {1}
    User {2}
    Port {3}
    IdentityFile {4}""".format("katapult.vscode",instance.get_ip_addr(),"ubuntu",22,key_file_path)

    # edit the ssh config
    home_dir = os.path.expanduser('~')
    ssh_config_path = os.path.join(home_dir,'.ssh','config')
    with open(ssh_config_path,'r') as ssh_config:
        ssh_config_content = ssh_config.read()
    
    if 'katapult.vscode' in ssh_config_content:
        with open(ssh_config_path,'w') as ssh_config:
            new_content = re.sub(r"""Host katapult.vscode
    Hostname [^\n]+
    User [^\n]+
    Port [^\n]+
    IdentityFile [^\n]+""",nu_fragment,ssh_config_content)
            ssh_config.write(new_content)
    else:
        with open(ssh_config_path,'a') as ssh_config:
            ssh_config.write('\n')
            ssh_config.write(nu_fragment)

    # https://stackoverflow.com/questions/54402104/how-to-connect-ec2-instance-with-vscode-directly-using-pem-file-in-sftp/60305052#60305052
    # https://stackoverflow.com/questions/60144074/how-to-open-a-remote-folder-from-command-line-in-vs-code
    #
    # on OSX:
    # /Applications/Visual\ Studio\ Code.app/Contents/MacOS/Electron --folder-uri=vscode-remote://ubuntu@13.38.11.243/home/ubuntu/
    os.system( "/Applications/Visual\ Studio\ Code.app/Contents/MacOS/Electron --folder-uri=vscode-remote://katapult.vscode/home/ubuntu/")

def start_server():
    server_started = False
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            if is_katapult_process(p,"katapult.maestroserver"):
                print("[Katapult server already started]")
                server_started = True
                break
        except psutil.NoSuchProcess:
            pass
    if not server_started:
        # make sure we kill any rogue processes
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)
                for pp in p.children(recursive=True):
                    if is_katapult_process(pp):
                        katapult_kill(pp)
                if is_katapult_process(p):
                    katapult_kill(p)
            except psutil.NoSuchProcess:
                pass
        print("[Starting Katapult server ...]")
        subprocess.Popen(['python3','-u','-m','katapult.maestroserver'])
        time.sleep(1)
        #q = multiprocessing.Queue()
        #p = multiprocessing.Process(target=server_main,args=(q,))
        #p = multiprocessing.Process(target=server_main)
        #p.daemon = True
        #p.start()

def cli_translate(command,args):
    if command == 'init':
        return args

    elif command == 'wakeup':
        return args

    elif command == 'start':
        if not args:
            return [False]
        elif len(args)==1:
            return [args[0].strip().lower() == "true"]
        else:
            return [False]

    elif command == 'cfg_add_instances':
        return args

    elif command == 'cfg_add_environments':
        return args

    elif command == 'cfg_add_jobs':
        return args

    elif command == 'cfg_add_config':
        return args

    elif command == 'cfg_reset':
        return args

    elif command == 'deploy':
        return args

    elif command == 'run':
        return args

    elif command == 'kill':
        return args
    
    elif command == 'wait':
        new_args = []
        if args and len(args) >= 1:
            job_state = int(args[0])
            new_args.append(job_state)
        if args and len(args) >= 2:
            run_session = KatapultRunSessionProxy( args[1] )
            new_args.append( stream_dump(run_session) )
        return new_args 

    elif command == 'get_num_active_processes':

        new_args = []
        if args and len(args) >= 1:
            run_session = KatapultRunSessionProxy( args[0] )
            new_args.append( stream_dump(run_session) )
        return new_args 

    elif command == 'get_num_instances':
        return args

    elif command == 'get_states' or command == 'get_jobs_states':
        new_args = []
        if args and len(args) >= 1:
            run_session = KatapultRunSessionProxy( args[0] )
            new_args.append( stream_dump(run_session) )
        return new_args 

    elif command == 'print_summary' or command == 'print':
        new_args = []
        if args and len(args) >= 1:
            run_session = KatapultRunSessionProxy( args[0] )
            new_args.append( stream_dump(run_session) )
        if args and len(args) >= 2:
            instance = KatapultInstanceProxy( args[1] )
            new_args.append( stream_dump(instance) )
        return new_args 

    elif command == 'print_aborted' or command == 'print_aborted_logs':
        new_args = []
        if args and len(args) >= 1:
            run_session = KatapultRunSessionProxy( args[0] )
            new_args.append( stream_dump(run_session) )
        if args and len(args) >= 2:
            instance = KatapultInstanceProxy( args[1] )
            new_args.append( stream_dump(instance) )
        return new_args 
        
    elif command == 'print_objects':
        return args

    elif command == 'clear_results_dir':
        return args

    # out_dir=None,run_session=None,use_cached=True,use_normal_output=False
    elif command == 'fetch_results':

        new_args = []
        if args and len(args)>=1:
            directory = args[0].strip()
            if directory.lower() == 'none':
                directory = None
            new_args.append(directory)
        if args and len(args)>=2:
            run_session = KatapultRunSessionProxy( args[1] )
            new_args.append( stream_dump(run_session) )
        if args and len(args)>=3:
            use_cached = args[2].lower().strip() == "true"
            new_args.append( use_cached )
        if args and len(args)>=4:
            use_normal_output = args[3].lower().strip() == "true"
            new_args.append( use_normal_output )
        return new_args

    elif command == 'finalize':
        return args

    elif command == 'shutdown':
        return args

    elif command == 'test':
        return args
    
    else:
        return None

def main():
    multiprocessing.set_start_method('spawn')

    if len(sys.argv)<2:
        print("python3 -m katapult.cli CMD [ARGS]")
        sys.exit()

    args = copy.deepcopy(sys.argv)
    cmd_arg = args.pop(0) #trash
    while 'cli' not in cmd_arg:
        cmd_arg = args.pop(0)
    command = args.pop(0)

    one_shot_command = command in [ 'vscode' , 'run_dir' ]

    if one_shot_command:
        asyncio.run( cli_one_shot() )
    else:
        ser_args = cli_translate(command,args)
        # lets not escape the command, we're not sending it to a stream
        the_command = make_client_command( command , ser_args , False)
        cli(the_command)


if __name__ == '__main__':     
    main()