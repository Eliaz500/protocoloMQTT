import paho.mqtt.client as mqtt


class Conexao_Cliente:
    def __init__(self, broker_ip: str, port: int, nome_cliente: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__nome_cliente = nome_cliente
        self.__keepalive = keepalive

    def start_conexao(self):
        mqtt_cliente = mqtt.Client(self.__nome_cliente)
        mqtt_cliente.connect(self.__broker_ip, self.__port, self.__keepalive)
        mqtt_cliente.loop_start()