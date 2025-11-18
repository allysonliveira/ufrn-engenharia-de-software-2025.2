# app.py

import sys
import os
from flask import Flask, render_template, request, redirect, url_for, flash

# --- INÍCIO DA CORREÇÃO DE IMPORTAÇÃO ---
# Isso "ensina" o Flask a encontrar sua pasta 'src'
caminho_arquivo_atual = os.path.abspath(__file__)
raiz_do_projeto = os.path.dirname(caminho_arquivo_atual)
if raiz_do_projeto not in sys.path:
    sys.path.append(raiz_do_projeto)
# --- FIM DA CORREÇÃO DE IMPORTAÇÃO ---

# 1. IMPORTANDO O SEU BACKEND
from src.services.cadastro_facade import CadastroFacade

# 2. INICIALIZANDO O FLASK
app = Flask(__name__, template_folder='templates', static_folder='static')
# Chave secreta necessária para 'flash messages' (mensagens de pop-up)
app.secret_key = 'sua-chave-secreta-aleatoria-123'

# 3. INICIALIZANDO O BACKEND
# Criamos UMA instância da Facade para o app inteiro usar.
# A facade, por sua vez, já inicializa o Singleton do logger.
sistema_de_cadastro = CadastroFacade()


# --- 4. DEFININDO AS ROTAS (PÁGINAS) DO SITE ---

@app.route("/")
def index():
    """Esta função serve a página index.html"""
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    """
    Esta rota serve a página de cadastro (GET)
    e recebe os dados do formulário (POST).
    """
    
    # Se o usuário estiver enviando dados (método POST)...
    if request.method == "POST":
        
        # 1. Coleta os dados do formulário HTML
        dados_formulario = {
            "nome": request.form.get("nome"),
            "cpf": request.form.get("cpf"),
            "cartao_sus": request.form.get("cartao_sus"),
            "email": request.form.get("email")
            # Ignoramos a senha por enquanto, pois o backend não a usa
        }
        
        # 2. **A MÁGICA ACONTECE AQUI**
        # Chamamos a *mesma* Facade do nosso backend (Python/Tkinter),
        # mas agora os dados vêm do formulário web.
        sucesso = sistema_de_cadastro.cadastrar_usuario("paciente", dados_formulario)
        
        if sucesso:
            # 'flash' cria uma mensagem pop-up para a próxima página
            flash("Paciente cadastrado com sucesso!", "success")
            # Redireciona para o dashboard
            return redirect(url_for("dashboard"))
        else:
            # Mostra uma mensagem de erro
            flash("Erro ao cadastrar. Verifique os dados.", "danger")
            # Continua na página de cadastro
            return render_template("cadastro.html")

    # Se o usuário estiver apenas visitando a página (método GET)
    return render_template("cadastro.html")

@app.route("/dashboard")
def dashboard():
    """Esta função serve a página dashboard.html"""
    return render_template("dashboard.html")

@app.route("/agendar")
def agendar():
    """Esta função serve a página agendar.html"""
    return render_template("agendar.html")

# --- 5. PONTO DE ENTRADA PARA EXECUTAR O SERVIDOR ---
if __name__ == "__main__":
    # O debug=True faz o servidor reiniciar sozinho quando você salvar o arquivo
    app.run(debug=True, port=5000)