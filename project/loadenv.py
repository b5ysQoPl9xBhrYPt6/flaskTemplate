import dotenv, os

path = os.path.abspath(os.path.join(__file__, '..', '..'))

def get_env(key: str) -> str:
    env_path = os.path.join(path, '.env')
    dotenv.load_dotenv(env_path)
    return  str(dotenv.get_key(env_path, key))
