from flask import Flask, jsonify, request
from models.user import User
from models.meal import Meal
from database import db


# config init Flask
app = Flask(__name__)

# área de config banco
app.config['SECRET_KEY'] = 'data_developer_diet_meals'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mand_42#21@127.0.0.1:3308/daily-diet-api"

db.init_app(app)

# CREATE MEAL
@app.route('/meal', methods=['POST'])
def create_meal():
    data = request.json
    name = data.get('nome_refeicao')
    description = data.get('descricao_refeicao')
    date_time = data.get('data_hora_refeicao')
    present_diet = data.get('presente_na_dieta')
    user_id = int(data.get('usuario'))

    if name and description and date_time and user_id:
        '''
            filtrando registros na base de dados e 
            como é retornado uma lista nessa filtragem,
            será necessário 'pegar' somente a primeira
            ocorrência, por isso o uso do first.
        '''
        user = User.query.filter_by(id=user_id).first()
        if user:
            meal = Meal(name=name, description=description, date_time=date_time, present_diet=present_diet, user_id=user_id)
            db.session.add(meal)
            db.session.commit()
            return jsonify({'message':f'REFEIÇÃO {meal.id} => {meal.name.upper()} VINCULADA AO USUÁRIO {user_id} FOI CADASTRADA COM SUCESSO!'})
        
    return jsonify({'message':'DADOS INVÁLIDOS OU FORAM INSERIDOS DE MANEIRA INCORRETA!'}), 400

# UPDATE USER MEAL
@app.route('/meal/<int:id_meal>', methods=['PUT'])
def update_meal(id_meal):
    data = request.json
    name = data.get('nome_refeicao')
    description = data.get('descricao_refeicao')
    date_time = data.get('data_hora_refeicao')
    present_diet = data.get('presente_na_dieta')
    user_id = int(data.get('usuario'))

    if id_meal:
        meal = Meal.query.get(id_meal)
        user = User.query.get(user_id)

        if user is None:
            return jsonify({'message':f'USUÁRIO {user_id} NÃO REGISTRADO!'}), 404
        
        if meal is None: 
            return jsonify({"message": f"REFEIÇÃO {id_meal} NÃO REGISTRADA" }), 404
        
        if name and description and date_time and present_diet:
            meal.name = name
            meal.description = description
            meal.date_time = date_time
            meal.present_diet = present_diet
            meal.user_id = user_id
            db.session.commit()

            return jsonify({'message':f'REFEIÇÃO {id_meal} DO USUÁRIO {user_id} FOI ATUALIZADA COM SUCESSO!'})
        
        return jsonify({'message':f'DADOS DA REFEIÇÃO {id_meal} VINCULADOS AO USUÁRIO {user_id} ESTÃO INCOMPLETOS!'}), 404
    
    return jsonify({'message':f'NÃO FOI ENCONTRADO REGISTRO DA REFEIÇÃO {id_meal} VINCULADO AO USUÁRIO {user_id}!'}), 404

# DELETE USER MEAL
@app.route('/meal/<int:id_meal>', methods=['DELETE'])
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        db.session.delete(meal)
        db.session.commit()

        return jsonify({'message':f'REFEIÇÃO {id_meal} VINCULADA AO USUÁRIO {meal.user_id} FOI DELETADA COM SUCESSO!'})
    
    return jsonify({'message':f'REFEIÇÃO {id_meal} NÃO ENCONTRADA'}), 404

# LIST A USER'S MEALS
@app.route('/meals/<int:user_id>', methods=['GET'])
def get_all_user_meals(user_id):
    meals = Meal.query.filter(user_id == Meal.user_id).all()

    if meals:
        meal_user_data = [{'id': meal.id,
                           'nome_refeicao': meal.name,
                           'descricao_refeicao': meal.description, 
                           'data_hora_refeicao': meal.date_time,
                           'presente_na_dieta': meal.present_diet,
                           'id_usuario': meal.user_id,
                           'usuario': meal.user.username } for meal in meals ]
        return jsonify({'message': meal_user_data})
    return jsonify({'message':f'NENHUMA REFEIÇÃO VINCULADA AO USUÁRIO {user_id} FOI ENCONTRADA!'}), 404

# LIST SINGLE USER MEAL
@app.route('/meal/<int:id_meal>', methods=['GET'])
def get_single_user_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        return jsonify({'meal':{
            'nome_refeicao': meal.name,
            'descricao_refeicao': meal.description,
            'data_hora_refeicao': meal.date_time,
            'presente_na_dieta': meal.present_diet,
            'id_usuario': meal.user_id,
            'usuario': meal.user.username
        }})
    return jsonify({'message':f'REFEIÇÃO {id_meal} NÃO FOI REGISTRADO NO SISTEMA!'}), 404

if __name__ == '__main__':
     app.run(port=8000, debug=True)