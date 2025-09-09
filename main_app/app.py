import flask, os

path = os.path.abspath(os.path.join(__file__, '..'))

app = flask.Blueprint(
    import_name = 'main_app',
    name = 'app',
    template_folder = os.path.join(path, 'templates'),
    static_folder = os.path.join(path, 'static'),
    static_url_path = '/static_main'
)