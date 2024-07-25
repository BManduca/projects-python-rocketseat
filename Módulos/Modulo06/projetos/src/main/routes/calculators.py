from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_01():
    print(request.json)

    return jsonify({'success': True})