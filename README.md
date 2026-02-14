# Giveaway — MVP

Projeto mínimo para gerenciar brindes — frontend simples (HTML/CSS) + backend em Django + SQLite (desenvolvimento).

Funcionalidades incluídas:
- Lista de brindes ativos
- Formulário de inscrição ("Já sou cadastrado" valida por telefone)
- Área administrativa (`/admin/`) para CRUD de brindes e visualização de inscrições

Como rodar (Windows / PowerShell):

1. Criar ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Instalar dependências

```powershell
pip install -r requirements.txt
```

3. Migrar banco e criar superuser

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Executar

```powershell
python manage.py runserver
```

A aplicação usa `SQLite` por padrão (arquivo `db.sqlite3` na raiz). Para trocar para MySQL depois, altere `DATABASES` em `giveaway_project/settings.py`.
