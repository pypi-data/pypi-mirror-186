from msb_exceptions import AppException


class ApiServiceExceptions:
	class InvalidDatabaseModel(AppException):
		_message = "Invalid database model in services."

	class InvalidPk(AppException):
		_message = "Primary Identifier Field cant be empty."

	class InvalidDataForCreateOperation(AppException):
		_message = "Invalid data for creation."

	class CreateOperationFailed(AppException):
		_message = "Create operation request failed."

	class RetrieveOperationFailed(AppException):
		_message = "Failed to retrieve the requested data."

	class ListOperationFailed(AppException):
		_message = "Failed to retrieve the requested list."

	class UpdateOperationFailed(AppException):
		_message = "Update operation failed."

	class BulkUpdateOperationFailed(AppException):
		_message = "Bulk update operation failed."

	class DeleteOperationFailed(AppException):
		_message = "Delete operation failed."

	class BulkDeleteOperationFailed(AppException):
		_message = "Bulk delete operation failed."
