# Laboratório 09 — Engenharia de Software | APIs, Microsserviços e Deploy

**Universidade Presbiteriana Mackenzie**  
**Disciplina:** Engenharia de Software  
**Aluno:** Eduardo Ferreira de Mattos (TIA: 10402800)  
**Professor:** Prof. Dr. Rodrigo Juliani  

---

## 📌 Visão Geral do Laboratório

Este repositório contém a implementação completa das atividades do **Laboratório 09**:
* **9.1:** API Flask (Hello World, RESTful, execução local e Postman).
* **9.2:** API FastAPI (RESTful, execução com Uvicorn e Postman).
* **9.3:** Deploy de Aplicação Flask na Nuvem (Azure App Service + CI/CD).
* **9.4:** Deploy de API RESTful Flask na Nuvem (Azure App Service + CI/CD + Postman).
* **9.5:** Containerização da API FastAPI com Docker (Dockerfile, .dockerignore, build e run local).
* **9.6:** Deploy da API FastAPI na Nuvem (Azure App Service + CI/CD + Postman).

---

## 🚀 Entregas e Links Oficiais

### 9.1 — API Flask
* **9.1-a (Hello World):** [`9.1_Flask/a_hello_world.py`](9.1_Flask/a_hello_world.py)
* **9.1-b (API RESTful):** [`9.1_Flask/b_api_restful.py`](9.1_Flask/b_api_restful.py)
* **9.1-c (Execução):** Prints no PyCharm e navegador em `http://127.0.0.1:5000/livros`.
* **9.1-d (Postman):** [`Colecoes_Postman/Lab09_Flask.postman_collection.json`](Colecoes_Postman/Lab09_Flask.postman_collection.json)

### 9.2 — API FastAPI
* **9.2-a (API RESTful):** [`9.2_FastAPI/main.py`](9.2_FastAPI/main.py)
* **9.2-b (Uvicorn):** Prints no PyCharm e navegador em `http://127.0.0.1:8000/docs`.
* **9.2-c (Postman):** [`Colecoes_Postman/Lab09_FastAPI.postman_collection.json`](Colecoes_Postman/Lab09_FastAPI.postman_collection.json)

### 9.3 — Deploy Flask (Hello World na Nuvem)
* **Link do Repositório:** [https://github.com/EduardoFdeM/mackenzie-es-lab09-apis](https://github.com/EduardoFdeM/mackenzie-es-lab09-apis)
* **Aplicação Online (Azure App Service):** [https://lab09-flask-10402800-akepcrafhdakdhf3.brazilsouth-01.azurewebsites.net/](https://lab09-flask-10402800-akepcrafhdakdhf3.brazilsouth-01.azurewebsites.net/)
* **Pipeline de CI/CD:** [`.github/workflows/deploy-flask.yml`](.github/workflows/deploy-flask.yml)

### 9.4 — Deploy API Flask (RESTful na Nuvem)
* **Aplicação Online (Endpoint Livros):** [https://lab09-flask-10402800-akepcrafhdakdhf3.brazilsouth-01.azurewebsites.net/livros](https://lab09-flask-10402800-akepcrafhdakdhf3.brazilsouth-01.azurewebsites.net/livros)
* **Coleção do Postman:** [`Colecoes_Postman/Lab09_Flask.postman_collection.json`](Colecoes_Postman/Lab09_Flask.postman_collection.json)
* **Link do Código:** [`9.1_Flask/app.py`](9.1_Flask/app.py)

### 9.5 — FastAPI e Docker (Local)
* **Dockerfile:** [`9.2_FastAPI/Dockerfile`](9.2_FastAPI/Dockerfile)
* **.dockerignore:** [`9.2_FastAPI/.dockerignore`](9.2_FastAPI/.dockerignore)
* **Comandos de Execução Local:**
  ```bash
  cd 9.2_FastAPI
  docker build -t fast-api-livraria:latest .
  docker run -d -p 8000:8000 --name fast-api-container fast-api-livraria:latest
  ```

### 9.6 — FastAPI e Deploy na Nuvem
* **Link da Aplicação Online (FastAPI):** [https://lab09-fastapi-10402800-gchzh3gbdmf3b2cu.brazilsouth-01.azurewebsites.net/](https://lab09-fastapi-10402800-gchzh3gbdmf3b2cu.brazilsouth-01.azurewebsites.net/)
* **Documentação Interativa (Swagger):** [https://lab09-fastapi-10402800-gchzh3gbdmf3b2cu.brazilsouth-01.azurewebsites.net/docs](https://lab09-fastapi-10402800-gchzh3gbdmf3b2cu.brazilsouth-01.azurewebsites.net/docs)
* **Endpoint Livros:** [https://lab09-fastapi-10402800-gchzh3gbdmf3b2cu.brazilsouth-01.azurewebsites.net/livros](https://lab09-fastapi-10402800-gchzh3gbdmf3b2cu.brazilsouth-01.azurewebsites.net/livros)
* **Link do Repositório:** [https://github.com/EduardoFdeM/mackenzie-es-lab09-apis](https://github.com/EduardoFdeM/mackenzie-es-lab09-apis)
* **Coleção do Postman:** [`Colecoes_Postman/Lab09_FastAPI.postman_collection.json`](Colecoes_Postman/Lab09_FastAPI.postman_collection.json)
