
from __future__ import (print_function, division, absolute_import, unicode_literals)

from builtins import *

from ipykernel.kernelbase import Kernel
from pexpect import replwrap
import pexpect
import signal


class SuperColliderKernel(Kernel):
    ''' This kernel is an adaptation from the ipykernel docs and the
     bash_kernel example by takluyver
    '''

    implementation = 'SuperCollider'
    implementation_version = '0.0.0'
    language_info = {
        'name': 'sclang',
        'mimetype': 'text/x-sclang',
        'file_extension': '.scd'
    }

    def __init__(self, **kwargs):
        super(SuperColliderKernel).__init__(**kwargs)
        self._init_sc()

    def _init_sc(self):
        ''' initialize the sc repl wrapper class'''

        # NOTE this is pretty simple for now, need to check out the subprocess interupt
        self.scwrapper = replwrap.REPLWrapper('sclang', u'sc3>', None) # cretes the child process

    def do_execute(self, code, silent, store_history=True, allow_stdin=False):
        ''' executes the code in the cell by passing to wrapper.run_command
        '''
        if not code.strip():
            return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

        #NOTE needs error handling and keyboard interupt handling 
        self.scwrapper.run_command(code.rstrip(), timeout=None)

        if not silent:
            output = self.scwrapper.child.before  # this gets the last streamed output from the child process
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}
