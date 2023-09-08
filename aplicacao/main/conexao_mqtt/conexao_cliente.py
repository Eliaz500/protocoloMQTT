import paho.mqtt.client as mqtt

class Conexao_Cliente:

    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive

    def inicia_conexao(self):
        cliente_mqtt = mqtt.Client(self.__client_name)
        cliente_mqtt.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        cliente_mqtt.loop_start()