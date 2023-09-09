import paho.mqtt.client as mqtt
from .interrupcao_callback import on_connect, on_subscribe, on_message

class Conexao_Cliente:

    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive

    def inicia_conexao(self):
        cliente_mqtt = mqtt.Client(self.__client_name)

        # Callbacks
        cliente_mqtt.on_connect = on_connect
        cliente_mqtt.on_subscribe = on_subscribe
        cliente_mqtt.on_message = on_message


        cliente_mqtt.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        cliente_mqtt.loop_start()