# ✅ TaskFlow — Gerenciador de Tarefas

> Aplicação web completa para gerenciamento de tarefas pessoais com autenticação de usuários, desenvolvida com Flask e SQLite.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)

---

## 📋 Funcionalidades

- 🔐 Cadastro e login de usuários com senha criptografada
- ➕ Criar, editar e excluir tarefas
- ✅ Marcar tarefas como concluídas
- 🎯 Definir prioridade (Alta, Média, Baixa)
- 🔍 Filtrar tarefas por status e prioridade
- 📊 Painel com contagem de tarefas (total, pendentes, concluídas)
- 🔒 Cada usuário acessa apenas as próprias tarefas

---

## 🛠️ Tecnologias

| Camada      | Tecnologia                          |
|-------------|-------------------------------------|
| Backend     | Python 3.10+, Flask 3.0             |
| Banco de dados | SQLite + SQLAlchemy              |
| Autenticação | Flask-Login + Werkzeug (hash bcrypt) |
| Frontend    | Jinja2, Bootstrap 5, Bootstrap Icons |

---

## 🚀 Como rodar localmente

### Pré-requisitos
- Python 3.10 ou superior instalado
- Git

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/taskflow.git
cd taskflow

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python run.py
```

Acesse **http://localhost:5000** no navegador.

> O banco de dados SQLite é criado automaticamente na primeira execução.

---

## 📁 Estrutura do Projeto

```
taskflow/
├── app/
│   ├── __init__.py       # Factory da aplicação Flask
│   ├── models.py         # Models: User e Task (SQLAlchemy)
│   ├── routes.py         # Rotas e lógica de negócio
│   └── templates/
│       ├── base.html     # Layout base
│       ├── login.html    # Página de login
│       ├── register.html # Página de cadastro
│       ├── tasks.html    # Dashboard de tarefas
│       └── edit_task.html # Edição de tarefa
├── run.py                # Ponto de entrada
├── requirements.txt      # Dependências
├── .gitignore
└── README.md
```

---

## 🔮 Melhorias futuras

- [ ] Definir prazo (deadline) para cada tarefa
- [ ] Organização por categorias/tags
- [ ] Notificações por e-mail de tarefas próximas do vencimento
- [ ] API REST com endpoints JSON
- [ ] Deploy na nuvem (Render, Railway ou Heroku)
- [ ] Testes automatizados com pytest

---

## 👨‍💻 Autor

Feito por **José** — estudante de Análise e Desenvolvimento de Sistemas na Faculdade Ficr PE.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ferreiracostadev)


---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
