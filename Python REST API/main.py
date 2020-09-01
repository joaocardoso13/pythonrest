from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class PessoaModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(11))
    CPF = db.Column(db.String(11))

    def __repr__(self):
        return f"Pessoa(id= {id}, nome= {nome}, telefone= {telefone}, CPF= {CPF})"

class CursoModel(db.Model):
    id_matricula = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f"Curso(id_matricula= {id_matricula}, nome= {nome})"
    
Pessoa_put_args = reqparse.RequestParser()
Pessoa_put_args.add_argument("id", type=int, help="ID", required= True)
Pessoa_put_args.add_argument("nome", type=str, help="Nome", required= True)
Pessoa_put_args.add_argument("telefone", type=str, help="Telefone", required= True)
Pessoa_put_args.add_argument("CPF", type=str, help="CPF", required= True)
Pessoa_update_args = reqparse.RequestParser()
Pessoa_update_args.add_argument("id", type=int, help="ID")
Pessoa_update_args.add_argument("nome", type=str, help="Nome")
Pessoa_update_args.add_argument("telefone", type=str, help="Telefone")
Pessoa_update_args.add_argument("CPF", type=str, help="CPF")

Curso_put_args = reqparse.RequestParser()
Curso_put_args.add_argument("Id Matricula", type=str, help="Id matricula", required = True)
Curso_put_args.add_argument("nome", type=str, help="Nome", required = True)
Curso_update_args = reqparse.RequestParser()
Curso_update_args.add_argument("Id Matricula", type=str, help="Id matricula")
Curso_update_args.add_argument("nome", type=str, help="Nome")


resource_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'telefone': fields.String,
    'CPF': fields.String
    }

class Pessoa(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = PessoaModel.query.filter_by(id=id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, id):
        args = Pessoa_put_args.parse_args()
        id = PessoaModel(id=id, nome=args['nome'], telefone=args['telefone'], cpf=args['cpf'])
        db.session.add(id)
        db.session.commit()
        return Pessoa, 201

    @marshal_with(resource_fields)
    def patch(self,id):
        args = Pessoa_update_args.parse_args()
        result = PessoaModel.query.filter_by(id=id).first()
        if not result:
            abort(404, message="Pessoa não existe")

        if args['id']:
            result.name = args['id']
        if args['nome']:
            result.name = args['nome']
        if args['telefone']:
            result.name = args['telefone']
        if args['CPF']:
            result.name = args['CPF']

        db.session.commit()

        return result

    @marshal_with(resource_fields)
    def delete(self, id):
        del id[id]
        return'',204

    @marshal_with(resource_fields)
    def get(self, nome):
        result = PessoaModel.query.filter_by(nome=nome).first()
        return result

    @marshal_with(resource_fields)
    def put (self, nome):
        args = Pessoa_put_args.parse_args()
        nome = PessoaModel(id=args['id'], nome=nome, telefone=args['telefone'], CPF=args['CPF'])
        db.session.add(nome)
        db.session.commit()
        return Pessoa, 201

    @marshal_with(resource_fields)
    def delete(self, nome):
        del nome[nome]
        return'',204

    @marshal_with(resource_fields)
    def get(self,telefone):
        result = PessoaModel.get.filter_by(telefone=telefone).first()
        return result

    @marshal_with(resource_fields)
    def put (self,telefone):
        args = Pessoa_put_args.parse_args()
        telefone = PessoaModel(id=args['id'], nome=['nome'], telefone=telefone, CPF=args['CPF'])
        db.session.add(telefone)
        db.session.commit()
        return Pessoa, 201

    @marshal_with(resource_fields)
    def delete(self, telefone):
        del telefone[telefone]
        return'',204

    @marshal_with(resource_fields)
    def get(self,CPF):
        result = PessoaModel.get.filter_by(CPF=CPF).first()
        return result

    @marshal_with(resource_fields)
    def put(self,CPF):
        args = Pessoa_put_args.parse_args()
        CPF = PessoaModel(id=args['id'], nome=args['nome'], telefone=args['telefone'], CPF=CPF)
        db.session.add(CPF)
        db.session.commit()
        return Pessoa, 201

    @marshal_with(resource_fields)
    def delete(self, CPF):
        del CPF[CPF]
        return'',204
        
class Curso(Resource):
    @marshal_with(resource_fields)
    def get(self, id_matricula):
        result = CursoModel.query.filter_by(id_matricula=id_matricula).first()
        return result

    @marshal_with(resource_fields)
    def put(self,id_matricula):
        args = Curso_put_args.parse_args()
        id_matricula = CursoModel(id_matricula=id_matricula, nome=args['nome'])
        db.session.add(id_matricula)
        db.session.commit()
        return Curso, 201

    @marshal_with(resource_fields)
    def delete(self, id_matricula):
        del id_matricula[id_matricula]
        return'',204

    @marshal_with(resource_fields)
    def patch(self,id_matricula):
        args = Curso_update_args.parse_args()
        result = CursoModel.query.filter_by(id_matricula=id_matricula).first()
        if not result:
            abort(404, message="Curso não existe")

        if args['id_matricula']:
            result.name = args['id_matricula']
        if args['nome']:
            result.name = args['nome']

        db.session.commit()

        return result

    @marshal_with(resource_fields)
    def get(self, nome):
        result = CursoModel.query.filter_by(nome=nome).first()
        return result

    @marshal_with(resource_fields)
    def put(self,nome):
        args = Curso_put_args.parse_args()
        nome = CursoModel(id_matricula=args['id_matricula'], nome=nome)
        db.session.add(nome)
        db.session.commit()
        return Curso, 201

    @marshal_with(resource_fields)
    def delete(self, nome):
        del nome[nome]
        return'',204

api.add_resource(Pessoa, "/pessoa/<int:id>")
api.add_resource(Curso, "/curso/<int:id_matricula>")

if __name__ == "__main__":
    app.run(debug=True)
