from flask import request, jsonify
from models.driver import Driver

def create_driver():
    data = request.get_json()
    name = data.get("name")
    vehicle = data.get("vehicle")
    available = data.get("available", True)  # Define o valor padrão como True caso não seja especificado

    # Validação dos dados obrigatórios
    if not name or not vehicle:
        return jsonify({"error": "Name and vehicle are required"}), 400

    # Criação do objeto Driver
    driver = Driver(name=name, vehicle=vehicle, available=available)
    # Aqui você pode salvar o motorista no banco de dados, se necessário
    # driver.save()

    # Retorna a resposta com o motorista criado
    return jsonify({
        "message": "Driver created successfully",
        "driver": driver.to_dict()
    }), 201