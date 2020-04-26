
from os import environ

from app import app

HOST = environ.get('FLASK_HOST', '0.0.0.0')
PORT = int(environ.get('FLASK_PORT', 5000))
DEBUG = bool(environ.get('FLASK_DEBUG', True))

app.run(host=HOST, port=PORT, debug=DEBUG)