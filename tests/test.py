from test_version import *

try:
    test_version()

except Exception as e:
    print('Error!')
    print(e)
    exit(1)

print('ALL TESTS PASSED!')