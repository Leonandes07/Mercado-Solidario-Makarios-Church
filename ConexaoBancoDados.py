import mysql.connector

# Configurar conexão com MySQL
conn = mysql.connector.connect(
    host="localhost",  # Endereço do servidor MySQL
    user="root",  # Usuário do banco de dados
    password="12345678",  # Senha do banco de dados
    database="Lista_de_produtos"  # Nome do banco de dados
)

cursor = conn.cursor()
print("Conexão com MySQL estabelecida!")

# Criar tabela para armazenar produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    codigo_barra VARCHAR(13) NOT NULL
)
""")
conn.commit()
print("Tabela 'produtos' criada com sucesso!")
 
# Inserir produtos no banco de dados
produtos = [
    ("Óleo", "Óleo de cozinha 900ml", "1234567890123"),
    ("Arroz", "Arroz branco tipo 1 - 5kg", "9876543210987"),
    ("Macarrão", "Macarrão espaguete 500g", "5678901234567"),
    ("Feijão", "Feijão carioca 1kg", "3456789012345")
]

cursor.executemany("INSERT INTO produtos (nome, descricao, codigo_barra) VALUES (%s, %s, %s)", produtos)
conn.commit()
print("Produtos inseridos com sucesso!")

# Consultar produtos no banco de dados
cursor.execute("SELECT * FROM produtos")
for produto in cursor.fetchall():
    print(produto)

# Fechar conexão
conn.close()
print("Conexão com MySQL encerrada.")