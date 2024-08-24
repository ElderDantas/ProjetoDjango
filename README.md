# Projeto_Django_Fabrica
## Projeto em Django criado para a imersão na Fábrica de Software da Unipê

## Criando a Venv
```shell
py -m venv venv
```

## Ativando a Venv
```shell
.\venv\Scripts\activate
```

## Instalando o Django Rest Framework (Com a venv ativa)
```shell
pip install djangorestframework
```

## Criando arquivo requirements.txt
```shell
pip freeze > requirements.txt
```

## Criando a pasta do projeto
```shell
django-admin startproject projeto_fabrica
```

## Criando o app
```shell
py manage.py startapp absolute_cinema .
```

## Migração do banco de dados
```shell
py manage.py makemigrations
```
```shell
py manage.py migrate
```

## Criando um usuário administrador para o banco de dados Django
```shell
py manage.py createsuperuser
```

## Rodando o servidor
```shell
py manage.py runserver
```