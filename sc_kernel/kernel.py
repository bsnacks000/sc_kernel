
from __future__ import (print_function, division, absolute_import, unicode_literals)

from builtins import *

from ipykernel.kernelbase import Kernel
from pexpect import replwrap, EOF
import pexpect
import signal


class SuperColliderKernel(Kernel):
    ''' This kernel is an adaptation from the ipykernel docs, the
     bash_kernel example by takluyver and a few other REPLWrapper kernels
    '''

    implementation = 'SuperCollider'
    implementation_version = '0.0.1'
    language_version = '3'
    language_info = {
        'name': 'sclang',
        'mimetype': 'text/x-sclang',
        'file_extension': '.scd'
    }
    banner = 'SuperCollider kernel - make bleeps and bloops'

    def __init__(self, **kwargs):
        super(SuperColliderKernel, self).__init__(**kwargs)
        self._init_sc()

    def _init_sc(self):
        ''' initialize the sc repl wrapper class'''

        sig = signal.signal(signal.SIGINT, signal.SIG_DFL)
        try:
            self.scwrapper = replwrap.REPLWrapper('sclang', u'sc3>', None) # cretes the child process

        finally:
            signal.signal(signal.SIGINT, sig)


    def _execute_sclang(self, code):
        interrupted = False
        try:
            output = self.scwrapper.run_command(code.rstrip(), timeout=None)

        except KeyboardInterrupt as err:
            self.scwrapper.child.sendintr()
            interrupted = True
            self.scwrapper._expect_prompt()
            output = self.scwrapper.child.before

        except EOF as err:
            output = self.scwrapper.child.before + 'restarting sclang'
            self._init_sc()

        return interrupted, output

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        ''' executes the code in the cell by passing to wrapper.run_command
        '''
        if not code.strip():
            return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

        interrupted, output = self._execute_sclang(code)

        if not silent:
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        if interrupted:
            return {'status': 'abort', 'execution_count': self.execution_count}

        if 'ERROR: ' in output:
            return {'status': 'error', 'execution_count': self.execution_count,
                    'ename': '', 'evalue': output, 'traceback': []}

        return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}
