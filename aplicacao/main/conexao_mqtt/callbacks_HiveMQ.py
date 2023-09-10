from aplicacao.configuracao.broker_HiveMQ_configuracao import configuracao_broker_mqtt_HiveMQ

# definir retornos de chamada para diferentes eventos para ver se funciona, imprimir a mensagem etc.
def on_connect_HiveMQ(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f'Cliente Conectado com sucesso: {client}')
        client.subscribe(configuracao_broker_mqtt_HiveMQ["TOPIC"])
    else:
        print(f'Erro ao se conectar! Erro = {rc}')


# imprimir qual tópico foi inscrito
def on_subscribe_HiveMQ(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: "  + str(mid) + " " + configuracao_broker_mqtt_HiveMQ["TOPIC"] + str(granted_qos))

# mensagem de impressão, útil para verificar se foi bem-sucedida
def on_message_HiveMQ(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))



# com este retorno de chamada você pode ver se sua publicação foi bem-sucedida
def on_publish_HiveMQ(client, userdata, mid, properties=None):
    print("mid: " + str(mid))