from connexion.resolver import RestyResolver
import connexion
from livereload import Server


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    app.debug = True
    server = Server(app)
    server.watch('api/*.py')
    server.watch('swagger/*.yaml')
    server.serve(9090)