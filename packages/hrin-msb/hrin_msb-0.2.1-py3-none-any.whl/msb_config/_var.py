import os


# Env variable class
class EnvVar(object):
	_key = None

	_value = None

	def __init__(self, key: str = '', value: str = ''):
		self._key = key
		self._value = value

	def __str__(self):
		return f"{self._key} : {self._value}"

	def as_str(self, default: str = '') -> str:
		return default if self._value is None else self._value

	def as_int(self, default: int = 0) -> int:
		return default if self._value is None else int(self._value)

	def as_float(self, default: float = 0.0) -> float:
		return default if self._value is None else float(self._value)

	def as_bool(self, default: bool = False) -> bool:
		if self._value is not None:
			return (int(self._value) > 0) if self._value.isnumeric() \
				else self._value.lower() in ['yes', 'true', '1']
		else:
			return default

	def as_list(self, sep='|', default: list = None) -> list:
		default = default if default is not None else []
		return default if self._value is None else self._value.split(sep=sep)

	def as_tuple(self, sep='|', default: tuple = None) -> tuple:
		default = default if default is not None else tuple()
		return tuple(self.as_list(sep=sep, default=list(default)))

	def as_dict(self, sep='|', kv_sep: str = '=', default: dict = None) -> dict:
		default = default if default is not None else dict()
		lst = self.as_list(sep=sep)
		if len(lst) > 0:
			return {
				str(item).strip().split(kv_sep)[0]:
					str(item).strip().split(kv_sep)[1]
				for item in lst}

	def as_path(self, default='', joinpath: str = None):
		if joinpath is not None:
			return os.path.join(joinpath, self.as_str(default=default))
		return self.as_str(default=default)
