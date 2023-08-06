from __future__ import annotations

from rest_framework import status
from rest_framework.response import Response as RestResponse
from msb_exceptions import AppException
from msb_exceptions import CustomExceptionHandler


class ContentTypes:
	JSON = 'application/json'


class ApiResponse:
	data_types = [list, dict]

	@staticmethod
	def _dispatch(data: dict = None, status=status.HTTP_200_OK) -> RestResponse:
		headers = dict()
		_response = RestResponse(data=data, headers=headers, status=status)
		return _response

	@staticmethod
	def success(data=None, msg: str = 'ok') -> RestResponse:
		response_data = dict(
			success=True, message=msg,
			code=200, data=([] if type(data) not in ApiResponse.data_types else data)
		)
		return ApiResponse._dispatch(data=response_data)

	@staticmethod
	def error(msg: str = "Failure", err_code=600, data=None) -> RestResponse:
		response_data = dict(
			success=False,
			message=msg,
			code=err_code,
			data=([] if type(data) not in ApiResponse.data_types else data)
		)
		return ApiResponse._dispatch(data=response_data)

	@staticmethod
	def exception(e: AppException | Exception = None) -> RestResponse:
		CustomExceptionHandler.handle_exception(e=e)
		return ApiResponse.error(
			msg=e.message if hasattr(e, 'message') else str(e),
			data=e.errors if hasattr(e, 'errors') else [],
			err_code=e.code if hasattr(e, 'code') else 500
		)

	@staticmethod
	def not_found(msg: str = "Resource Not Found.", **kwargs):
		response_data = dict(success=False, message=msg, code=404, data=[])
		return ApiResponse._dispatch(data=response_data, status=status.HTTP_404_NOT_FOUND)

	@staticmethod
	def forbidden(msg: str = "Forbidden.", **kwargs):
		response_data = dict(success=False, message=msg, code=403, data=[])
		return ApiResponse._dispatch(data=response_data, status=status.HTTP_403_FORBIDDEN)

	@staticmethod
	def bad_request(msg: str = "Bad Request.", **kwargs):
		response_data = dict(success=False, message=msg, code=400, data=[])
		return ApiResponse._dispatch(data=response_data, status=status.HTTP_400_BAD_REQUEST)

	@staticmethod
	def method_not_allowed(msg: str = "Method Not Allowed.", **kwargs):
		response_data = dict(success=False, message=msg, code=405, data=[])
		return ApiResponse._dispatch(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	@staticmethod
	def internal_server_error(msg: str = "Internal Server Error", **kwargs):
		response_data = dict(success=False, message=msg, code=500, data=[])
		return ApiResponse._dispatch(
			data=response_data,
			status=status.HTTP_500_INTERNAL_SERVER_ERROR
		)