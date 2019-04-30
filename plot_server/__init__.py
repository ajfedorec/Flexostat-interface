from flask import Flask

app = Flask(__name__, static_url_path='/static')

from plot_server.views import general
