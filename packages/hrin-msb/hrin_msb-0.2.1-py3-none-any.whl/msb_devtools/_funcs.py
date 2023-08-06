import os
import sys


def add_paths_to_system(*path_list):
	for path in path_list:
		sys.path.append(path)


def log_to_console(msg, format=False):
	_log_message = f"\n{f'[ {msg} ] ' :*^100}" if format else f"LOG : {msg}"
	return print(_log_message)
