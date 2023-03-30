# *Tarefa 2: Criando uma API com Flask e a biblioteca Pandas*

Complemente o código com as seguintes requisições:

## Conteudo

[Importar Biblioteca]()

### Dataset: Devem haver pelo menos 20 linhas. as colunas a serem criadas: Name, Rating, Duration, Gender, Actor

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
    Data_films = pd.DataFrame(films)
    display(Data_films)
    Data_films.to_csv('films.csv')
```

## B. Criar um endpoint para editar um arquivo.csv enviando dados para adicionar

```python
{
    Data_films.loc[Data_films.shape[0], :] = ['Wednesday', 8.1, 45,'Jenna Ortega','Fantasy']
    Data_films.loc[Data_films.shape[0], :] = ['Transformer', 6.1, 110,'Robots','Adventure']
    Data_films.loc[Data_films.shape[0], :] = ['Finding to Dolly', 5.5, 121,'Nemo','Infantil']
    Data_films.loc[Data_films.shape[0], :] = ['Pirates of the Caribbean', 6.5, 151,'Capitan Sparrow','Adventure']

    Data_films.to_csv('films.csv')
} 
``` 

## C. Criar um endpoint para ler de n a m linhas de um arquivo .csv;


Utilizando o método loc, na qual é baseado nas labels da colunas e funciona assim: primeiro argumento são as linhas e o segundo as colunas a serem buscadas.

```python
{
    n = 2,  m = 6
    display(Data_films.loc[n:m])
} 
```
## D. Criar um endpoint para retornar valores filtrados da coluna 'Duration' com valores menores que 120 min;


Utilizando o método loc, na qual é baseado nas labels da colunas e funciona assim: primeiro argumento são as linhas e o segundo as colunas a serem buscadas.

```python
{
    filmes120 = Data_films.loc[Data_films['Duration'] <= 120]
    display (filmes120)
} 
```


## E. Criar um endpoint para retornar os valores ascendentemente do atributo 'Name'

O Método sort_values(), dá para mexer apenas se baseando nos valores dentro das colunas e linhas do dataframe 

```python
{
    Data_films.sort_values('Name', inplace=True)
    display(Data_films)
}

```

## F. Criar um endpoint para retornar todos os filmes de 'Sci-Fi'

Utilizando o método loc, na qual é baseado nas labels da colunas e funciona assim: primeiro argumento são as linhas e o segundo as colunas a serem buscadas.

```python
{
    films_sciFi = Data_films.loc[ Data_films['Genre'] == 'Sci-Fi' ,['Name', 'Rating', 'Actor'] ] 
    display( films_sciFi )
} 
```

## G. Criar um endpoint para retornar todos os filmes de 'Duration' no minimo 2 horas

Criei uma coluna adicional calculando em duração do filme em horas, a coluna -Duration- está em minutos. Utilizando o método loc, adicionei a condição de 2.1 horas

```python
{
    Data_films['Hours']= Data_films['Duration']/60
    filmes2 = Data_films.loc[Data_films['Hours'] <= 2.1]
    display (filmes2)
} 
```

## H. Criar um endpoint para retornar o promedio do rating dos filmes

O método df.describe() oferece estimativa de parâmetros estatísticos interesantes

```python
{
    Data_films.describe()
} 
```

## Para rodar o projeto

1. Execute o arquivo app.py para iniciar o servidor.
2. O arquivo app_client tem um exemplo de como interagir com a API.