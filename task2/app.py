from flask import Flask, request, jsonify
import pandas as pd
from data import films, new_films

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
        
        Data_films = pd.DataFrame(films)
        Data_films.to_csv('films.csv')

    return jsonify(list_files)

# EDIT A .create_csv

@app.route("/edit_csv",methods=["POST"])
def edit_csv():
    response = request.get_json()
    filename = response.get("filename")
    message = response.get("message")
    mode = response.get("mode")
    
        
    return jsonify(
        mensagem = "Arquivo editado",
        data = conteudo
    )
    

app.run()