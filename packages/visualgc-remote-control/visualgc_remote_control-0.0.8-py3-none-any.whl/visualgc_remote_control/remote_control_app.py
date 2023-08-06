import logging

from flask import Flask, Response, render_template
from visualgc_remote_control.remote_commands import RemoteCommand

global_command_facade = RemoteCommand()


class RemoteControlApp:

    @staticmethod
    def run():
        app = Flask(__name__)
        app.add_url_rule('/', view_func=RemoteControlApp.index, methods=['GET'])
        app.add_url_rule('/accept_certificate', view_func=RemoteControlApp.accept_certificate, methods=['GET'])
        app.add_url_rule('/folder_test', view_func=RemoteControlApp.test_script_folder, methods=['GET'])
        # app.register_error_handler(404, RemoteControlApp.page_not_found)
        logging.getLogger('werkzeug').disabled = True
        debug_mode = True
        app.run(host="0.0.0.0", debug=debug_mode)

    @staticmethod
    def index():
        # http://localhost:5000/
        return "<h1>This is my indexpage</h1>"

    @staticmethod
    def accept_certificate():
        # return Response('certificate found', status=200, headers={})
        if global_command_facade.accept_certificate():
            return Response('accept certificate OK', status=200, headers={})
        else:
            msg = f'unable to run command accept_certificate'
            logging.error(msg)
            return Response(msg, status=500, headers={})

    @staticmethod
    def test_script_folder():
        # return Response('certificate found', status=200, headers={})
        if global_command_facade.test_script_folder():
            return Response('Test OK', status=200, headers={})
        else:
            msg = f'unable to run Test'
            logging.error(msg)
            return Response(msg, status=500, headers={})

    @staticmethod
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404







