# *Criando uma Api com Flask e Python*

Utilizei o Postman (API Client) que facilita criar, compartilhar, testar e documentar APIs.

## 1. Criar um endpoint para criar um arquivo.txt

Utilizando POST enviamos para http://127.0.0.1:5000/create_file

```json 
{ 
    "filename": "prueba1.txt"
}
```

## 2. Criar um endpoint para ler arquivo.txt

Utilizando POST enviamos para http://127.0.0.1:5000/read_file

Response:
```json
{
    "O arquivo criado foi prueba1.txt"
} 
``` 

## 3. Criar um endpoint para editar arquivo.txt já existente

Utilizando POST enviamos para http://127.0.0.1:5000/edit_file

```json
{
    "mensagem": "Arquivo editado",
    "data": [
        "O arquivo criado foi prueba1.txt 1989 \n",
        " D 1989"
    ]
} 
```
## Descrição do projeto
Cliente faz uma solicitação para editar um .txt que já existe. O server faz a edição e responde ao client com a alteração feita.

- Bibliotecas necessárias para esta tarefa: Flask, Requests, json.
- Pesquise como enviar um texto via requisição HTTP (post, put, get, delete).
- Utilize nomes de variáveis autoexplicativas.

## Para rodar o projeto

1. Execute o arquivo app.py para iniciar o servidor.
2. O arquivo app_client tem um exemplo de como interagir com a API.