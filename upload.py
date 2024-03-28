import clean
import os

PYTHON = '.venv/bin/python3'
PIP = '.venv/bin/pip3'


def exit_if_error(code):
    # if an error has occurred, stop execution
    if code != 0:
        print(f'\nUpload stopped. Error code {code}.')
        exit(code)


# clean
print('CLEANING...')
clean.clean()

# check-branch
# TODO

# test
print('\nTESTING...')

exit_if_error(
    os.system(f'{PYTHON} tests/test.py')
)

# build
print('\nBUILDING...')
exit_if_error(
    os.system(f'{PYTHON} -m build')
)

# check
print('\nCHECKING...')
exit_if_error(
    os.system('twine check dist/*')
)

# confirm
confirmation = input('\nAll looks good. Upload? (Y/n) ')
if confirmation == '' or \
        confirmation.lower() == 'y':
    # upload
    print('\nUPLOADING...')
    exit_if_error(
        os.system('twine upload dist/*')
    )

# clean again
print('\nCLEANING...')
clean.clean()