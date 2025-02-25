import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_notificacao_email(produto, quantidade):
    remetente = "seu_email@gmail.com"
    senha = "sua_senha"
    destinatario = "destinatario@gmail.com"

    # Configurar servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remetente, senha)

    # Criar mensagem
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = f"Estoque Baixo: {produto}"

    corpo = f"O produto {produto} está com baixa quantidade em estoque: {quantidade} unidades restantes."
    mensagem.attach(MIMEText(corpo, 'plain'))

    # Enviar email
    server.send_message(mensagem)
    server.quit()
