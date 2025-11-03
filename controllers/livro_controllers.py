from models.livro_models import Livro
from db import db
import json
from flask import make_response, request

# GET - todos os livros (com filtro opcional por gênero)
def get_livros():
    genero = request.args.get('genero')
    if genero:
        livros = Livro.query.filter_by(genero=genero).all()
    else:
        livros = Livro.query.all()

    response = make_response(
        json.dumps({
            'mensagem': 'Lista de livros.',
            'dados': [livro.json() for livro in livros]
        }, ensure_ascii=False),
        200
    )
    response.headers['Content-Type'] = 'application/json'
    return response

# GET - livro por ID
def get_livro_by_id(livro_id):
    livro = Livro.query.get(livro_id)

    if livro:
        response = make_response(
            json.dumps({'mensagem': 'Livro encontrado.', 'dados': livro.json()}, ensure_ascii=False),
            200
        )
    else:
        response = make_response(
            json.dumps({'mensagem': 'Livro não encontrado.', 'dados': {}}, ensure_ascii=False),
            404
        )
    response.headers['Content-Type'] = 'application/json'
    return response

# GET - livro por título
def get_livro_by_titulo(titulo):
    livro = Livro.query.filter_by(titulo=titulo).first()

    if livro:
        response = make_response(
            json.dumps({'mensagem': 'Livro encontrado.', 'dados': livro.json()}, ensure_ascii=False),
            200
        )
    else:
        response = make_response(
            json.dumps({'mensagem': 'Livro não encontrado.', 'dados': {}}, ensure_ascii=False),
            404
        )
    response.headers['Content-Type'] = 'application/json'
    return response

# POST - criar livro
def create_livro(livro_data):
    if not all(key in livro_data for key in ['titulo', 'autor', 'genero', 'ano_publicacao']):
        response = make_response(
            json.dumps({'mensagem': 'Campos obrigatórios: título, autor, gênero e ano de publicação.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    novo_livro = Livro(
        titulo=livro_data['titulo'],
        autor=livro_data['autor'],
        genero=livro_data['genero'],
        ano_publicacao=livro_data['ano_publicacao']
    )

    db.session.add(novo_livro)
    db.session.commit()

    response = make_response(
        json.dumps({'mensagem': 'Livro cadastrado com sucesso.', 'dados': novo_livro.json()}, ensure_ascii=False),
        201
    )
    response.headers['Content-Type'] = 'application/json'
    return response

# PUT - atualizar livro
def update_livro(livro_id, livro_data):
    livro = Livro.query.get(livro_id)

    if not livro:
        response = make_response(
            json.dumps({'mensagem': 'Livro não encontrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    livro.titulo = livro_data.get('titulo', livro.titulo)
    livro.autor = livro_data.get('autor', livro.autor)
    livro.genero = livro_data.get('genero', livro.genero)
    livro.ano_publicacao = livro_data.get('ano_publicacao', livro.ano_publicacao)

    db.session.commit()

    response = make_response(
        json.dumps({'mensagem': 'Livro atualizado com sucesso.', 'dados': livro.json()}, ensure_ascii=False),
        200
    )
    response.headers['Content-Type'] = 'application/json'
    return response

# DELETE - excluir livro
def delete_livro(livro_id):
    livro = Livro.query.get(livro_id)
    if not livro:
        response = make_response(
            json.dumps({'mensagem': 'Livro não encontrado.'}, ensure_ascii=False),
            404
        )
    else:
        db.session.delete(livro)
        db.session.commit()
        response = make_response(
            json.dumps({'mensagem': 'Livro excluído com sucesso.'}, ensure_ascii=False),
            200
        )

    response.headers['Content-Type'] = 'application/json'
    return response