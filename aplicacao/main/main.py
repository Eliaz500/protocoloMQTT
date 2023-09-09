import time
from aplicacao.configuracao.broker_configuracao import configuracao_broker_mqtt
from .conexao_mqtt.conexao_cliente import Conexao_Cliente

def start():
    cliente_mqtt = Conexao_Cliente(
        configuracao_broker_mqtt["HOST"],
        configuracao_broker_mqtt["PORT"],
        configuracao_broker_mqtt["CLIENT_NAME"],
        configuracao_broker_mqtt["KEEPALIVE"]
    )
    cliente_mqtt.inicia_conexao()

    while True: time.sleep(0.001)

