import time
from aplicacao.configuracao.broker_configuracao import configuraco_broker_mqtt
from .conexao_mqtt.conexao_cliente import Conexao_Cliente

def start():
    cliente_mqtt = Conexao_Cliente(
        configuraco_broker_mqtt["HOST"],
        configuraco_broker_mqtt["PORT"],
        configuraco_broker_mqtt["CLIENT_NAME"],
        configuraco_broker_mqtt["KEEPALIVE"]
    )
    cliente_mqtt.inicia_conexao()

    while True: time.sleep(0.001)

