# *Criando uma Api com Flask e Python*


## 1. Criar um endpoint para criar um arquivo.txt

Utilizando POST enviamos para http://127.0.0.1:5000/create_file

{ 
    "filename": "prueba1.txt"
}


## 2. Criar um endpoint para ler arquivo.txt

Utilizando POST enviamos para http://127.0.0.1:5000/read_file

Response:

[
    "O arquivo criado foi prueba1.txt"
]

## 3. Criar um endpoint para editar arquivo.txt já existente



