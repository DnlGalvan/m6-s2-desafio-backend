# `CNAB Simualtor`

<p>Aplicação com o untuito de:<br>
- 1º: Receber arquivos de extenção *.txt através de um formulario, com informações financeiras no estilo (CNAB)<br>
- 2º: Normalizar os dados e salvar corretamente a informação em um banco de dados relacional.<br>
- 3º: Exibir uma lista das operações importadas por lojas, sendo que essa lista deve conter um totalizador do saldo em conta por loja.</p>
<hr>
<br>

## `Tecnologias utilizadas no projeto`

<br>
<div id="tecs"style='display:flex; gap: 5px;'><br>
   <img align="center" alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white">

   <img align="center" alt="css" src="https://img.shields.io/badge/DJANGO-092E20?style=plastic&logo=django&logoColor=white">

   <img align="center" alt="react" src="https://img.shields.io/badge/RestFramework-red?style=plastic&logo=rest_framework">

</div></br>
<hr>
<br>

## `Instruções para rodar o projeto localmente`

<br>

### Crie o ambiente virtual local com o comando:

```
python -m venv venv
```

### Inicie o ambiente virtual

<br>

#### Windows:

```
.\venv\Scripts\activate
```

#### Linux:

```
source venv/bin/activate
```

<br>

### Instalar as dependências necessárias:

```
pip install -r requirements.txt
```

<br>

### Execute as migrações para criação das tabelas SQLite3

```
python manage.py migrate
```

<br>

### Inicie o servidor

```
python manage.py runserver
```

<br>
<hr>
<br>

## `Instruções para rodar o porjeto com DOCKER`

```
docker compose up
```

<br>
<hr>
<br>

## `Para acessar o endpoint`

```
localhost:8000/api/cnab/
```

<br>
<hr>
