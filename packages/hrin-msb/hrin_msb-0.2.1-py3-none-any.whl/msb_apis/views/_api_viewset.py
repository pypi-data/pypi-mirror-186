from msb_validation import DefaultRules, validate_against, InvalidPayloadException
from ._api_view import ApiView
from ._constants import (CRUD_MAPPINGS, BULK_MAPPINGS, CrudActions, CRUD_URL_PK_NAME)
from ._exceptions import CrudApiExceptions
from ..services import ApiService
from ..wrappers import (RestResponse)


class ApiViewset(ApiView):
	service_class: ApiService = None
	validation_schema_class = None
	pk_name: str = CRUD_URL_PK_NAME

	def __validate_crud_request(self, action: str, inp=None, unknown=True, bulk=False, rule=None):
		if self.validation_schema_class is None:
			raise CrudApiExceptions.SchemaValidationClassNotDefined
		rule = self.validation_schema_class.get(action, default={}) if rule is None else rule
		if (validation_errors := validate_against(schema=rule, inp=inp, unknown=unknown, bulk=bulk)) is not None:
			raise InvalidPayloadException(errors=validation_errors)

	@classmethod
	def crud_routes(cls, actions: list = None, **kwargs):
		try:
			from django.urls import path, include

			pk_name = cls.pk_name or CRUD_URL_PK_NAME
			allowed_actions = actions if isinstance(actions, list) else []
			single_operation_mappings, bulk_operation_mappings = (dict(), dict())

			for single_mapping, bulk_mapping in zip(CRUD_MAPPINGS.keys(), BULK_MAPPINGS.keys()):
				if single_mapping in allowed_actions and single_mapping not in [CrudActions.create]:
					single_operation_mappings.update(CRUD_MAPPINGS.get(single_mapping))

				if bulk_mapping in allowed_actions:
					bulk_operation_mappings.update(BULK_MAPPINGS.get(bulk_mapping))

			return [
				path("", cls.as_view(actions=bulk_operation_mappings)),
				path(f"/<str:{pk_name}>", cls.as_view(actions=single_operation_mappings))
			]

		except Exception as e:
			return None

	def create(self, *args, **kwargs) -> RestResponse:
		try:
			is_bulk = not isinstance(self.payload, dict)
			self.__validate_crud_request(CrudActions.create, inp=self.payload, unknown=False, bulk=is_bulk)
			_create_payload = [self.payload] if not is_bulk else self.payload

			if not (result := self.service_class.create(*_create_payload)):
				raise CrudApiExceptions.CreateOperationFailed
			return self.api_response.success()

		except Exception as e:
			return self.api_response.exception(e)

	def retrieve(self, *args, **kwargs) -> RestResponse:
		try:
			self.__validate_crud_request(CrudActions.retrieve, inp=kwargs)
			_pk = kwargs.get(self.pk_name)
			result = self.service_class.retrieve(pk=_pk)
			return self.api_response.success(data=self.serializer(data=[result]))
		except Exception as e:
			return self.api_response.exception(e=e)

	def list(self, *args, **kwargs) -> RestResponse:
		try:

			result = self.service_class.list()
			return self.api_response.success(data=self.serializer(data=result))
		except Exception as e:
			return self.api_response.exception(e=e)

	def update(self, *args, **kwargs) -> RestResponse:
		try:
			_rule = DefaultRules.pk_validation_rule(self.pk_name)
			_pk = kwargs.get(self.pk_name)
			_update_data = self.payload
			self.__validate_crud_request(CrudActions.update, inp=kwargs, rule=_rule)
			self.__validate_crud_request(CrudActions.update, inp=_update_data)
			result = self.service_class.update(pk=_pk, **_update_data)
			if not (result):
				raise CrudApiExceptions.UpdateOperationFailed
			return self.api_response.success()
		except Exception as e:
			return self.api_response.exception(e=e)

	def bulk_update(self, *args, **kwargs) -> RestResponse:
		try:
			_payload_list = [self.payload] if isinstance(self.payload, dict) else self.payload
			self.__validate_crud_request(CrudActions.update, inp=_payload_list, bulk=True)
			for _payload in _payload_list:
				if (_pk := _payload.get(self.pk_name)) is not None:
					del _payload[self.pk_name]
					self.service_class.update(pk=_pk, **_payload)
			return self.api_response.success()
		except Exception as e:
			return self.api_response.exception(e=e)

	def delete(self, *args, **kwargs) -> RestResponse:
		try:
			_rule = DefaultRules.pk_validation_rule(self.pk_name)
			_pk = kwargs.get(self.pk_name)
			self.__validate_crud_request(CrudActions.delete, inp=kwargs, rule=_rule)
			if not (result := self.service_class.delete(pk=_pk)):
				raise CrudApiExceptions.DeleteOperationFailed
			return self.api_response.success()
		except Exception as e:
			return self.api_response.exception(e=e)

	def bulk_delete(self, *args, **kwargs) -> RestResponse:
		try:
			_rule = DefaultRules.pk_validation_rule(self.pk_name)
			_payload = [self.payload] if isinstance(self.payload, dict) else self.payload
			self.__validate_crud_request(CrudActions.delete, inp=_payload, rule=_rule, bulk=True)
			for pk_details in _payload:
				_pk = pk_details.get(self.pk_name)
				self.service_class.delete(pk=_pk)
			return self.api_response.success()
		except Exception as e:
			return self.api_response.exception(e=e)
