from flask_script import Manager, Shell
import pytest

from app import app

manager = Manager(app, with_default_commands=False)
manager.add_command("shell", Shell())


@manager.command
@manager.option('-c', '--config', dest="config_file_path",
                help="Configuration file path", default="./config/default.py", required=False)
def run(config_file_path="./config/default.py"):
    """
    Run server
    """
    app.config.from_pyfile(config_file_path)
    from controller.api import api
    from controller.web import web
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(web)
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])


@manager.command
def test():
    """
    Run all tests
    """
    app.config.from_pyfile('./config/testing.py')
    pytest.main()

if __name__ == '__main__':
    manager.run()
