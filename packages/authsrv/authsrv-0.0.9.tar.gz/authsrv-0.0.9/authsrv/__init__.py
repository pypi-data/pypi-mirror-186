'''
Wrapper around authsrv utilities from https://github.com/unixtools/authsrv
'''

import subprocess
from subprocess import PIPE

import getpass

__author__ = 'Nathan Neulinger'
__url__ = 'https://github.com/unixtools/authsrv-python'
__version__ = '0.0.9'

_authsrv_py_global_cache = {}


def fetch(owner: str = None, user='', instance='') -> str:
    '''Retrieve a stash from authsrv'''

    if owner is None:
        owner = getpass.getuser()

    if user == '' or instance == '':
        return None

    cache_key = "/".join([owner, user, instance])

    # TODO: Give the cache a lifetime

    # Check if present in cache
    if cache_key in _authsrv_py_global_cache:
        return _authsrv_py_global_cache[cache_key]

    # Wasn't found in cache, try retrieving
    try:

        password = subprocess.check_output(["authsrv-decrypt", owner, user, instance], stderr=PIPE)
        if password != "" and password is not None:
            password = password.decode('utf-8')
        password = password.rstrip('\n\r')

        _authsrv_py_global_cache[cache_key] = password
    except subprocess.CalledProcessError:
        password = None
        _authsrv_py_global_cache[cache_key] = None

    return password
