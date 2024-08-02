from flask import Blueprint, jsonify, request
from src.main.factories.calculator01_factory import calculator01_factory
from src.main.factories.calculator02_factory import calculator02_factory

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_01():
    calc = calculator01_factory()
    response = calc.calculate(request)

    return jsonify(response)

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_02():
    calc = calculator02_factory()
    response = calc.calculate(request)

    return jsonify(response)