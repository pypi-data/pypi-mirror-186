from ..wrappers import (ApiResponse, RestResponse)


def api_details(request=None, ver='', name=''):
	return ApiResponse.success(
		data=dict(method=request.method, version=ver, name=name)
	)
