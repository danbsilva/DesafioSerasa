FROM python:3.9.6

# Definindo a Pasta Raiz
WORKDIR /app

# Copiando aqruivos
COPY requirements.txt .
COPY settings.toml .
COPY main.py .

# venv
ENV VIRTUAL_ENV=/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# upgrade pip
RUN pip install --upgrade pip

# Instalação das Dependencias
RUN pip install -r requirements.txt

