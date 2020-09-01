from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(11))
    CPF = db.column(db.String(11))

class Curso(db.Model):
    id_matricula = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    
Pessoa_put_args = reqparse.RequestParser()
Pessoa_put_args.add_argument("id", type=int, help="ID", required= True)
Pessoa_put_args.add_argument("nome", type=str, help="Nome", required= True)
Pessoa_put_args.add_argument("telefone", type=str, help="Telefone", required= True)
Pessoa_put_args.add_argument("CPF", type=str, help="CPF", required= True)
Curso_put_args.add_argument("Id Matricula", type=str, help="Id matricula", required = True)
Curso_put_args.add_argument("nome", type=str, help="Nome", required = True)

resource_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'telefone': fields.String,
    'CPF': fields.String
    }

class Pessoa(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = Pessoa.query.get(id=id)
        return result

    @marshal_with(resource_fields)
    def put(self, id):
        args = Pessoa_put_args.parse_args()
        id = Pessoa(id=id, nome=args['nome'], telefone=args['telefone'], cpf=args['cpf'])
        db.session.add(id)
        db.session.commit()
        return Pessoa, 201

    def delete(self, id):
        del videos[video_id]
        return'',204

class Curso(Resource):
    @marshal_with(resource_fields)
    def get(self, id_matricula):
        result = Curso.query.get(id_matricula=id_matricula)
        return result

    @marshal_with(resource_fields)
    def put(self,id_matricula):
        args = Curso_put_args.parse_args()
        id_matricula = Curso(id_matricula=idmatricula, nome=args['nome'])
        db.session.add(id_matricula)
        db.session.commit()

api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
