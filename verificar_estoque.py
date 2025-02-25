# Teste da função verificar_estoque
def testar_verificar_estoque():
    # Simular a função de enviar email para verificação visual
    def enviar_notificacao_email(produto, quantidade):
        print(f"Email enviado: O produto {produto} está com baixa quantidade em estoque: {quantidade} unidades restantes.")
    
    # Função modificada para usar a função simulada de envio de email
    def verificar_estoque():
        with open('cadastro_produtos.csv', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                nome_produto, categoria, quantidade, descricao = row
                quantidade = int(quantidade)
                if quantidade < 2:  # Defina o limite para baixa quantidade
                    enviar_notificacao_email(nome_produto, quantidade)

    verificar_estoque()

