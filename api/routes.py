from flask import Blueprint
from .controllers.driver_controller import creat_driver
from .controllers.passenger_controller import creat_passenger
from .controllers.ride_controller import creat_ride

# Blueprint da API 
api_bp = Blueprint('api',__name__)

# Rotas de criação de entidades 
api_bp.route('/drivers', methods=['POST'])(creat_driver)
api_bp.route('/passengers',methods=['POST'])(creat_passenger)
api_bp.route('/ride',methods=['POST'])(creat_ride)