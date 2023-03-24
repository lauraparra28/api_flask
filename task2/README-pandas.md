# *Criando uma API com Flask e a biblioteca Pandas*

Complemente o código com as seguintes requisições:

## Dataset

Devem haver pelo menos 20 linhas. as colunas a serem criadas: Name, Rating, Duration, Gender, Actor

## A. Importar a biblioteca pandas

Criei um dataframe a partir de um dicionário

```python
import pandas as pd
films = {'Name' : ['Inception'],
         'Rating': [8.8],
         'Duration': [148],
         'Actor' : ['Leonardo DiCaprio'],
         'Genre' : ['Sci-Fi']
          }
df = pd.df(films)
```

## B. Criar um endpoint para editar um arquivo.csv enviando dados para adicionar

```python
{
    import pandas as pd
    df = pd.read_csv("my_favorite_films.csv")
} 
``` 

## C. Criar um endpoint para ler de n a m linhas de um arquivo .csv;


Utilizando o método loc, na qual é baseado nas labels da colunas e funciona assim: primeiro argumento são as linhas e o segundo as colunas a serem buscadas.

```python
{
    n = 2
    m = 6
    display(Data_films.loc[n:m])
} 
```

## Para rodar o projeto

1. Execute o arquivo app.py para iniciar o servidor.
2. O arquivo app_client tem um exemplo de como interagir com a API.