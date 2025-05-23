import sqlite3
import qrcode

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect("produtos.db")
cursor = conn.cursor()

# Criar tabela para armazenar os produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL
)
""")
conn.commit()

# Lista de produtos
produtos = [
    ("Óleo", "Óleo de cozinha 900ml"),
    ("Arroz", "Arroz branco tipo 1 - 5kg"),
    ("Macarrão", "Macarrão espaguete 500g"),
    ("Feijão", "Feijão carioca 1kg")
]

# Inserir produtos no banco de dados
for produto in produtos:
    cursor.execute("INSERT INTO produtos (nome, descricao) VALUES (?, ?)", produto)
conn.commit()

# Gerar QR Codes para cada produto
cursor.execute("SELECT id, nome, descricao FROM produtos")
for produto in cursor.fetchall():
    produto_id, nome, descricao = produto
    data = f"Produto: {nome}\nDescrição: {descricao}\nID: {produto_id}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(f"qrcode_{produto_id}.png")

    print(f"QR Code gerado para {nome}: qrcode_{produto_id}.png")

print("Todos os QR Codes foram gerados com sucesso!")