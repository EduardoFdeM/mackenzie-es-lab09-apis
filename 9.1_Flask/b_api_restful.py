"""Exercícios 9.1(b, c, d) — API RESTful de livros com Flask.

Exemplo didático: dados em memória, sem persistência em banco de dados.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = {
    1: {"id": 1, "titulo": "Engenharia de Software", "autor": "Ian Sommerville", "ano": 2019},
    2: {"id": 2, "titulo": "Clean Code", "autor": "Robert C. Martin", "ano": 2008},
}
proximo_id = 3

@app.get("/")
def inicio():
    return jsonify({"mensagem": "API RESTful da Livraria (Flask)", "endpoint": "/livros"})

@app.get("/livros")
def listar_livros():
    return jsonify(list(livros.values())), 200

@app.get("/livros/<int:livro_id>")
def obter_livro(livro_id):
    livro = livros.get(livro_id)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify(livro), 200


def validar_livro(dados):
    if not isinstance(dados, dict):
        return "Envie um objeto JSON."
    if not isinstance(dados.get("titulo"), str) or not dados["titulo"].strip():
        return "O campo 'titulo' deve conter um texto não vazio."
    if not isinstance(dados.get("autor"), str) or not dados["autor"].strip():
        return "O campo 'autor' deve conter um texto não vazio."
    if not isinstance(dados.get("ano"), int) or isinstance(dados["ano"], bool):
        return "O campo 'ano' deve ser um número inteiro."
    return None


@app.post("/livros")
def criar_livro():
    global proximo_id
    dados = request.get_json(silent=True)
    erro = validar_livro(dados)
    if erro:
        return jsonify({"erro": erro}), 400
    novo = {"id": proximo_id, "titulo": dados["titulo"].strip(),
            "autor": dados["autor"].strip(), "ano": dados["ano"]}
    livros[proximo_id] = novo
    proximo_id += 1
    return jsonify(novo), 201


@app.put("/livros/<int:livro_id>")
def atualizar_livro(livro_id):
    if livro_id not in livros:
        return jsonify({"erro": "Livro não encontrado"}), 404
    dados = request.get_json(silent=True)
    erro = validar_livro(dados)
    if erro:
        return jsonify({"erro": erro}), 400
    livros[livro_id] = {"id": livro_id, "titulo": dados["titulo"].strip(),
                        "autor": dados["autor"].strip(), "ano": dados["ano"]}
    return jsonify(livros[livro_id]), 200


@app.delete("/livros/<int:livro_id>")
def remover_livro(livro_id):
    if livro_id not in livros:
        return jsonify({"erro": "Livro não encontrado"}), 404
    del livros[livro_id]
    return jsonify({"mensagem": "Livro removido com sucesso"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
