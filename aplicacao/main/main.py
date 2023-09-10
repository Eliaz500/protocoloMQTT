import time
# -------- CONFIGURACAO LOCALHOST
from aplicacao.configuracao.broker_LOCALHOST_configuracao import configuracao_broker_mqtt

# -------- CONFIGURACAO HIVEMQ
from aplicacao.configuracao.broker_HiveMQ_configuracao import configuracao_broker_mqtt_HiveMQ

# -------- CONEXAO LOCALHOST
from .conexao_mqtt.conexao_cliente_LOCALHOST import Conexao_Cliente

# -------- CONEXAO HIVEMQ
from .conexao_mqtt.conexao_cliente_HiveMQ import Conexao_Cliente_HiveMQ


def start():
    # ----- CONEXAO LOCALHOST ------------------
    # cliente_mqtt = Conexao_Cliente(
    #     configuracao_broker_mqtt["HOST"],
    #     configuracao_broker_mqtt["PORT"],
    #     configuracao_broker_mqtt["CLIENT_NAME"],
    #     configuracao_broker_mqtt["KEEPALIVE"]
    # )
    # cliente_mqtt.inicia_conexao()

    # ----- CONEXAO HIVEMQ------------------
    cliente_mqtt = Conexao_Cliente_HiveMQ(
        configuracao_broker_mqtt_HiveMQ["HOST"],
        configuracao_broker_mqtt_HiveMQ["PORT"],
        configuracao_broker_mqtt_HiveMQ["CLIENT_NAME"],
        configuracao_broker_mqtt_HiveMQ["PASSWORD"],
        configuracao_broker_mqtt_HiveMQ["TOPIC"],
        configuracao_broker_mqtt_HiveMQ["PUBlISH"]
    )
    cliente_mqtt.inicia_conexao_HiveMQ()

    while True: time.sleep(0.001)

