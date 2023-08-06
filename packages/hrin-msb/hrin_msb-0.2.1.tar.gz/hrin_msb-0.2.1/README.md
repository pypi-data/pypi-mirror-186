# hrin-msb

## Pre-requisites for setup
1. `pip install poetry`

## How To Build

1. `poetry build`
2. `poetry config http-basic.pypi __token__ <access-token>`
3. `poetry publish`


# Change Log
 ### Version 0.1.1
***

 ### Version 0.1.2
***

 ### Version 0.1.3
***

1.  Default serializer added to ApiView
2. fixed incorrect import in _validators.py
3. fixed msb_database_router
4. fixed Config.is_local_env() not working
5. moved devscripts -> devtools
6. File Utils Added to utils/files
7. "app_label" removed from "TestConfig" & "ApiTest" Classes
8. Fixed Bug : 'LoggingModelManager' object has no attribute '_queryset_class'
9. Fixed : Logging Model not showing any records
10. Fixed : str method for base model, & removed current_timestamp method from base model
***

 ## Version 0.1.4
1. Fixed : ModuleNotFoundError: No module named 'pdf2docx'
2. Renamed “FileGenerator“ => “FileFactory”,
3. Add `create_` Prefix in FileFactory methods
4. Renamed MsbMetaModel -> MsbModelMetaFields
5. Added validation decorators, and fixed bulk validation issuses
6. Modified Logging Configuration Files
7. removed utils package
8. moved msb_core.wrappers.exceptions -> msb_exceptions
9. Fixed : Base ApiViews and Crud Routes
10. Searchparameter class refactored, search method added in ApiService Class
***

## Version 0.1.41
1. Fixed: Crud operations not working with encrypted id's
2. Package dependencies updated
3. Validator test cases refactored
***
## Version 0.1.5x
 ### -- Version 0.1.51
1. dbrouter print statement removed
2. datetime constants renamed (added _FORMAT to all fof them)
3. Fixed the default argument in msb_exception  which was causing "DESC :" to log even if desc was none
4. Api service create methdhod not working correctly
5. file logging handler is not registered in local env by default, we need to pass `emulate_prod=True` to add it 
6. SearchParameter class imported in package.__init__.py 
7. Fixed : test-cases are breaking because of logs databae
8. added base unittest class, and modified unit_test to inherit djangoTestCase instead of unittest
9. Added Validation Schema not defined exceptions
10. Fixed init_django_app error, int datatype instead of str while setting environement variable.
11. Added use_django decorator to use over classes/functions
12. Fixed : MsbMetaModel not working
13. MsbModel meta fields accessor added
14. Poetry dependencies updated
15. DMY_DATE_FORMAT added
16. versioning changed

  ### -- Version 0.1.52
1. Fixed : MsbMetaFields not working 
2. Fixed : logging model lot of exceptions are thrown if table applicationlogs is not found
3. Fixed : logging model exceptions file not found
4. Fixed : db_migration throwing error if no migration dire is found
5. renamed use_djnago -> use_django, default value for settinfs_dir is added to "app"
6. renamend _query in msb_model to db_query
7. field_type, and label added to configuration model
8. unique_together constraint added to ConfigurationModel
9. class DjangoMigration creates migration folder if it doesn't exists
10. Added automatic fixture loading
11. Fixed : msb_model.__str__() was not able to read the primary key value 
12. comma removed from msbMetamodels
13. Cipher now supports encryption/decryption of list items 
14. SearchParameter modified to supoprt autmatic filter assignment 
15. Refactor `msb_auth` : TokenUser,AuthResult,Constants added
16. Jwt Token Validation is strict now, it allows only same owner
  
### -- Version 0.1.521
1. Fixed improper import exception

  
### -- Version 0.1.522
1. Added Login Required to base viewset
2. Added Config Object class to msb_dataclasses 
3. Added msb_http to the package
4. Added MsbDatabaseRouter in init.py
5. Fixed model.delete() is not working

### -- Version 0.1.611
1. Modified django migration script
2. Aded devtools to msb_ext
3. removed `use_django` decorator & added `requires_django` decorator
4. added default values for metafields
5. added InputFiled.time in validation schema types


### -- Version 0.2.0
1. Fixed Cipher.decrypt() returning bytes instead of str
2. Changed `SearchParameter` class implementation.
3. default offset & limit fixed in `SearchParameter` class

### -- Version 0.2.1
1. default values removed from model metafields
2. Fixed `ModuleNotFoundError: No module named '_asymmetric_cipher'`
