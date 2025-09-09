import flask, os, main_app

path = os.path.abspath(os.path.join(__file__, '..', '..'))

project = flask.Flask(
    import_name = 'project'
)

project.register_blueprint(main_app.app)