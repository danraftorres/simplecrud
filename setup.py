import environ

base = environ.Path(__file__)  - 1 # two folders back (/a/b/ - 2 = /) # /home/daniel/Documentos/ProyectosDjango/simplecrud

env = environ.Env()
env.read_env(env_file=base('.env')) # reading .env file

