from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

list_files = []

@app.route("/")
def home():
    return "Bem-vindo ao ICA"

# CREATE A FILE 
@app.route("/create_file",methods=["POST"])
def create_file():
    response = request.get_json()
    filename = response.get("filename")
    list_files.append(response)
    
    with open(filename,"w") as f:
        f.write(f"O arquivo criado foi {filename}")
    
    return jsonify(list_files)

# READ A FILE .txt
@app.route("/read_file",methods=["POST"])
def read_file():
    response = request.get_json()
    filename = response.get("filename")
   
    with open(filename,"r") as f:
        conteudo = f.readlines()
    
    return jsonify(conteudo)

# EDIT A FILE .txt
@app.route("/edit_file",methods=["POST"])
def edit_file():
    response = request.get_json()
    filename = response.get("filename")
    data = response.get("data")
    
    with open(filename,"a") as f:
        f.write(f" {data}")
    
    with open(filename, "r") as f:
        conteudo = f.readlines()
        
    return jsonify(
        mensagem = "Arquivo editado",
        data = conteudo
    )

# CREATE A .csv
@app.route("/create_csv",methods=["POST"])
def create_csv():
    response = request.get_json()
    filename = response.get("filename")
    list_files.append(response)
    
    with open(filename,"w") as f:
        films = {'Name' : ['Inception', 'In time', 'The Intouchables', 'Source Code', 'Avatar', 'Pinochhio', 'Megan', 'Everything everywhere all at once ', 'Jumanji 2', 'The Whale', 'Harry Potter', 'Captain America', 'The Avengers', 'Under the Skin', 'Sing 2', 'Nemo'],
                 'Rating': [8.8, 6.7, 8.5, 7.5, 7.8, 5.5, 6.4, 7.9, 7.4, 7.8, 7.6, 7.8, 8, 6.3, 7.4, 6.5],
                 'Duration': [ 148, 109, 112, 93, 213, 124, 102, 139 , 123, 117, 152, 147, 143, 108, 110, 111],
                 'Actor' : ['Leonardo DiCaprio', 'Justin Timberlake', 'Omar Sy', 'Jake Gyllenhaal', 'Zoe Saldana', 'Disney', 'Jenna Davis', 'Michelle Yeoh', 'Dwayne Johnson', 'Darren Aronofsky', 'Daniel Radcliffe', 'Chris Evans', 'Chris Evans', 'Scarlett Johansson', 'Scarlett Johansson', 'Dolly' ] ,
                 'Genre' : ['Sci-Fi', 'Sci-Fi', 'Comedy','Sci-Fi', 'Adventure', 'Fantasy', 'Thriller', 'Sci-Fi', 'Adventure', 'Drama', 'Fantasy', 'Adventure', 'Adventure', 'Drama', 'Infantil', 'Infantil']
                 
          }
        Data_films = pd.DataFrame(films)
        Data_films.to_csv('films.csv')

    return jsonify(list_files)

# EDIT A .create_csv

@app.route("/edit_csv",methods=["POST"])
def edit_csv():
    response = request.get_json()
    filename = response.get("filename")
    data = response.get("data")
    
    with open(filename,"a") as f:
        f.write(f" {data}")
    
    with open(filename, "r") as f:
        conteudo = f.readlines()
        
    return jsonify(
        mensagem = "Arquivo editado",
        data = conteudo
    )
    
    Data_films.loc[Data_films.shape[0], :] = ['Toy Story', 7.9, 92,'Woody', 'Sci-Fi']
    Data_films.loc[Data_films.shape[0], :] = ['Wednesday', 8.1, 45,'Jenna Ortega','Fantasy']
    Data_films.loc[Data_films.shape[0], :] = ['Transformer', 6.1, 110,'Robots','Adventure']
    Data_films.loc[Data_films.shape[0], :] = ['Finding to Dolly', 5.5, 121,'Nemo','Infantil']
    Data_films.loc[Data_films.shape[0], :] = ['Pirates of the Caribbean', 6.5, 151,'Capitan Sparrow','Adventure']

app.run()