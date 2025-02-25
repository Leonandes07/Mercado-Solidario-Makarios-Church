from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, mundo! Bem-vindo à minha aplicação Flask!"

if __name__ == '__main__':
    app.run(debug=True)
