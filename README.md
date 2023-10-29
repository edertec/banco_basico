## Sistema de Gerenciamento de Tarefas com Flask e SQLite

📌 Visão Geral do Projeto
Este projeto visa fornecer uma aplicação para gerenciamento de tarefas utilizando Python, Flask e SQLite. O projeto abrange duas interfaces principais:

Cadastro de Tarefas: Permite ao usuário cadastrar novas tarefas.
Consulta de Tarefas: Exibe uma lista de todas as tarefas cadastradas.

⚙️ Funcionalidades
Criação de Tarefas: Suporte aos seguintes campos:
- ID
- Tarefa
- Data
- Responsável
- Observações
- Status

Consulta de Tarefas: Exibe todas as tarefas cadastradas em uma tabela.

🔧 Pré-requisitos
Python 3.x
Flask
SQLite

# Estrutura
/projeto
|-- /templates
|   |-- index.html
|   |-- tasks.html
|-- app.py
|-- database.db  (gerado após a primeira execução)
|-- README.md

app.py: Lógica do back-end e rotas da aplicação.
index.html: Template HTML para a tela de consulta.
tasks.html: Template HTML para a tela de cadastro.
database.db: Arquivo SQLite para armazenamento das tarefas.

# ambiente virtual
- python3 -m venv myenv
- source myenv/bin/activate  # No Windows, use `myenv\Scripts\activate`

- pip install Flask


# Como Utilizar
Rodar: python app.py

Consulta de Tarefas
Acesse http://127.0.0.1:5000/ para visualizar todas as tarefas cadastradas.

Cadastro de Novas Tarefas
Clique no link "Cadastrar Nova Tarefa" na tela de consulta para ser direcionado à tela de cadastro.

Licença
Criado para uso acadêmico no CETEC - 2023






