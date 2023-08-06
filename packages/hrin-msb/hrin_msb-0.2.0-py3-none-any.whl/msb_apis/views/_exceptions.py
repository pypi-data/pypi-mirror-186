from msb_exceptions import ApiException


class CrudApiExceptions:

	class SchemaValidationClassNotDefined(ApiException):
		_message = "Api class inherited from 'ApiViewset' must have a 'validation_schema_class' property defined." \
		           "The value of which should be the class which holds your validation rules."

	class CreateOperationFailed(ApiException):
		_message = "Failed to create the requested data."

	class DeleteOperationFailed(ApiException):
		_message = "Failed to delete the requested data."


	class UpdateOperationFailed(ApiException):
		_message = "Failed to update the requested data."


	class RetrieveOperationFailed(ApiException):
		_message = "Failed to retrieve the requested data."