from msb_cipher import Cipher
from msb_dataclasses import Singleton
from msb_dataclasses.search_parameter import SearchParameter
from msb_db.models import MsbModel
from msb_exceptions import CustomExceptionHandler
from ._exceptions import ApiServiceExceptions


class ApiService(CustomExceptionHandler, metaclass=Singleton):
	db_model = MsbModel

	@property
	def cipher(self):
		return Cipher

	def __decrypt(self, data):
		return Cipher.decrypt(data=data)

	def __init__(self):
		if self.db_model is None:
			raise ApiServiceExceptions.InvalidDatabaseModel

	def search(self, params: SearchParameter):
		try:
			model_query = params.get_query(self.db_model)
			return model_query.all()[params.offset:params.offset + params.limit]
		except Exception:
			return False

	def create(self, *model_data_list):
		try:
			create_status = False
			if len(model_data_list) <= 0:
				raise ApiServiceExceptions.InvalidDataForCreateOperation

			if len(model_data_list) == 1:
				_model_data = model_data_list[0]
				_model = self.db_model(**_model_data)
				_model.save()
				create_status = True
			else:
				create_status = self.db_model.objects.bulk_create(
					[self.db_model(**model_data) for model_data in model_data_list]
				)
				create_status = True
		except Exception:
			raise ApiServiceExceptions.CreateOperationFailed
		return create_status

	def retrieve(self, pk=None):
		try:
			if pk is None:
				raise ApiServiceExceptions.InvalidPk
			return self.db_model.objects.get(pk=pk)
		except Exception:
			raise ApiServiceExceptions.RetrieveOperationFailed

	def list(self, fields: list = None, filters: dict = None):
		try:
			model_objects = self.db_model.objects
			if isinstance(fields, list) and len(fields) > 0:
				model_objects.only(*fields)

			if isinstance(filters, dict) and len(filters.keys()) > 0:
				model_objects.filter(**filters)
			offset, limit = (0, 50)
			data_list = model_objects.all()[offset:limit]
			return data_list
		except Exception:
			raise ApiServiceExceptions.ListOperationFailed

	def update(self, pk=None, **model_data):
		try:
			if (pk := self.__decrypt(pk)) is None:
				raise ApiServiceExceptions.InvalidPk
			model_object = self.db_model.objects.filter(pk=pk)
			if model_object and not (status := model_object.update(**model_data)):
				raise ApiServiceExceptions.UpdateOperationFailed
			return bool(status)
		except Exception:
			raise ApiServiceExceptions.UpdateOperationFailed

	def delete(self, pk=None):
		try:
			if (pk := self.__decrypt(pk)) is None:
				raise ApiServiceExceptions.InvalidPk
			model_object = self.db_model.objects.get(pk=pk)

			if model_object and not (status := model_object.delete()):
				raise ApiServiceExceptions.DeleteOperationFailed
			return status
		except Exception:
			raise ApiServiceExceptions.DeleteOperationFailed
