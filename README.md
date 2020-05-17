
# Instructions
## Run all tests with:
python -m unittest
## Pyunit is an implementation of JUnit

#### the SetUpClass method is executed once before all tests
#### the TearDownClass method is executed once after all tests
#### the SetUp method is executed before each test
#### the TearDown method is executed after each test

# Tips
Use 'assertRaises' for Exceptions instead of try...catch
    assertRaises(ExceptionClass, method, params...)

# Limitations
PyUnit framework doesn't contain any support for timeout
You can try timeout-decorator library from PyPI.

unittest does not support checking for files

# Examples

![Simple Test Example](/screenshots/entity.png)

## SetUp and TearDown
![SetUp](/screenshots/setUp.png)
![SetUpClass](/screenshots/setUpClass.png)

![TearDown](/screenshots/tearDown.png)
![TearDownClass](/screenshots/tearDownClass.png)

## Create suite
![Suite](/screenshots/suiteCreate.png)

## Skip tests
![Skip](/screenshots/skip.png)