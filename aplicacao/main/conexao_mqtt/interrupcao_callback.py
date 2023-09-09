from aplicacao.configuracao.broker_configuracao import configuracao_broker_mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'Cliente Conectado com sucesso: {client}')
        client.subscribe(configuracao_broker_mqtt["TOPIC"])
    else:
        print(f'Erro ao se conectar! Erro = {rc}')

def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Cliente Subscribed at {configuracao_broker_mqtt["TOPIC"]}')
    print(f'QOS:  {granted_qos}')

def on_message(client, userdata, message):
    print('Mensagem Recebida')
    print(client)
    print(message.payload)