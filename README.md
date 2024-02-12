This is my Result:

Niranjan kumar@LAPTOP-OSH3L9DM MINGW64 ~/desktop/aim5005 (main)
$ python -m pytest tests/test_features.py
============================= test session starts =============================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: C:\Users\Niranjan kumar\desktop\aim5005
plugins: anyio-3.5.0
collected 8 items

tests\test_features.py ........                                          [100%]

============================== 8 passed in 0.50s ==============================


## AIM 5005

### Install
1. `git clone git@github.com:mzelenetz/aim5005.git`
2. `cd aim5005`
3. `make install`
4. You can ensure the test pass by running `make` (which defaults to `make tests`)

### Use
- `make` will build and run all tests
- `make lr` will only run the tests for linear regression
- `make features` will run the test for features (this is your first assignment)

