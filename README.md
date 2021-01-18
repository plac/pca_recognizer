# Reconhecimento facial com PCA

## Objetivo

Modelo de reconhecimento facial utilizando análise de componentes principais (PCA) e opencv.

Imagens (410) para treino e teste disponíveis em `./ORL2`, utilizando 70% para treinos e 30% para testes.

## Setup e execução

Baixar projeto:
> git clone https://github.com/plac/pca_recognizer.git

Dentro da pasta do projeto, criar virtual environment para python:
> virtualenv .venv

Ativar o virtual env:
> source .venv/bin/activate

Instalar dependências:
> pip install -r requirements.txt

Rodar aplicação com paramêtros _default_:
> python main.py

Desativar virtualenv:
> deactivate

## Resumo de resultados

```
...
10 componentes principais, acurácia: 95.93%
11 componentes principais, acurácia: 95.12%
12 componentes principais, acurácia: 96.75%
13 componentes principais, acurácia: 96.75%
14 componentes principais, acurácia: 96.75%
15 componentes principais, acurácia: 95.93%
16 componentes principais, acurácia: 95.12%
17 componentes principais, acurácia: 95.12%
18 componentes principais, acurácia: 95.12%
19 componentes principais, acurácia: 95.12%
20 componentes principais, acurácia: 95.93%
...
```



