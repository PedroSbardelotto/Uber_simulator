# from fastapi import FastAPI
# from factories.driver_factory import DrivenFactory

# app = FastAPI()
# driver_factory = DrivenFactory()
# motoristas = []

# @app.post("/motoristas/")
# def criar_motorista(nome: str, veiculo: str):
#     motorista = driver_factory.criar_motorista(nome,veiculo)
#     motoristas.apend(motorista)
#     return {"message":"Motorista criado com sucesso"}

# @app.get("/motoristas/")
# def listar_motoristas():
#     return motoristas