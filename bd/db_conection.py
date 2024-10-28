import psycopg2
from psycopg2 import sql


def creat_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",  # Endereço do servidor
            datebase="uber_simulator_data_base",  # Nome do banco de dados
            user="seu_usuario",  # Usuário do PostgreSQL
            password="sue_senha"  # Senha do usuário
        )
        print("Conexão bem-sucedia!")
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None