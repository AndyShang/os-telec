from flask import Flask

app = Flask(__name__)
	
def create_app(config=None):
    return app

import myapp.views