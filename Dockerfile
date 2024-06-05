# Use a imagem oficial do Python
FROM python:3.12-slim-buster
LABEL authors="ariel"

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Instale o Poetry
RUN pip install poetry

# Copie o arquivo pyproject.toml para o diretório de trabalho
COPY pyproject.toml ./

# Instale as dependências
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copie o restante do seu código para o diretório de trabalho
COPY . .

# Comando para executar o aplicativo
CMD ["python", "./main.py"]