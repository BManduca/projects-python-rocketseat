from flask import Blueprint, jsonify, request
from src.main.factories.calculator04_factory import calculator04_factory

from src.errors.error_controller import handle_errors

calc_bp_route = Blueprint('calc_routes', __name__)

@calc_bp_route.route('/calculator/4', methods=['POST'])
def calculator_04():
  try:
    calc = calculator04_factory()
    response = calc.calculate(request)

    return jsonify(response)
  except Exception as exception:
    error_response = handle_errors(exception)

    return jsonify(
      error_response['body']
    ), error_response['status_code']