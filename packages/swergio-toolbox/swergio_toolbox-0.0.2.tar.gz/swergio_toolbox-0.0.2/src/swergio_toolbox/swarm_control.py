import subprocess
import yaml
import time

class Component():
    """
    A class representing a component that can be started and stopped.

    :param filepath: The file path of the component.
    :type filepath: str

    :param envpath: Path to environment used to execute python or julia code. 
    :type envpath: str

    :param delay: The delay in seconds before starting the component.
    :type delay: int or float

    :param terminal_cmd: Command used to start the component in a terminal. When None no terminal is used. 
    :type terminal_cmd: str
    
    :param python_cmd: Command to run python file. Default "python".
    :type python_cmd: str

    :ivar filepath: The file path of the component.
    :vartype filepath: str

    :ivar envpath: Path to environment used to execute python or julia code. 
    :vartype envpath: str

    :ivar delay: The delay in seconds before starting the component.
    :vartype delay: int or float

    :ivar process: The subprocess object representing the running component.
    :vartype process: subprocess.Popen

    :ivar terminal_cmd: Command used to start the component in a terminal. When None no terminal is used. 
    :vartype terminal_cmd: str
    
    :ivar python_cmd: Command to run python file. Default "python".
    :vartype python_cmd: str
    """
    def __init__(self, filepath, envpath = None, delay = None, terminal_cmd = None, python_cmd = "python" ):
        self.filepath = filepath
        self.envpath = envpath
        self.delay = delay
        self.process = None 
        self.terminal_cmd = terminal_cmd
        self.python_cmd = python_cmd
        
    def start(self):
        """
        Start the component.
        
        :return: The delay in seconds before starting the component, or None if the file extension is not recognized.
        :rtype: int or float or None
        """
        if self.filepath.split('.')[-1] == "py":
            lang = self.python_cmd
        elif self.filepath.split('.')[-1] == "jl":
            lang = "julia"
        else:
            return None
        
        if self.envpath is not None:
            if lang == "julia":
                if self.envpath == ".":
                    cmd = [lang,"--project","-i",self.filepath]
                else:
                    cmd = [lang,"--project",self.envpath,"-i",self.filepath]
            elif lang == "python":
                cmd = [self.envpath + lang,"-i",self.filepath]
        else:
            cmd = [lang,"-i",self.filepath]
        
        if self.terminal_cmd  is not None:
            command = self.terminal_cmd.split(" ") + cmd
        else:
            command = cmd
        self.process = subprocess.Popen(command)
        
        return self.delay    

    def stop(self):
        """
        Stop the component.
        """
        if self.process is not None:
            self.process.terminate()

        
class Swarm():
    """
    A class representing a swarm of components that can be started and stopped as a group.

    :param config_file: The file path of the configuration file.
    :type config_file: str

    :ivar config: The configuration for the swarm.
    :vartype config: dict

    :ivar components: The components in the swarm.
    :vartype components: dict
    """
    def __init__(self, config_file = None) -> None:
        """
        Initialize the Swarm.
        
        :param config_file: The file path of the configuration file.
        :type config_file: str
        """
        if config_file is None:
            config_file = 'swarm.yaml'
        with open(config_file, 'r') as stream:
            self.config = yaml.safe_load(stream)
        
        self.julia_envpath = self.config['settings']['julia_envpath'] if 'julia_envpath' in self.config['settings'].keys() else None
        self.python_envpath = self.config['settings']['python_envpath'] if 'python_envpath' in self.config['settings'].keys() else None
        self.python_cmd = self.config['settings']['python_cmd'] if 'python_cmd' in self.config['settings'].keys() else "python"
        self.terminal_cmd = self.config['settings']['terminal_cmd'] if 'terminal_cmd' in self.config['settings'].keys() else None
        
        self.components = {}
        for k,v in self.config['components'].items():
            
            if 'envpath' in v.keys():
                envpath = envpath
            else:
                if v['filepath'].split('.')[-1] == "py" and self.python_envpath is not None:
                    envpath = self.python_envpath
                elif v['filepath'].split('.')[-1] == "jl" and self.julia_envpath is not None:
                    envpath = self.julia_envpath
                else:
                    envpath = None
    
            self.components[k] = Component(
                v['filepath'],
                envpath= envpath,
                delay= v['delay'] if 'delay' in v.keys() else None,
                terminal_cmd= v['terminal_cmd'] if 'terminal_cmd' in v.keys() else self.terminal_cmd,
                python_cmd = v['python_cmd'] if 'python_cmd' in v.keys() else self.python_cmd,
            )
                
    def start(self, components = None):
        """
        Start the specified components in the swarm.

        :param components: The names of the components to start. If not provided, all components will be started.
        :type components: list of str or str or None

        :return: None
        """
        if components is None:
            components = list(self.components.keys())
        if isinstance(components,str):
            components = [components]
        for c in components:
            delay = self.components[c].start()
            if delay is not None:
                print("DELAY")
                time.sleep(delay)

            
    def stop(self, components = None):
        """
        Stop the specified components in the swarm.

        :param components: The names of the components to stop. If not provided, all components will be stopped.
        :type components: list of str or str or None

        :return: None
        """
        if components is None:
            components = list(self.components.keys())
        if isinstance(components,str):
            components = [components]
        for c in components:
            delay = self.components[c].stop()

    
    def add(self,name, filepath,envpath = None ,delay = None, terminal_cmd = None, python_cmd = "python"):
        """
        Add a new component to the swarm.

        :param name: The name of the new component.
        :type name: str

        :param filepath: The file path of the new component.
        :type filepath: str

        :param envpath: Path to environment used to execute python or julia code. 
        :type envpath: str

        :param delay: The delay in seconds before starting the new component.
        :type delay: int or float

        :param terminal_cmd: Command used to start the component in a terminal. When None no terminal is used. If terminal_cmd is "", the terminal_cmd of the swarm will be used.
        :type terminal_cmd: str
        
        :param python_cmd: Command to run python file. Default "python". If python_cmd is "", the python_cmd of the swarm will be used.
        :type python_cmd: str

        :return: None
        """
        if envpath is not None:
            envpath = envpath
        else:
            if filepath.split('.')[-1] == "py" and self.python_envpath is not None:
                envpath = self.python_envpath
            elif filepath.split('.')[-1] == "jl" and self.julia_envpath is not None:
                envpath = self.julia_envpath
            else:
                envpath = None
                
        self.components[name] = Component(
                filepath,
                envpath= envpath,
                delay= delay,
                terminal_cmd= terminal_cmd if terminal_cmd != "" else self.terminal_cmd,
                python_cmd = python_cmd if python_cmd != "" else self.python_cmd
            )

    
    