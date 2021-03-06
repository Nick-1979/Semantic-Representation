from flask import Flask
from .config import Config

app = Flask(__name__)
# Add default configuration to app
app.config.from_object(Config)

from project import routes
