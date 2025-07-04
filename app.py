from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
from transformers import pipeline

app = FastAPI()
db_file = "data.db"

class Item(BaseModel):
    nameUser: str
    text:str

class data_cadastro(BaseModel):
    username: str
    email:str
    password:str

class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.initialize_db()

    def initialize_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w") as f:
                json.dump([], f)

    def get_all_users(self):
        try:
            with open(self.db_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            with open(self.db_file, "w") as f:
                json.dump([], f)
            return []

    def add_user(self, user):
        users = self.get_all_users()
        if any(u["email"] == user["email"] for u in users):
            raise ValueError("Email já cadastrado")
        users.append(user)
        with open(self.db_file, "w") as f:
            json.dump(users, f)
    
    def checar_user(self, username):
        users = self.get_all_users()
        for user in users:
            if user["username"] == username:
                return True
        return False
    
    def alterar_username(self, email, senha, new_username):
        db = DataBase(db_file)
        users = db.get_all_users()
        for user in users:
            if user["email"] == email and user["password"] == senha:
                user["username"] = new_username
            elif user["email"] == email and user["password"] != senha:
                return {"message": "Senha incorreta"}
        with open(self.db_file, "w") as f:
            json.dump(users, f)


model = pipeline("sentiment-analysis")

@app.post("/verEmocao")
def verNívelEmoção(question: Item):
    db = DataBase(db_file)
    userExists = db.checar_user(question.nameUser)
    if userExists == False:
        return {"message": "Usuário não cadastrado"}
    response = model(question.text)
    return {
        "message": response[0]
    }

@app.post("/cadastrar")
def cadastrar_usuario(data_user: data_cadastro):
    db = DataBase(db_file)
    try:
        db.add_user(data_user.dict())
        return {"message": "Usuário cadastrado com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/VerUsers")
def verUsers():
    db = DataBase(db_file)
    users = db.get_all_users()
    return users

@app.put("/alterarUsername")
def alterarUsername(data_user: data_cadastro):
    db = DataBase(db_file)
    try:
        db.alterar_username(data_user.email, data_user.password, data_user.username)
        return {"message": "Username alterado com sucesso!"}
    except Exception as e:
        return {"error": str(e)}