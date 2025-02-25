import requests

def enviar_notificacao_push(produto, quantidade):
    server_key = 'sua_fcm_server_key'
    url = 'https://fcm.googleapis.com/fcm/send'
    headers = {
        'Authorization': f'key={server_key}',
        'Content-Type': 'application/json'
    }
    body = {
        'notification': {
            'title': f'Estoque Baixo: {produto}',
            'body': f'O produto {produto} está com baixa quantidade em estoque: {quantidade} unidades restantes.'
        },
        'to': '/topics/all'
    }
    response = requests.post(url, headers=headers, json=body)
    print(response.status_code, response.json())


#A função requests é usada para fazer requisições HTTP em Python
# Ela permite que você envie requisições HTTP, como GET e POST, de forma fácil e intuitiva
# Como exemplo, a função enviar_notificacao_push está usando a biblioteca requests para enviar
# uma notificação push para um servidor de notificações Firebase Cloud Messaging (FCM). Onde:

#server_key: Chave do servidor FCM
#url: URL para enviar a requisição POST ao FCM
#headers: Cabeçalhos HTTP necessários para autenticação e tipo de conteúdo
#body: Corpo da requisição que contém os detalhes da notificação