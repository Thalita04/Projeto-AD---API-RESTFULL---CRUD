from flask import Blueprint, request
from controllers.livro_controllers import (
    get_livros,
    get_livro_by_id,
    get_livro_by_titulo,
    create_livro,
    update_livro,
    delete_livro
)

livro_routes = Blueprint('livro_routes', __name__)

@livro_routes.route('/livros', methods=['GET'])
def livros_get():
    return get_livros()

@livro_routes.route('/livros/<int:livro_id>', methods=['GET'])
def livro_get_by_id(livro_id):
    return get_livro_by_id(livro_id)

@livro_routes.route('/livros/titulo/<string:titulo>', methods=['GET'])
def livro_get_by_titulo(titulo):
    return get_livro_by_titulo(titulo)

@livro_routes.route('/livros', methods=['POST'])
def livros_post():
    livro_data = request.json
    return create_livro(livro_data)

@livro_routes.route('/livros/<int:livro_id>', methods=['PUT'])
def livros_put(livro_id):
    livro_data = request.json
    return update_livro(livro_id, livro_data)

@livro_routes.route('/livros/<int:livro_id>', methods=['DELETE'])
def livros_delete(livro_id):
    return delete_livro(livro_id)