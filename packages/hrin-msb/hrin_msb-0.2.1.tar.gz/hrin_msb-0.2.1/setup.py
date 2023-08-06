# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['msb_apis',
 'msb_apis.services',
 'msb_apis.views',
 'msb_apis.wrappers',
 'msb_auth',
 'msb_auth.permissions',
 'msb_auth.users',
 'msb_auth.validators',
 'msb_cipher',
 'msb_config',
 'msb_dataclasses',
 'msb_datetime',
 'msb_db',
 'msb_db.models',
 'msb_devtools',
 'msb_exceptions',
 'msb_ext',
 'msb_ext.devtools',
 'msb_files',
 'msb_files.core',
 'msb_http',
 'msb_logging',
 'msb_testing',
 'msb_validation']

package_data = \
{'': ['*']}

install_requires = \
['cerberus>=1.3.4,<2.0.0',
 'cffi>=1.15.1,<2.0.0',
 'cryptography>=38.0.3,<39.0.0',
 'django>=4.1.3,<5.0.0',
 'djangorestframework-simplejwt>=5.2.2,<6.0.0',
 'djangorestframework>=3.14.0,<4.0.0',
 'pandas>=1.5.1,<2.0.0',
 'pdf2docx>=0.5.6,<0.6.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'xhtml2pdf>=0.2.8,<0.3.0']

setup_kwargs = {
    'name': 'hrin-msb',
    'version': '0.2.1',
    'description': '',
    'long_description': '# hrin-msb\n\n## Pre-requisites for setup\n1. `pip install poetry`\n\n## How To Build\n\n1. `poetry build`\n2. `poetry config http-basic.pypi __token__ <access-token>`\n3. `poetry publish`\n\n\n# Change Log\n ### Version 0.1.1\n***\n\n ### Version 0.1.2\n***\n\n ### Version 0.1.3\n***\n\n1.  Default serializer added to ApiView\n2. fixed incorrect import in _validators.py\n3. fixed msb_database_router\n4. fixed Config.is_local_env() not working\n5. moved devscripts -> devtools\n6. File Utils Added to utils/files\n7. "app_label" removed from "TestConfig" & "ApiTest" Classes\n8. Fixed Bug : \'LoggingModelManager\' object has no attribute \'_queryset_class\'\n9. Fixed : Logging Model not showing any records\n10. Fixed : str method for base model, & removed current_timestamp method from base model\n***\n\n ## Version 0.1.4\n1. Fixed : ModuleNotFoundError: No module named \'pdf2docx\'\n2. Renamed “FileGenerator“ => “FileFactory”,\n3. Add `create_` Prefix in FileFactory methods\n4. Renamed MsbMetaModel -> MsbModelMetaFields\n5. Added validation decorators, and fixed bulk validation issuses\n6. Modified Logging Configuration Files\n7. removed utils package\n8. moved msb_core.wrappers.exceptions -> msb_exceptions\n9. Fixed : Base ApiViews and Crud Routes\n10. Searchparameter class refactored, search method added in ApiService Class\n***\n\n## Version 0.1.41\n1. Fixed: Crud operations not working with encrypted id\'s\n2. Package dependencies updated\n3. Validator test cases refactored\n***\n## Version 0.1.5x\n ### -- Version 0.1.51\n1. dbrouter print statement removed\n2. datetime constants renamed (added _FORMAT to all fof them)\n3. Fixed the default argument in msb_exception  which was causing "DESC :" to log even if desc was none\n4. Api service create methdhod not working correctly\n5. file logging handler is not registered in local env by default, we need to pass `emulate_prod=True` to add it \n6. SearchParameter class imported in package.__init__.py \n7. Fixed : test-cases are breaking because of logs databae\n8. added base unittest class, and modified unit_test to inherit djangoTestCase instead of unittest\n9. Added Validation Schema not defined exceptions\n10. Fixed init_django_app error, int datatype instead of str while setting environement variable.\n11. Added use_django decorator to use over classes/functions\n12. Fixed : MsbMetaModel not working\n13. MsbModel meta fields accessor added\n14. Poetry dependencies updated\n15. DMY_DATE_FORMAT added\n16. versioning changed\n\n  ### -- Version 0.1.52\n1. Fixed : MsbMetaFields not working \n2. Fixed : logging model lot of exceptions are thrown if table applicationlogs is not found\n3. Fixed : logging model exceptions file not found\n4. Fixed : db_migration throwing error if no migration dire is found\n5. renamed use_djnago -> use_django, default value for settinfs_dir is added to "app"\n6. renamend _query in msb_model to db_query\n7. field_type, and label added to configuration model\n8. unique_together constraint added to ConfigurationModel\n9. class DjangoMigration creates migration folder if it doesn\'t exists\n10. Added automatic fixture loading\n11. Fixed : msb_model.__str__() was not able to read the primary key value \n12. comma removed from msbMetamodels\n13. Cipher now supports encryption/decryption of list items \n14. SearchParameter modified to supoprt autmatic filter assignment \n15. Refactor `msb_auth` : TokenUser,AuthResult,Constants added\n16. Jwt Token Validation is strict now, it allows only same owner\n  \n### -- Version 0.1.521\n1. Fixed improper import exception\n\n  \n### -- Version 0.1.522\n1. Added Login Required to base viewset\n2. Added Config Object class to msb_dataclasses \n3. Added msb_http to the package\n4. Added MsbDatabaseRouter in init.py\n5. Fixed model.delete() is not working\n\n### -- Version 0.1.611\n1. Modified django migration script\n2. Aded devtools to msb_ext\n3. removed `use_django` decorator & added `requires_django` decorator\n4. added default values for metafields\n5. added InputFiled.time in validation schema types\n\n\n### -- Version 0.2.0\n1. Fixed Cipher.decrypt() returning bytes instead of str\n2. Changed `SearchParameter` class implementation.\n3. default offset & limit fixed in `SearchParameter` class\n\n### -- Version 0.2.1\n1. default values removed from model metafields\n2. Fixed `ModuleNotFoundError: No module named \'_asymmetric_cipher\'`\n',
    'author': 'Prakash Mishra',
    'author_email': 'prakash.mishra@intimetec.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
