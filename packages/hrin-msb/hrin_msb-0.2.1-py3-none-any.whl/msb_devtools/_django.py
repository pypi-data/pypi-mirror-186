import logging
import os

from django.core.management import call_command
from django.db import connections

from ._constants import DJANGO_MIGRATION_DB_VENDOR_CONFIG
from ._dto import DbVendorConfig
from ._funcs import log_to_console


def init_django_app(settings_dir: str, sys_pathlist:list, **kwargs):
	import django, sys
	sys.path.extend(sys_pathlist)
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{settings_dir}.settings")
	os.environ.setdefault("PYTHONUNBUFFERED", "1")

	django.setup()


class DjangoBase():
	def _execute_cmd(self, *args):
		log_to_console(msg=f"executing {' '.join(args if len(args) > 0 else 'all')} ", format=True)
		call_command(*args)


class DjangoMigration(DjangoBase):
	migration_dir: str
	__vendor_config: dict
	__database_set: set = set()
	__remove_tables_from_database_set: set = set()
	__apps_set: set = set()
	__is_dev_env: bool = False
	__remove_migration_files: bool = False
	__migrations_only: bool = False

	def __db_query(self, db_connection, *queries):
		if db_connection and len(queries) > 0:
			with db_connection.cursor() as cursor:
				_result = []
				for query in queries:
					print(f"Executing Query = {query}\n")
					query_result = cursor.execute(query)
					if query.lstrip(' ').lower().startswith(('select', 'show')):
						_result.append(cursor.fetchall())
					else:
						_result.append(query_result)
				return _result[0] if len(_result) == 1 else _result

	def __init__(self, migration_dir, **kwargs):
		try:

			self.migration_dir = migration_dir
			self.__vendor_config = DJANGO_MIGRATION_DB_VENDOR_CONFIG
			self.__is_dev_env = kwargs.get('is_dev_env') == True
			self.__remove_migration_files = kwargs.get('remove_files') == True
			if not os.path.isdir(self.migration_dir):
				os.mkdir(self.migration_dir, 0o777)
		except Exception as e:
			logging.warning(e)

	def __get_db_vendor_config(self, db_connection) -> DbVendorConfig:
		if db_connection and hasattr(db_connection, 'vendor'):
			return self.__vendor_config.get(getattr(db_connection, 'vendor'))
		return None

	def __remove_files(self):
		if self.__is_dev_env or self.__remove_migration_files:
			log_to_console(msg="Removing Migration Files.", format=True)
			for miration_file in os.listdir(self.migration_dir):
				if miration_file not in ['__init__.py', '__pycache__']:
					os.remove(os.path.join(self.migration_dir, miration_file))
					log_to_console(miration_file)

	def __remove_tables(self):
		if self.__is_dev_env:
			for db in list(self.__remove_tables_from_database_set):
				con = connections[db]
				db_config = self.__get_db_vendor_config(db_connection=con)
				if db_config:
					log_to_console(f"Removing Database Tables From {db}", format=True)
					table_list = self.__db_query(con, db_config.query_to_list_tables)
					queries_to_drop_tables = db_config.queries_to_drop_multiple_tables(table_list, )

					self.__db_query(con, *[*queries_to_drop_tables])
		else:
			logging.warning(msg=f"Removing Tables only allowed in Dev Enviroment")

	def __build_migrations(self):
		app_list = list(self.__apps_set)
		return self._execute_cmd(*["makemigrations", *app_list])

	def __migrate_databases(self):
		if not self.__migrations_only:
			for db in list(self.__database_set):
				self._execute_cmd("migrate", "--database", db)
		else:
			logging.warning(msg="Migrations Only is Set To True", format=False)

	def configure(self, db_list: list, apps_list: list, **kwargs):

		self.__migrations_only = kwargs.get('migrations_only') == True

		if isinstance(db_list, list) and len(db_list) > 0:
			for db in db_list:
				self.__database_set.add(db)

		if isinstance(apps_list, list) and len(apps_list) > 0:
			for app in apps_list:
				self.__apps_set.add(app)

		remove_tables_from_databases = kwargs.get('remove_tables_from_databases')
		if isinstance(remove_tables_from_databases, list) and len(remove_tables_from_databases) > 0:
			for database in remove_tables_from_databases:
				self.__remove_tables_from_database_set.add(database)

		return self

	def run(self, **kwargs):
		try:
			self.__remove_files()

			if kwargs.get('remove_tables') is True:
				self.__remove_tables()

			self.__build_migrations()
			self.__migrate_databases()
		except Exception as e:
			logging.exception(e)


class DjangoFixtures(DjangoBase):

	def __get_list_of_fixtures_to_load_from_dir(self, dir: str):
		if os.path.isdir(dir):
			return list(filter(lambda f: os.path.splitext(f)[1] == f".{self.file_ext}", os.listdir(dir)))

		else:
			logging.warning(f"Fixture Directory '{dir}' not found.")
			return []

	def load_from_dir(self, dir: str):
		try:
			_fixtures = self.__get_list_of_fixtures_to_load_from_dir(dir=dir)
			self._execute_cmd(*["loaddata", *_fixtures])
			print(f"Succesfully loaded {len(_fixtures)} db fixtures in the following seq:", '\n'.join(_fixtures), sep="\n")
		except Exception as e:
			logging.warning(e)

	def __init__(self, file_ext: str):
		self.file_ext = file_ext
