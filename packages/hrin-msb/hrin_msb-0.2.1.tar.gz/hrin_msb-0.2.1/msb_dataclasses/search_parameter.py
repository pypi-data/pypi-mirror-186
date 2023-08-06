from dataclasses import dataclass, field
from msb_cipher import Cipher

DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 50


@dataclass
class SearchParameter:
	_model_filters: dict
	_fields: list = None
	_order_by: str = None
	_limit: int = None
	_offset: int = None
	_order_field: str = None
	_filters = dict()
	_model_filter_map = dict()
	_auto_decrypt_filters = list()

	def get_query(self, for_model=None):
		self._init_model_filters(model=for_model)
		data_set = for_model.objects.only(*self.fields).filter(**self.filters)
		if self.order_field:
			data_set = data_set.order_by(self.order_field)
		return data_set

	def _init_model_filters(self, model=None):
		for key, value in self._filters.items():
			if key in self._model_filter_map.keys():
				self.add_filters(self._model_filter_map[key], value)
			elif hasattr(model, key):
				self.add_filters(key, value)

	def __init_model_filters(self, filters: dict):
		for key, value in filters.items():
			if key in self._model_filter_map.keys():
				self.add_filters(self._model_filter_map[key], filters[key])

	def __parse_value(self, key, value):
		if key in self._auto_decrypt_filters:
			if isinstance(value, list):
				value = Cipher.decrypt_list_items(*value)
		return value

	def __init__(self, **kwargs):
		self._model_filters = dict()
		self._fields = kwargs.get('fields') or []
		self._order_by = kwargs.get('order_by') or 'ASC'
		self._limit = kwargs.get('limit') or DEFAULT_LIMIT
		self._offset = kwargs.get('offset') or DEFAULT_OFFSET
		self.order_field = kwargs.get('order_field')
		self._filters = kwargs.get('filters') or dict()

	def add_filters(self, key: str, value):
		if isinstance(key, str) and value is not None:
			self._model_filters[key] = self.__parse_value(key, value)

	@property
	def filters(self) -> dict:
		return self._model_filters

	@property
	def fields(self) -> list:
		return self._fields

	@property
	def order_by(self) -> str:
		return self._order_by

	@property
	def limit(self) -> int:
		try:
			return int(self._limit) if int(self._limit) > 0 else DEFAULT_LIMIT
		except Exception:
			return 0

	@property
	def offset(self) -> int:
		try:
			return int(self._offset) if int(self._offset) >= 0 else DEFAULT_OFFSET
		except Exception:
			return 0

	@property
	def order_field(self) -> str:
		return self._order_field

	@order_field.setter
	def order_field(self, value):
		if value is not None:
			if self.order_by != 'ASC':
				self._order_field = f"-{value}"
			else:
				self._order_field = value
