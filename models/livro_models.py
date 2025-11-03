from db import db

class Livro(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(80), nullable=False)
    ano_publicacao = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'ano_publicacao': self.ano_publicacao
        }