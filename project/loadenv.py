import dotenv, os, subprocess

path = os.path.abspath(os.path.join(__file__, '..', '..'))

def migrate():
    if not os.path.exists(os.path.join(path, 'project', 'migrations')):
        subprocess.run(['flask', 'db', 'init'])

    subprocess.run(['flask', 'db', 'migrate'])
    subprocess.run(['flask', 'db', 'upgrade'])

def get_env(key: str) -> str:
    env_path = os.path.join(path, '.env')
    dotenv.load_dotenv(env_path)
    return  str(dotenv.get_key(env_path, key))
