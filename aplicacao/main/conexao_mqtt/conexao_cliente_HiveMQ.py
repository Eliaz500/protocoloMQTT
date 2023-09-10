import paho.mqtt.client as mqtt

class Conexao_Cliente_HiveMQ:

    def __init__(self, broker_ip: str, port: int, client_name: str, password: str):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__password = password


    def inicia_conexao_HiveMQ(self):
        cliente_mqtt = mqtt.Client(self.__client_name, userdata=None, protocol=mqtt.MQTTv5)

        # ativar TLS para conexão segura
        #cliente_mqtt.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        cliente_mqtt.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

        # definir nome de usuário e senha
        cliente_mqtt.username_pw_set(self.__client_name, self.__password)

        # conecte-se ao HiveMQ Cloud na porta 8883 (padrão para MQTT)
        cliente_mqtt.connect(host=self.__broker_ip, port=self.__port)


        self.__cliente_mqtt = cliente_mqtt

        # loop_forever para simplificar, aqui você precisa parar o loop manualmente
        # você também pode usar loop_start e loop_stop
        self.__cliente_mqtt.loop_start()

    def finaliza_conexao_HiveMQ(self):
        try:
            self.__cliente_mqtt.loop_stop()
            self.__cliente_mqtt.disconnect()
            return True
        except:
            return False