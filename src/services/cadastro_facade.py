
# Este arquivo implementa a fachada para o sistema de cadastro de usuários.
# A fachada simplifica a interface para o cliente,
# encapsulando a complexidade do sistema de cadastro.

from src.services.logger_service import logger
from src.factories.usuario_factory import UsuarioFactory
from src.models.usuario import Usuario

class CadastroFacade:
    
    def __init__(self):
        self.logger = logger
        self.factory = UsuarioFactory()
        self.logger.log("CadastroFacade inicializada.")

    def cadastrar_usuario(self, tipo: str, dados: dict) -> bool:
        self.logger.log(f"Iniciando tentativa de cadastro (via Facade) para tipo '{tipo}'...")
        
        try:
            novo_usuario = self.factory.criar_usuario(tipo, dados)
            print(f"[FACADE] Simulação de salvamento de: {novo_usuario.descrever_funcao()}")
            
            self.logger.log("Cadastro (via Facade) bem-sucedido.")
            return True
            
        except ValueError as e:
            self.logger.log(f"[ERRO FACADE] Falha no cadastro: {e}")
            return False