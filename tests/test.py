from test_version import *

try:
    test_version()

    print('ALL TESTS PASSED!')

except Exception as e:
    print('Error!')
    print(e.args[0])