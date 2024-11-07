from flask import request, jsonify
from models.passenger import Passenger

class PassengerProxy:
    def __init__(self, passenger_service):
        self.passenger_service = passenger_service

    def create(self, name, destination, departure_location):
        # Aqui podemos adicionar alguma lógica extra, como validações, log, etc.
        print(f"Proxy: Criando passageiro com o nome {name}, destino {destination}, e local de partida {departure_location}")
        
        # Chama o serviço real para criar o passageiro
        return self.passenger_service.create(name, destination, departure_location)

class PassengerService:
    def create(self, name, destination, departure_location):
        # Criação do objeto Passenger
        passenger = Passenger(name=name, destination=destination, departure_location=departure_location)
        return passenger

# Função do controlador que usa o Proxy
def create_passenger():
    data = request.get_json()
    name = data.get("name")
    destination = data.get("destination")
    departure_location = data.get("departure_location")
    
    if not name or not destination or not departure_location:
        return jsonify({"error": "Name, destination, and departure location are required"}), 400
    
    # Criando o serviço real e o proxy
    passenger_service = PassengerService()
    proxy = PassengerProxy(passenger_service)
    
    # Usando o Proxy para criar o passageiro
    passenger = proxy.create(name, destination, departure_location)
    
    return jsonify({"message": "Passenger created successfully", "passenger": passenger.to_dict()}), 201


