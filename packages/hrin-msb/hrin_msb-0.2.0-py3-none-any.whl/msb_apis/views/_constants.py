CRUD_URL_PK = '/<str:pk>'
CRUD_URL_PK_NAME = "pk"
MAX_FETCH_LIMIT = 100
DEFAULT_LOGGER_NAME = 'root'

class REQUEST_METHODS:
	POST = "post"
	PUT = "put"
	GET = "get"
	DELETE = "delete"

	ALL = [POST, PUT, GET, DELETE]


class CrudActions:
	create = 'create'
	retrieve = 'retrieve'
	list = 'list'

	update = 'update'
	bulk_update = 'bulk_update'

	delete = 'delete'
	bulk_delete = 'bulk_delete'
	all = [create, retrieve, update, delete, bulk_delete, bulk_update, list]


CRUD_MAPPINGS = {
	CrudActions.retrieve: {REQUEST_METHODS.GET: CrudActions.retrieve},
	CrudActions.update: {REQUEST_METHODS.PUT: CrudActions.update},
	CrudActions.delete: {REQUEST_METHODS.DELETE: CrudActions.delete},
	CrudActions.create: {REQUEST_METHODS.POST: CrudActions.create},

}

BULK_MAPPINGS = {
	CrudActions.bulk_delete: {REQUEST_METHODS.DELETE: CrudActions.bulk_delete},
	CrudActions.bulk_update: {REQUEST_METHODS.PUT: CrudActions.bulk_update},
	CrudActions.list: {REQUEST_METHODS.GET: CrudActions.list},
	CrudActions.create: {REQUEST_METHODS.POST: CrudActions.create},

}
