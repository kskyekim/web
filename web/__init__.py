"This is the website python package initializer."
import flask

# create new flask object
app = flask.Flask(__name__)

# read settings from config (web/config.py)
app.config.from_object("web.config")