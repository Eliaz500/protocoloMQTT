import time
from aplicacao.configuracao.configuracao_broker import configuracao_broker
from .conexao_mqtt.conexao_cliente import Conexao_Cliente


def start():
    conexao_cliente_mqtt = Conexao_Cliente(
        configuracao_broker["HOST"],
        configuracao_broker["PORT"],
        configuracao_broker["CLIENT_NAME"],
        configuracao_broker["KEEPALIVE"]
    )
    conexao_cliente_mqtt.start_conexao()

    while True: time.sleep(0.001)
