from db_conection import creat_connection

def insert_passenger(nome, cpf):
    connection = creat_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO passageiros (nome, cpf) VALUES (%s,%s)",
        (nome,cpf)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("passsageiro inserido com sucesso!")

