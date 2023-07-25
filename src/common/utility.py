import subprocess

def print_colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m",
    }

    if color not in colors:
        raise ValueError("Invalid color. Available colors are: red, green, yellow, blue, magenta, cyan")

    colored_text = colors[color] + text + colors["reset"]
    print(colored_text)

def eWHc_cmd(cmd):
    # cmd_result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    cmd_result_stderr = ""
    while True:
        # output stdout
        cmd_result = process.stdout.readline()
        if cmd_result == b'' and process.poll() is not None:
            break
        if cmd_result:
            print_colored(cmd_result.decode('utf-8').strip(), "magenta")

    while True:
        # output stderr
        stderr = process.stderr.readline()
        if not stderr and not process.poll() is None:
            break
        if stderr:
            cmd_result_stderr += stderr.decode('utf-8')

    if len(cmd_result_stderr) == 0:
        return
    else:
        return cmd_result_stderr

class Dict2Obj(object):
    """字典转对象"""

    def __init__(self, map_):
        self.map_ = map_

    def __getattr__(self, name):
        val = self.map_.get(name)
        if isinstance(val, dict):
            return Dict2Obj(val)
        elif isinstance(val, list):
            return [Dict2Obj(item) for item in val]
        else:
            return self.map_.get(name)

    def __str__(self) -> str:
        return str(self.map_)

    @property
    def dict_data(self):
        return self.map_