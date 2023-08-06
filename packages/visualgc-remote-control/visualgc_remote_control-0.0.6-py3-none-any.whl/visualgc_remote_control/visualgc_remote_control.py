import argparse
import logging
import os
import sys
from logging import handlers
from visualgc_remote_control.enterprise import RemoteControlException
from visualgc_remote_control.remote_control_app import RemoteControlApp
from visualgc_remote_control.remote_commands import RemoteCommand

# VERSION = '0.0.4'  # Redo imports
# VERSION = '0.0.5'  # Use absolute path
VERSION = '0.0.6'  # Add test folder command line


class VisualgcRemoteControl:

    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.work_dir = os.path.join(self.current_dir, 'tmp')
        self.commands = RemoteCommand()
        msg = f'running on Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}-{sys.version_info.releaselevel}'
        logging.debug(msg)

    @staticmethod
    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean new_value expected, got {}'.format(v))

    @staticmethod
    def main():
        my_log = logging.getLogger()
        my_log.setLevel(logging.DEBUG)
        my_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        my_ch = logging.StreamHandler(sys.stdout)
        my_ch.setFormatter(my_fmt)
        my_log.addHandler(my_ch)
        my_fh = handlers.RotatingFileHandler('visualgc_remote_control.log', maxBytes=(1048576 * 5), backupCount=7)
        my_fh.setFormatter(my_fmt)
        my_log.addHandler(my_fh)

        logging.info(f'start...')
        logging.info(f'VisualGC remote control {VERSION}')
        p = VisualgcRemoteControl()
        parser = argparse.ArgumentParser(prog='visualgc_remote_control.py')

        subparsers = parser.add_subparsers()
        subparsers.required = True
        subparsers.dest = 'command'
        subparser = subparsers.add_parser("START_SERVER", help="Accept certificate from the controller")
        subparser = subparsers.add_parser("ACCEPT_CERTIFICATE", help="Accept certificate from the controller")
        subparser = subparsers.add_parser("TEST_FOLDER", help="Test Folder")
        subparsers.add_parser("VERSION", help="Print version")
        ret = 0

        try:
            args = parser.parse_args()
            if  args.command == 'START_SERVER':
                p.start_server()
            elif args.command == 'ACCEPT_CERTIFICATE':
                p.accept_certificate()
            elif args.command == 'VERSION':
                logging.info('version={0}'.format(VERSION))
            else:
                parser.print_help()
            logging.info('... all done')

        except RemoteControlException as e:
            logging.error(e)
            logging.info('... exiting with error')

    def accept_certificate(self):
        # run autoit executable
        self.commands.accept_certificate()

    def test_folder(self):
        self.commands.test_script_folder()

    def start_server(self):
        my_server = RemoteControlApp.run()


if __name__ == "__main__":
    VisualgcRemoteControl.main()



