"""Exercícios 9.2(a, b, c) — API RESTful de livros com FastAPI.

Exemplo didático: dados em memória, sem persistência em banco de dados.
"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="API da Livraria — FastAPI", version="1.0.0")

class LivroEntrada(BaseModel):
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    ano: int

class Livro(LivroEntrada):
    id: int

livros: dict[int, Livro] = {
    1: Livro(id=1, titulo="Engenharia de Software", autor="Ian Sommerville", ano=2019),
    2: Livro(id=2, titulo="Clean Code", autor="Robert C. Martin", ano=2008),
}
proximo_id = 3

@app.get("/")
def inicio():
    return {"mensagem": "API RESTful da Livraria (FastAPI)", "documentacao": "/docs"}

@app.get("/livros", response_model=list[Livro])
def listar_livros():
    return list(livros.values())

@app.get("/livros/{livro_id}", response_model=Livro)
def obter_livro(livro_id: int):
    if livro_id not in livros:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livros[livro_id]

@app.post("/livros", response_model=Livro, status_code=status.HTTP_201_CREATED)
def criar_livro(dados: LivroEntrada):
    global proximo_id
    novo = Livro(id=proximo_id, **dados.model_dump())
    livros[proximo_id] = novo
    proximo_id += 1
    return novo

@app.put("/livros/{livro_id}", response_model=Livro)
def atualizar_livro(livro_id: int, dados: LivroEntrada):
    if livro_id not in livros:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    atualizado = Livro(id=livro_id, **dados.model_dump())
    livros[livro_id] = atualizado
    return atualizado

@app.delete("/livros/{livro_id}")
def remover_livro(livro_id: int):
    if livro_id not in livros:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    del livros[livro_id]
    return {"mensagem": "Livro removido com sucesso"}
