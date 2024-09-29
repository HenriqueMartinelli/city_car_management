# Utilizar uma imagem Python como base
FROM python:3.12-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo pyproject.toml e poetry.lock para o container
COPY pyproject.toml poetry.lock /app/

# Instalar o Poetry
RUN pip install poetry

# Instalar as dependências do projeto
RUN poetry install --no-root

# Copiar o restante do código da aplicação
COPY . /app

# Definir a variável de ambiente para que o Flask funcione corretamente
ENV FLASK_APP=app:create_app
ENV FLASK_RUN_HOST=0.0.0.0

# Expor a porta 5000
EXPOSE 5000

COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Comando para rodar migrações e depois iniciar o servidor Flask
CMD ["sh", "-c", "poetry run flask db upgrade && poetry run flask run"]
