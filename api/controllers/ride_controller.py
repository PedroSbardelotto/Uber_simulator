from flask import request, jsonify
from models.ride import Ride
from models.driver import Driver
from models.passenger import Passenger

def create_ride():
    data = request.get_json()
    driver_id = data.get("driver_id")
    passenger_id = data.get("passenger_id")
    distance = data.get("distance")  # agora usamos "distancia" em vez de "destination"
    
    if not driver_id or not passenger_id or not distance:
        return jsonify({"error": "Driver, passenger, and distance are required"}), 400
    
    # Verifica se o motorista e o passageiro existem
    driver = Driver.get_by_id(driver_id)  # Aqui você buscaria o motorista no banco de dados
    passenger = Passenger.get_by_id(passenger_id)  # Aqui você buscaria o passageiro no banco de dados
    
    if not driver or not passenger:
        return jsonify({"error": "Driver or Passenger not found"}), 404
    
    # Criação do objeto Corrida
    ride = Ride(id_corrida=123, driver=driver, passenger=passenger, distance=distance)  # Exemplo de id_corrida
    # Salvar corrida no banco de dados (caso necessário)
    # corrida.save()

    return jsonify({
        "message": "Ride created successfully",
        "ride": {
            "id_ride": ride.id_ride,
            "driver": ride.driver.name,
            "passenger": ride.passenger.name,
            "distance": ride.distance,
            "status": ride.status,
            "price": ride.price
        }
    }), 201

def start_ride(ride_id):
    # Aqui você buscaria a corrida pelo ID
    ride = ride.get_by_id(ride_id)  # Exemplo, adapte conforme a persistência real
    
    if not ride:
        return jsonify({"error": "Ride not found"}), 404
    
    try:
        ride.start_ride()  # Tenta iniciar a corrida
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify({
        "message": "Ride started successfully",
        "ride": {
            "id_ride": ride.id_ride,
            "status": ride.status,
            "driver": ride.driver.name,
            "passenger": ride.passenger.name
        }
    })

def finish_ride(ride):
    # Aqui você buscaria a corrida pelo ID
    ride = ride.get_by_id(ride)  
    
    if not ride:
        return jsonify({"error": "Ride not found"}), 404
    
    try:
        ride.finish_ride()  # Tenta finalizar a corrida
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify({
        "message": "Ride finished successfully",
        "ride": {
            "id_ride": ride.id_corrida,
            "status": ride.status,
            "price": ride.price,
            "driver": ride.driver.name,
            "passenger": ride.passenger.name
        }
    })