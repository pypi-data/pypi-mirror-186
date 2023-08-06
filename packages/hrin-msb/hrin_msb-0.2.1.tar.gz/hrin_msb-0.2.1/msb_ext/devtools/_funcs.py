from msb_devtools import (init_django_app, DjangoMigration, DjangoFixtures)
from pathlib import Path
import logging,os

APP_DIRECTORY_NAME = "app"
RESOURCE_DIRECTORY_NAME = "resources"
WRITABLE_DIRECTORY_NAME = "writable"
FIXTURES_DIRECTORY_NAME = "fixtures"

BASE_DIR = Path(Path.cwd().__str__().split(RESOURCE_DIRECTORY_NAME)[0])
APP_DIR = BASE_DIR.joinpath(APP_DIRECTORY_NAME)
RESOURCE_DIR = BASE_DIR.joinpath(RESOURCE_DIRECTORY_NAME)
WRITABLE_DIR = BASE_DIR.joinpath(WRITABLE_DIRECTORY_NAME)
FIXTURES_DIR = RESOURCE_DIR.joinpath(FIXTURES_DIRECTORY_NAME)


def get_default_msb_dirs():
	return [BASE_DIR.__str__(), APP_DIR.__str__(), RESOURCE_DIR.__str__(), WRITABLE_DIR.__str__()]


def require_django(_func):
	def inner_func(*args, **kwargs):
		from msb_devtools import init_django_app
		init_django_app(settings_dir=APP_DIRECTORY_NAME, sys_pathlist=get_default_msb_dirs())
		return _func(*args, **kwargs)

	return inner_func


@require_django
def run_database_migrations(app_name: str, dblist: list, is_dev_env: bool, apps: list, **opt):
	try:
		from django.conf import settings
		migration_directory = os.path.join(settings.APP_DIR, app_name, "migrations")

		# perform risks ?
		allow_risky_operation = settings.IS_LOCAL_ENVIRONMENT

		# list of database to run migrations on
		database_list = dblist if len(dblist) > 0 else list(settings.DATABASES.keys())

		drop_tables: bool = opt.get("remove_tables") == True
		remove_files: bool = opt.get("remove_files") == True
		db_to_remove_tables_from: list = opt.get("db_to_remove_tables_from") or []

		migration = DjangoMigration(
			migration_dir=migration_directory,
			is_dev_env=is_dev_env,
			remove_files=remove_files,

		)
		migration.configure(db_list=database_list, apps_list=apps, remove_tables_from_databases=db_to_remove_tables_from)

		return migration.run(remove_tables=drop_tables)
	except Exception as e:
		logging.exception(e)


@require_django
def load_database_fixtures(*from_dirs, is_json=False):
	fixture_extention = "json" if is_json else "yaml"
	for fixture_dir in from_dirs:
		fixture_dir = FIXTURES_DIR.joinpath(fixture_dir.lower())
		fixtures = DjangoFixtures(file_ext=fixture_extention)
		fixtures.load_from_dir(dir=fixture_dir)
