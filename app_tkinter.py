import tkinter as tk # Importa a biblioteca para criar a tela inicial
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv # Importa a biblioteca para o banco de dados
import smtplib # Importa a biblioteca para realizar as notificaçoes via email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pusher # Importa a biblioteca para realizar as notificaçoes via push


# Função para enviar notificações por email
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

# Função para verificar estoque e enviar notificações
def verificar_estoque():
    with open('cadastro_produtos.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            nome_produto, categoria, quantidade, descricao = row
            quantidade = int(quantidade)
            if quantidade < 5:  # Defina o limite para baixa quantidade
                enviar_notificacao_email(nome_produto, quantidade)

# Função para salvar os dados dos usuários
def salvar_dados_usuario():
    nome = nome_entry.get().strip()
    email = email_entry.get().strip()
    tipo_usuario = tipo_usuario_combo.get().strip()

    if not nome or not email or not tipo_usuario:
        messagebox.showerror("Erro de Validação", "Todos os campos são obrigatórios!")
        return

    print(f"Nome: {nome}, Email: {email}, Tipo: {tipo_usuario}")

    with open('cadastro_usuarios.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome, email, tipo_usuario])

    messagebox.showinfo("Usuário Cadastrado", "Seja Bem-Vindo!")

# Função para salvar os dados dos produtos
def salvar_dados_produto():
    nome_produto = nome_produto_entry.get().strip()
    categoria = categoria_produto_combo.get().strip()
    quantidade = quantidade_produto_entry.get().strip()
    descricao = descricao_produto_entry.get().strip()

    if not nome_produto or not categoria or not quantidade or not descricao:
        messagebox.showerror("Erro de Validação", "Todos os campos são obrigatórios!")
        return

    print(f"Produto: {nome_produto}, Categoria: {categoria}, Quantidade: {quantidade}, Descrição: {descricao}")

    with open('cadastro_produtos.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome_produto, categoria, quantidade, descricao])

    messagebox.showinfo("Produto Cadastrado", "Deus te abençoe!")

    # Chamar a função de verificação de estoque após salvar os dados do produto
    verificar_estoque()

# Configura a janela principal
root = tk.Tk()
root.title("Mercado Solidário Makarios Church")

# Carregar a imagem usando Pillow 
img_path = "C:/Users/Leone Fernandes/Desktop/App_TKinter/img.png"
img = Image.open(img_path) 
img = img.resize((100, 100), Image.Resampling.LANCZOS) # Redimensionar a imagem se necessário. A partir da versão 10.0.0 do Pillow, o atributo ANTIALIAS foi descontinuado e substituído por Resampling.LANCZOS
img = ImageTk.PhotoImage(img)

# Frame para a imagem
frame_imagem = ttk.Frame(root)
frame_imagem.pack(side=tk.TOP, pady=10)
label_imagem = ttk.Label(frame_imagem, image=img)
label_imagem.pack()

# Configura o notebook para as abas
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Frame para o cadastro de usuários
frame_usuarios = ttk.Frame(notebook, padding="10")
notebook.add(frame_usuarios, text="Cadastro de Usuários")

# Frame para o cadastro de produtos
frame_produtos = ttk.Frame(notebook, padding="10")
notebook.add(frame_produtos, text="Cadastro de Produtos")

# Seção de cadastro de usuários
ttk.Label(frame_usuarios, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
nome_entry = ttk.Entry(frame_usuarios, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame_usuarios, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
email_entry = ttk.Entry(frame_usuarios, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame_usuarios, text="Tipo de Usuário:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
tipo_usuario_combo = ttk.Combobox(frame_usuarios, values=["Usuário do Sistema", "Voluntário"])
tipo_usuario_combo.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

salvar_button_usuario = ttk.Button(frame_usuarios, text="Salvar", command=salvar_dados_usuario)
salvar_button_usuario.grid(row=3, column=0, columnspan=2, pady=10)

# Seção de cadastro de produtos
ttk.Label(frame_produtos, text="Nome do Produto:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
nome_produto_entry = ttk.Entry(frame_produtos, width=30)
nome_produto_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame_produtos, text="Categoria:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
categoria_produto_combo = ttk.Combobox(frame_produtos, values=["Alimentos", "Higiene Pessoal", "Material de Limpeza", "Roupas", "Brinquedos", "Outros"])
categoria_produto_combo.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame_produtos, text="Quantidade:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
quantidade_produto_entry = ttk.Entry(frame_produtos, width=30)
quantidade_produto_entry.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

ttk.Label(frame_produtos, text="Descrição:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
descricao_produto_entry = ttk.Entry(frame_produtos, width=30)
descricao_produto_entry.grid(row=3, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

salvar_button_produto = ttk.Button(frame_produtos, text="Salvar", command=salvar_dados_produto)
salvar_button_produto.grid(row=4, column=0, columnspan=2, pady=10)

# Ajusta o tamanho da janela para se adaptar ao conteúdo
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame_usuarios.columnconfigure(1, weight=1)
frame_produtos.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
root.mainloop()
