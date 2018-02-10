from __future__ import (print_function, division, absolute_import, unicode_literals)
from builtins import *
import click
import json
import os
import sys

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

'''
This module contains the command line utility to install the kernel spec.
'''


# define kernel spec here
kernel_json = { "argv":[sys.executable, "-m", "sc_kernel", "-f", "{connection_file}"],
    "display_name":"SuperCollider",
    "language": "sclang",
    "env": {"PS1":"sc3>"}
}

def install_kernel_spec(user=True, prefix=None):
    with TemporaryDirectory() as td:
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        print('Installing IPython kernel spec')
        KernelSpecManager().install_kernel_spec(td, 'supercollider', user=user, replace=True, prefix=prefix)

@click.command()
def main():
    #TODO add install options - installs to user directory with sys.prefix (virtualenv)
    user = False
    prefix = sys.prefix
    install_kernel_spec(user=user, prefix=prefix)

if __name__ == '__main__':
    main()
