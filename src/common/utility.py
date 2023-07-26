import os
import re
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


def exec_cmd(cmd):
	cmd_result = subprocess.run(cmd, shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	return cmd_result.stdout.decode("utf8")

def create_dir(dir_name):
	if os.path.exists(dir_name):
		pass
	else:
		os.makedirs(dir_name)


def check_file(filename):
	if os.path.exists(filename):
		with open(filename, "r", encoding="utf8") as f:
			return re.sub('\n{2,}', '\n', f.read()).split("\n")
	else:
		return False


def find_list_difference(args1: list, args2: list):
	difference = set(args1).symmetric_difference(set(args2))
	if '' in difference:
		difference.remove('')
	return list(difference)


def write_content_to_file(content, filepath):
	with open(filepath, "a", encoding="utf8") as f:
		f.write(content + "\n")


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
