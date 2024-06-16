# Use a imagem base do Python
FROM python:slim-bookworm
LABEL authors="ariel"

# Atualiza e instala dependências do sistema
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip python3-setuptools curl

# Instalação do Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Adiciona o diretório do Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo pyproject.toml e poetry.lock para o contêiner
COPY pyproject.toml ./

# Instala as dependências usando Poetry
RUN poetry install --no-root

# Copia o restante dos arquivos da aplicação
COPY . .

# Define o Python path
ENV PYTHONPATH=/app

# Comando para iniciar a aplicação
CMD ["python3", "app/__main__.py"]
