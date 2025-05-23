import sqlite3
import barcode
from barcode.writer import ImageWriter

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect("produtos.db")
cursor = conn.cursor()

# Criar tabela para armazenar os produtos
cursor.execute("DROP TABLE IF EXISTS produtos")
cursor.execute("""
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    codigo_barra TEXT NOT NULL
)
""")
conn.commit()

# Lista de produtos com códigos fictícios (EAN-13 exige 12 números, o último é gerado automaticamente)
produtos = [
    ("Óleo", "Óleo de cozinha 900ml", "123456789012"),
    ("Arroz", "Arroz branco tipo 1 - 5kg", "987654321098"),
    ("Macarrão", "Macarrão espaguete 500g", "567890123456"),
    ("Feijão", "Feijão carioca 1kg", "345678901234")
]

# Inserir produtos no banco de dados e gerar códigos de barras
for nome, descricao, codigo in produtos:
    cursor.execute("INSERT INTO produtos (nome, descricao, codigo_barra) VALUES (?, ?, ?)", (nome, descricao, codigo))
    conn.commit()

    # Gerar código de barras
    barcode_obj = barcode.get("ean13", codigo, writer=ImageWriter())
    barcode_obj.save(f"barcode_{codigo}")

    print(f"Código de barras gerado para {nome}: barcode_{codigo}.png")

print("Todos os códigos de barras foram gerados com sucesso!")
