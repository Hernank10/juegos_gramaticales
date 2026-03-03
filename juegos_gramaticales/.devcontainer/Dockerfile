FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    postgresql-client \
    sqlite3 \
    nodejs \
    npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install poetry virtualenv

WORKDIR /workspace

RUN echo "export PS1='🐍 \[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ~/.bashrc
RUN echo "alias run='python run.py'" >> ~/.bashrc
RUN echo "alias db-init='python -c \"from app import app, db; app.app_context().push(); db.create_all()\"'" >> ~/.bashrc

EXPOSE 5000
