
# 'sys' e 'os' usados para manipular caminhos de arquivos
import sys
import os

# 1. Caminho do arquivo atual 
caminho_arquivo_atual = os.path.abspath(__file__)

# 2. Pega o diretório onde este arquivo está 
pasta_src = os.path.dirname(caminho_arquivo_atual)

# 3. Pega o diretório "pai" da pasta 'src' 
raiz_do_projeto = os.path.dirname(pasta_src)

# 4. Adiciona a raiz do projeto ao PATH do Python
# Procura os módulos
if raiz_do_projeto not in sys.path:
    sys.path.append(raiz_do_projeto)

# Iniciando a aplicação GUI, primeiramente importando a classe App
from src.gui_app import App

# Função para iniciar a aplicação GUI
def iniciar_aplicacao():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()