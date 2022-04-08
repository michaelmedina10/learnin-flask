import traceback
from flask_restful import Resource, reqparse
from models.usuario import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from blacklist import BLACKLIST
import traceback
from flask import make_response, render_template

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="Login Field is required")
atributos.add_argument('senha', type=str, required=True, help="Senha Field is required")
atributos.add_argument('email', type=str)
atributos.add_argument('ativado', type=bool)
class User(Resource): 
    # /usuarios/user_id   
    def get(self, user_id):
        try:
            user = UserModel.find_user(user_id)
            if user:
                # Precisa retornar um json mesmo, basta ter um metodo
                # que retorna um dicionário
                return user.json()
            return {'message': 'user not found'}, 404 # Status Code
            
        except :
            return {'message': 'user not found'}, 404 # Status Code
    
    @jwt_required
    def delete(self, user_id):
        try:
            user = UserModel.find_user(user_id)
            if user:
                user.delete_user()
                return {'Message': f'user {user_id} excluido com sucesso'}, 200 
        except :
            return {'Message': f'user {user_id} not found'}, 404
        
class UserRegister(Resource):   
    # /cadastro
    def post(self):
        dados = atributos.parse_args()
        if not dados.get('email') or dados.get('email') is None:
            return {"Message": "The field 'email' can not be left in blank."}, 400
        
        if UserModel.find_by_email(dados['email']):
            return {'Message': "E-mail '{}' already exists".format(dados['email'])}, 400
        
        if UserModel.find_by_login(dados['login']):
            return {'Message': f"Login {dados['login']} already exists."}, 400
        
        user = UserModel(**dados)
        user.ativado = False
        try:
            user.save_user()
            user.send_confirmation_email()
        except:
            user.delete_user()
            traceback.print_exc()
            return {'Message': 'An internal error has ocurred.'}, 400
        return {'Message': f"Usuário {dados['login']} criado com sucesso"}, 201
    
class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])
        if user and safe_str_cmp(user.senha, dados['senha']):
            if user.ativado:    
                token_de_acesso = create_access_token(identity=user.user_id)
                return {'access_token': token_de_acesso}, 200
            return {'Message': 'User not Confirmed'}, 400
        return {'Message': 'Username or Password is incorrect'}, 401 # não autorizado
    
class UserLogout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti'] # JWT Token Identifier
        BLACKLIST.add(jwt_id)
        return {'Message': 'Logged out Successfully!'}, 200
    
class UserConfirm(Resource):
    # URI = Raiz_do_site/confirmacao/{user_id
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_user(user_id)
        if not user:
            return {'Message': "User id '{}' not found".format(user_id)}, 404
        user.ativado = True
        user.save_user()
        # return {'Message': "User id '{}' confirmed successfully".format(user_id
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('user_confirm.html', email=user.email, usuario=user.login), 200, headers)

        # JINJA Template permite acessar os parametros email e usuario no codigo html
        # Com a sintaxe "{{email}}"
        
    