from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
# db= SQLAlchemy(app)

# class User(db.Model):
#     _tablename_ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), nullable=False)

#     def json(self):
#       return {'id': self.id, 'name': self.name, 'email': self.email}
    
# db.create_all()

@app.route('/', methods=['GET'])
def home():

    docker_ascii = '''\
          ##         .
    ## ## ##        ==
 ## ## ## ## ##    ===
/"""""""""""""""""\___/ ===
{                       /  ===-
\______ -0-         __/
 \    \         __/
  \____\_______/

Hello from Docker!
'''
    return '<pre>' + docker_ascii + '</pre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

# post user
# @app.route('/users', methods=['POST'])
# def post_users():
#     try:
#         data = request.get_json()
#         new_user = User(name=data['name'], email=data['email'])
#         db.session.add(new_user)
#         db.session.commit()
#         return make_response(jsonify(new_user.json()), 201)
#     except e:
#         return make_response(jsonify({'error': 'Bad request'}), 400)

# # get a users    
# @app.route('/users', methods=['GET'])
# def get_users():
#         try:
#          users = User.query.all()
#          users_json = [user.json() for user in users]
#          return make_response(jsonify(users_json), 200)
#         except e:   
#           return make_response(jsonify({'error': 'Bad request'}), 400)
        
# #get a user by id
# @app.route('/users/<int:id>', methods=['GET'])
# def get_user(id):
#     try:
#         user = User.query.get(id)
#         if user:
#             return make_response(jsonify(user.json()), 200)
#         else:
#             return make_response(jsonify({'error': 'User not found'}), 404)
#     except e:
#         return make_response(jsonify({'error': 'Bad request'}), 400)
# # update a user
# @app.route('/users/<int:id>', methods=['PUT'])
# def update_user(id):
#     try:
#         user = User.query.get(id)
#         if user:
#             data = request.get_json()
#             user.name = data['name']
#             user.email = data['email']
#             db.session.commit()
#             return make_response(jsonify(user.json()), 200)
#         else:
#             return make_response(jsonify({'error': 'User not found'}), 404)
#     except e:
#         return make_response(jsonify({'error': 'Bad request'}), 400)
    
# #delete a user
# @app.route('/users/<int:id>', methods=['DELETED'])
# def delete_user(id):
#     try:
#         user = User.query.get(id)
#         if user:
#             db.session.delete(user)
#             db.session.commit()
#             return make_response(jsonify({'message': 'User deleted'}), 200)
#         else:
#             return make_response(jsonify({'error': 'User not found'}), 404)
#     except e:
#         return make_response(jsonify({'error': 'Bad request'}), 400)