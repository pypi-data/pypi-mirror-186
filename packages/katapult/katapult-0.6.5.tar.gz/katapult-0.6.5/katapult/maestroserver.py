from cloudsend import provider as cs
from cloudsend.provider import COMMAND_ARGS_SEP , ARGS_SEP , STREAM_RESULT , debug , stream_load , stream_dump
import asyncio , os , sys , time
from cloudsend.core import CloudSendProcessState , bcolors , CloudSendRunSession , CloudSendRunSessionProxy
import traceback
import json
import socket
import asyncio

HOST = 'localhost' #'0.0.0.0' #127.0.0.1' 
PORT = 5000

async def mainloop(ctxt):

    await ctxt.init()

    server = await asyncio.start_server(ctxt.handle_client, HOST, PORT, reuse_address=True, reuse_port=True)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    try:
        async with server:
            await server.serve_forever()   
    except asyncio.CancelledError:
        ctxt.restore_stdio()
        print("Shutting down ...")


class ByteStreamWriter():

    def __init__(self,writer):
        self.writer = writer 
    
    def write(self,data):
        if isinstance(data,(bytes,bytearray)):
            self.writer.write(data)
        elif isinstance(data,str):
            self.writer.write(data.encode('utf-8'))
        else:
            self.writer.write(str(data,'utf-8').encode('utf-8'))

    async def drain(self):
        await self.writer.drain()

    def close(self):
        self.writer.close()

    def flush(self):
        asyncio.ensure_future( self.writer.drain() )

class ServerContext:
    def __init__(self,args):
        self.cs_client  = None
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        self.auto_init = any( arg == 'auto_init' for arg in args )

    async def init(self):
        if self.auto_init: # set to True by the crontab in case maestro crashed
            self.cs_client = cs.get_client(None)
            # we've just restarted a crashed maestro server process
            # let's test for WATCH state and reach it back again if thats needed
            await self.wakeup()

    async def wakeup(self):
        await self.cs_client.wakeup()

    async def handle_client(self, reader, writer):
        while True:
            try:
                cmd_line = await reader.readline()
                if not cmd_line:
                    break
                cmd_line = cmd_line.decode('utf-8').strip()
                #print(cmd_line)

                # OLD SERIALIZATION METHOD (cf. provider.py too)
                # cmd_args = cmd_line.split(COMMAND_ARGS_SEP)
                # if len(cmd_args)>=2:
                #     cmd  = cmd_args[0].strip()
                #     args = cmd_args[1].split(ARGS_SEP)
                # else:
                #     cmd  = cmd_line
                #     args = None

                cmd_json = json.loads(cmd_line)
                # DO NOT UNCOMMENT ! THIS CAUSES A LOCKS
                #print("JSON COMMAND",cmd_json)
                cmd  = cmd_json['cmd']
                args = cmd_json['args'] 

                await self.process_command(cmd,args,writer)
                break # one-shot command
            except ConnectionResetError as cre:
                try:
                    sys.stdout = self.old_stdout
                    print(cre)
                    print("DISCONNECTION")
                except:
                    pass
                break    
            except Exception as e:
                try:
                    sys.stdout = self.old_stdout
                    sys.stderr = self.old_stderr
                    print(e)
                    print(traceback.format_exc())
                    traceback.print_exc()
                except:
                    pass
                break  
        try:
            await writer.drain()
        except:
            pass
        try:
            writer.close()
        except:
            pass

    def get_run_session(self,label,session_arg,allow_proxied=False):
        if session_arg is None:
            return None
        run_session = stream_load(self.cs_client,session_arg)
        if run_session is None:
            err_level = bcolors.FAIL if not allow_proxied else bcolors.WARNING
            debug(1,label,"This session object has expired and can not be found in the server anymore",session_arg,color=err_level)
            if allow_proxied:
                debug(1,label,"Using CloudSendRunSessionProxy as argument",color=bcolors.WARNING)
                try:
                    session_number = int(session_arg['number'])
                    session_id     = session_arg['id'].strip()
                    run_session    = CloudSendRunSessionProxy(session_number,session_id)
                    return run_session
                except:
                    debug(1,label,"Could not create proxied session",session_arg,color=bcolors.FAIL)
                    return None
            else:
                return None
        return run_session

    def get_instance(self,label,instance_arg):
        instance = stream_load(self.cs_client,instance_arg)
        if instance is None:
            debug(1,label,"This instance object has expired and can not be found in the server anymore",arg,color=bcolors.FAIL)
            return None
        return instance

    def send_result(self,result):
        print(STREAM_RESULT+json.dumps(stream_dump(result)))

    async def process_command(self,command,args,writer):
        #sock = writer.transport.get_extra_info('socket')
        
        string_writer = ByteStreamWriter(writer)
        sys.stdout = string_writer
        sys.stderr = string_writer

        if self.cs_client is None:
            if command != 'init' and command != 'shutdown':
                print(bcolors.WARNING+"Server not ready. Run 'init CONFIG_FILE' or 'start' command first"+bcolors.ENDC)
                await writer.drain()
                return 
        try:

            if command == 'init':

                if not args:
                    config_ = None
                elif len(args)==1:
                    config_ = args[0].strip() 
                else:
                    config_ = None
                self.cs_client  = cs.get_client(config_)

                await self.wakeup() 

                init_objects = self.cs_client.get_objects()
                self.send_result(init_objects)               

            elif command == 'wakeup':

                await self.cs_client.wakeup()

            elif command == 'start':

                if not args:
                    reset = False
                elif len(args)==1:
                    reset = args[0]
                else:
                    reset = False

                await self.cs_client.start(reset)

            elif command == 'cfg_add_instances':
                config = None
                kwargs = dict()
                if args and len(args)>=1:
                    config = args[0]
                elif args and len(args)>=2:
                    config = args[0]
                    kwargs = stream_load(self.cs_client,args[1])
                else:
                    print("Error: you need to send a JSON stream for config")
                    await writer.drain()
                    return
                added_objects = await self.cs_client.cfg_add_instances(config,**kwargs)
                self.send_result(added_objects)

            elif command == 'cfg_add_en((vironments':
                config = None
                kwargs = dict()
                if args and len(args)>=1:
                    config = args[0]
                elif args and len(args)>=2:
                    config = args[0]
                    kwargs = stream_load(self.cs_client,args[1])
                else:
                    print("Error: you need to send a JSON stream for config")
                    await writer.drain()
                    return
                added_objects = await self.cs_client.cfg_add_environments(config,**kwargs)
                self.send_result(added_objects)

            elif command == 'cfg_add_jobs':
                config = None
                kwargs = dict()
                if args and len(args)>=1:
                    config = args[0]
                elif args and len(args)>=2:
                    config = args[0]
                    kwargs = stream_load(self.cs_client,args[1])
                else:
                    print("Error: you need to send a JSON stream for config")
                    await writer.drain()
                    return
                added_objects = await self.cs_client.cfg_add_jobs(config,**kwargs)
                self.send_result(added_objects)

            elif command == 'cfg_add_config':
                config = None
                kwargs = dict()
                if args and len(args)>=1:
                    config = args[0]
                elif args and len(args)>=2:
                    config = args[0]
                    kwargs = stream_load(self.cs_client,args[1])
                else:
                    print("Error: you need to send a JSON stream for config")
                    await writer.drain()
                    return
                added_objects = await self.cs_client.cfg_add_config(config,**kwargs)
                self.send_result(added_objects)

            elif command == 'cfg_reset':

                await self.cs_client.cfg_reset()

            elif command == 'deploy':

                await self.cs_client.deploy()

            elif command == 'run':

                if args and len(args)==1:
                    continue_session = args[0]
                    run_session = await self.cs_client.run(continue_session)
                else:
                    run_session = await self.cs_client.run()

                self.send_result(run_session)
            
            elif command == 'kill':

                if args and len(args)==1:
                    identifier = args[0].strip()
                    await self.cs_client.kill(identifier)
            
            elif command == 'wait':

                job_state   = CloudSendProcessState.DONE|CloudSendProcessState.ABORTED
                run_session = None
                if args and len(args) >= 1:
                    job_state = int(args[0])
                if args and len(args) >= 2:
                    run_session = self.get_run_session("WAIT:",args[1])

                await self.cs_client.wait(job_state,run_session)

            elif command == 'get_num_active_processes':

                run_session = None
                if args and len(args) >= 1:
                    run_session = self.get_run_session("GET_NUM_ACTIVE_PROCESSES:",args[0])

                result = await self.cs_client.get_num_active_processes(run_session)                
                self.send_result(result)

            elif command == 'get_num_instances':

                result = await self.cs_client.get_num_instances()                
                self.send_result(result)

            elif command == 'get_states' or command == 'get_jobs_states':

                run_session = None
                if args and len(args) == 1:
                    run_session = self.get_run_session("GET STATES:",args[0])
                    last_running_processes = False
                elif args and len(args) == 2:
                    run_session = self.get_run_session("GET STATES:",args[0]) 
                    last_running_processes = args[1]

                result = await self.cs_client.get_jobs_states(run_session,last_running_processes)
                self.send_result(result)

            elif command == 'print_summary' or command == 'print':

                run_session = None
                instance    = None
                if args and len(args) >= 1:
                    run_session = self.get_run_session("PRINT_SUMMARY:",args[0])
                if args and len(args) >= 2:
                    instance = self.get_instance("PRINT_SUMMARY:",args[1])

                debug(2,run_session,instance)

                await self.cs_client.print_jobs_summary(run_session,instance)

            elif command == 'print_aborted' or command == 'print_aborted_logs':

                run_session = None
                instance    = None
                if args and len(args) >= 1:
                    run_session = self.get_run_session("PRINT_SUMMARY:",args[0])
                if args and len(args) >= 2:
                    instance = self.get_instance("PRINT_SUMMARY:",args[1])

                debug(2,run_session,instance)

                await self.cs_client.print_aborted_logs(run_session,instance)

            elif command == 'print_objects':

                await self.cs_client.print_objects()

            elif command == 'clear_results_dir':

                if args and len(args)>0:
                    directory = args[0].strip()
                    await self.cs_client.clear_results_dir(directory)
                else:
                    await self.cs_client.clear_results_dir()

            elif command == 'fetch_results':

                directory   = None
                run_session = None
                use_cached  = True
                use_normal_output = False

                if args and len(args)>=1:
                    directory = args[0].strip()
                    if directory.lower() == 'none':
                        directory = None
                if args and len(args)>=2:
                    run_session = self.get_run_session("FETCH_RESULTS",args[1],True) # allow shallow object return
                if args and len(args)>=3:
                    use_cached = args[2]
                if args and len(args)>=4:
                    use_normal_output = args[3]

                out_dir = await self.cs_client.fetch_results(directory,run_session,use_cached,use_normal_output)
                
                self.send_result(out_dir)

            elif command == 'finalize':
                
                await self.cs_client.finalize()

            elif command == 'shutdown':

                asyncio.get_event_loop().stop()

            elif command == 'test':

                print("TEST")
            
            else:

                print("UNKNOWN COMMAND")
        
        except Exception as e:
            print(e)
            traceback.print_exc()
            await writer.drain()
            #writer.close()
            self.restore_stdio()
            print(e)
            traceback.print_exc()
            raise e

        await writer.drain()
        # to let time for the buffer to be flushed before killing thread and connection
        #time.sleep(1)
        #writer.close()  

    def restore_stdio(self):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

# run main loop
def main():

    ctxt = ServerContext(sys.argv)

    try:
        asyncio.run( mainloop(ctxt) )
    except RuntimeError as re:
        print(re)

if __name__ == '__main__':
    main()    