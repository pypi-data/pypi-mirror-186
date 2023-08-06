import logging
import os
import platform
import subprocess


class RemoteCommand:

    def __init__(self):
        self.work_dir = os.path.dirname(os.path.abspath(__file__))
        self.script_folder = 'au3_scripts'

    def accept_certificate(self):
        logging.debug(f'running from {self.work_dir}')
        cmd = os.path.join(f'{self.script_folder}', 'accept_certificate.exe')
        try:
            RemoteCommand._run_command(cmd)
            return True
        except FileNotFoundError as e:
            logging.error(e)
            return False

    def test_script_folder(self):
        logging.debug(f'running from {self.work_dir}')
        cmd = os.path.join(f'{self.script_folder}', 'test.txt')
        if platform.system().lower() == 'linux':
            try:
                RemoteCommand._run_command(f'cat {cmd}')
                return True
            except FileNotFoundError as e:
                logging.error(e)
                return False

        elif platform.system().lower() == 'windows':
            try:
                RemoteCommand._run_command(f'type {cmd}')
                return True
            except FileNotFoundError as e:
                logging.error(e)
                return False
        else:
            logging.error(f'not running on linux or windows'
                          f' can\'t run cat or type, current system is {platform.system()}')
            return False

    @staticmethod
    def _run_command(cmd):
        cmd = cmd.split()
        logging.debug('command in list format:{}'.format(cmd))
        output = subprocess.check_output(cmd, shell=False)
        logging.info(f'response is {output} of type {type(output)}')

