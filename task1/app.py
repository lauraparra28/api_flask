from flask import Flask, request, jsonify

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

# READ A FILE
@app.route("/read_file",methods=["POST"])
def read_file():
    response = request.get_json()
    filename = response.get("filename")
   
    with open(filename,"r") as f:
        conteudo = f.readlines()
    
    return jsonify(conteudo)

# EDIT A FILE
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
   
app.run()