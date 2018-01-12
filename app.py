from connexion.resolver import RestyResolver
import connexion
from livereload import Server
from injector import Binder
from flask_injector import FlaskInjector
from services.provider import ItemsProvider


def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name": "Test 1"}])
    )

    return binder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.debug = True
    server = Server(app)
    server.watch('api/*.py')
    server.watch('swagger/*.yaml')
    server.serve(9090)