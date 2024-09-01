from flask import Flask
from src.main.routes.calculators import calc_bp_route

app = Flask(__name__)

app.register_blueprint(calc_bp_route)