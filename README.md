# Laboratório 09 — Engenharia de Software | Entregas 9.1 e 9.2

**Prazo mostrado no Moodle:** 08/11/2026 às 23h59.

Este pacote cobre exclusivamente **9.1(a, b, c, d) e 9.2(a, b, c)**. Os exemplos usam uma livraria como domínio didático. É possível apresentar os exercícios da livraria porque o enunciado não exige um domínio de negócio específico.

## Pré-requisitos
- Python 3.10+ (3.11 ou 3.12 recomendado)
- PyCharm ou IDE equivalente
- GitHub (para links públicos dos códigos)
- Postman (para compartilhar coleções)

## 9.1(a) — Hello World Flask
1. Abra a pasta `9.1_Flask` no PyCharm.
2. Abra o Terminal da IDE e execute `python -m pip install -r requirements.txt`.
3. Execute `python a_hello_world.py`.
4. Acesse `http://127.0.0.1:5000/` no navegador. Deve aparecer `Hello World! API Flask funcionando.`.
5. Publique o código no GitHub e entregue o **link do arquivo `a_hello_world.py`**.

**Importante:** pare o servidor com `Ctrl+C` antes de iniciar o projeto da etapa (b) porque ambos usam a porta 5000.

## 9.1(b) — API RESTful Flask
1. Execute `python b_api_restful.py`.
2. Acesse `http://127.0.0.1:5000/livros` e confirme que aparece uma lista JSON de livros.
3. Entregue no Moodle o **link do arquivo `b_api_restful.py`** no GitHub.

## 9.1(c) — Executar API e navegador
1. Com `b_api_restful.py` executando, tire **um print do PyCharm** mostrando o código e o terminal com o servidor ativo.
2. Tire **um print do navegador** em `http://127.0.0.1:5000/livros` exibindo o JSON.
3. Envie esses prints à tarefa **9.1 API Flask - c** no Moodle. Opcionalmente, reúna os dois prints em um PDF, caso a tarefa aceite.

## 9.1(d) — Postman Flask
1. No Postman, escolha **Import > Files** e selecione `Colecoes_Postman/Lab09_Flask.postman_collection.json`.
2. Com Flask em execução, abra a coleção e rode as requisições na ordem 01 a 05.
3. Confirme o código de status HTTP correto na resposta. O POST deve retornar 201.
4. Compartilhe a coleção com **link acessível ao professor** via opções de compartilhamento do Postman. **Importar o JSON no Postman não cria automaticamente link público!**
5. Entregue o link compartilhável na tarefa **9.1 API Flask - d**.

## 9.2(a) — API RESTful FastAPI
1. Pare o Flask, se desejar (não é obrigatório, pois usa outra porta).
2. Abra a pasta `9.2_FastAPI` no PyCharm, preferencialmente com ambiente virtual.
3. Instale as dependências: `python -m pip install -r requirements.txt`.
4. Publique o arquivo `main.py` no GitHub e entregue o **link desse código** na tarefa **9.2 API FastAPI - a**.

## 9.2(b) — Uvicorn e navegador
1. No terminal da pasta `9.2_FastAPI`, execute: `python -m uvicorn main:app --reload --port 8000`.
2. Acesse `http://127.0.0.1:8000/livros` e, opcionalmente, `http://127.0.0.1:8000/docs`.
3. Tire **um print do PyCharm com Uvicorn rodando** e **um print do navegador mostrando a API**.
4. Entregue os prints na tarefa **9.2 API FastAPI - b**.

## 9.2(c) — Postman FastAPI
1. No Postman, importe `Colecoes_Postman/Lab09_FastAPI.postman_collection.json`.
2. Com FastAPI em execução, execute as cinco requisições, em ordem.
3. Compartilhe a coleção no Postman usando um link que o professor consiga acessar.
4. Entregue esse link na tarefa **9.2 API FastAPI - c**.

## Publicar o código no GitHub rapidamente
1. Crie **um único repositório** chamado `mackenzie-lab09-apis`, público se isso for permitido pela disciplina.
2. No GitHub, escolha **Add file > Upload files** e envie as pastas `9.1_Flask`, `9.2_FastAPI` e `Colecoes_Postman`, e este README.
3. Confirme com **Commit changes**.
4. Para cada tarefa com "link para o código", abra o arquivo exato no GitHub e copie a URL do navegador. Podem ser links diferentes para arquivos dentro do mesmo repositório.
5. Caso o GitHub mostre apenas o repositório, o professor poderá navegar entre as pastas.

## Endpoints de ambas as APIs
| Método | Endpoint | Função | HTTP esperado |
|---|---|---|---|
| GET | `/` | status/boas-vindas | 200 |
| GET | `/livros` | listar todos | 200 |
| GET | `/livros/1` | consultar livro | 200 |
| POST | `/livros` | criar livro | 201 |
| PUT | `/livros/1` | atualizar livro | 200 |
| DELETE | `/livros/2` | excluir livro | 200 |

**Body do POST/PUT (Postman):**
```json
{
  "titulo": "Padrões de Projeto",
  "autor": "Erich Gamma et al.",
  "ano": 1994
}
```

Os dados são mantidos apenas na memória: ao reiniciar a API, os exemplos de livros reaparecem. Isso é suficiente para o propósito demonstrativo do laboratório, mas não é adequado como sistema de produção.

## Checklist para o Moodle
- [ ] 9.1-a: URL do código Flask Hello World
- [ ] 9.1-b: URL do código Flask RESTful
- [ ] 9.1-c: print(s) PyCharm + navegador Flask
- [ ] 9.1-d: URL compartilhável da coleção Postman Flask
- [ ] 9.2-a: URL do código FastAPI
- [ ] 9.2-b: print(s) PyCharm + navegador FastAPI
- [ ] 9.2-c: URL compartilhável da coleção Postman FastAPI

> Os arquivos do pacote são o código-fonte e as coleções para executar os exercícios. **A publicação no GitHub, os testes no Postman, as capturas de tela e o envio no Moodle precisam ser realizados pelo aluno**, pois devem refletir sua execução e suas contas.
