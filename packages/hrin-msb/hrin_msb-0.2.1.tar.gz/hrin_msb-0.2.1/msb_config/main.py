import os

from ._constants import (ENVIRONMENT_VARIABLE_NAME, ENV_LOAD_STATUS_KEY, DEBUG_VARIABLE_NAME, DEBUG_VARIABLE_VALUE)
from ._var import EnvVar


class Config:

	@staticmethod
	def load(env_path: str = '', main_file: str = '', local_file: str = ''):
		from ._core import load_config
		load_config(env_path, main_file, local_file)

	@staticmethod
	def is_loaded() -> bool:
		return os.environ.get(ENV_LOAD_STATUS_KEY) is not None

	@staticmethod
	def get(key: str = '', default=None) -> EnvVar:
		return EnvVar(key=key, value=os.environ.get(key, default=default))

	@staticmethod
	def debug():
		return Config.get(DEBUG_VARIABLE_NAME).as_bool(default=DEBUG_VARIABLE_VALUE)

	@staticmethod
	def env_name() -> str:
		return Config.get(ENVIRONMENT_VARIABLE_NAME).as_str(default=None)

	@staticmethod
	def is_local_env():
		return Config.env_name() == 'local'
