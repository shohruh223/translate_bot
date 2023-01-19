from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')
APP_ID = env('APP_ID')
APP_KEY = env('APP_KEY')