import flask_migrate, flask_sqlalchemy, os
from .settings import project

path = os.path.abspath(os.path.join(__file__, '..', '..'))

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
DATA_BASE = flask_sqlalchemy.SQLAlchemy(project)
MIGRATE = flask_migrate.Migrate(project, DATA_BASE, os.path.join(path, 'project', 'migrations'))
