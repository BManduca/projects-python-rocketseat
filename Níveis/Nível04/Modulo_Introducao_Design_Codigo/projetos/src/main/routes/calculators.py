from flask import Blueprint, jsonify, request
from src.main.factories.calculator01_factory import calculator01_factory
from src.main.factories.calculator02_factory import calculator02_factory
from src.main.factories.calculator03_factory import calculator03_factory

from src.errors.error_controller import handle_errors

'''
   nomeando as rotas relacionadas as calculadoras apartir 
   do calc_route_bp 
'''
calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_01():
    try:
        calc = calculator01_factory()
        response = calc.calculate(request)

        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)

        return jsonify(error_response['body']), error_response['status_code']

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_02():
    try:
        calc = calculator02_factory()
        response = calc.calculate(request)

        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)

        return jsonify(error_response['body']), error_response['status_code']

@calc_route_bp.route('/calculator/3', methods=['POST'])
def calculator_03():
    try:
        calc = calculator03_factory()
        response = calc.calculate(request)

        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)

        return jsonify(error_response['body']), error_response['status_code']
