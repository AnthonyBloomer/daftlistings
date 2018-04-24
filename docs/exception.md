Module daftlistings.exception
-----------------------------

Classes
-------
#### DaftInputException 
##### Ancestors (in MRO)
- daftlistings.exception.DaftInputException

- exceptions.Exception

- exceptions.BaseException

- __builtin__.object

##### Class variables
- **args**

- **message**

##### Instance variables
- **reason**

##### Methods
- **__init__** (self, reason)

#### DaftRequestException 
##### Ancestors (in MRO)
- daftlistings.exception.DaftRequestException

- exceptions.Exception

- exceptions.BaseException

- __builtin__.object

##### Class variables
- **args**

- **message**

##### Instance variables
- **reason**

- **status_code**

##### Methods
- **__init__** (self, status_code, reason)
