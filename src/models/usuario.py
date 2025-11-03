#Este arquivo define a estrutura base para os usuários do sistema,
#seguindo o padrão de projeto "Interface" .

from abc import ABC, abstractmethod

# Esta é a nossa "Interface"
# Todos os usuários concretos devem seguir este contrato.

class Usuario(ABC):
    #Esta classe abstrata define a interface para os usuários do sistema.
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
    @abstractmethod

    def descrever_funcao(self): #Método abstrato que as classes filhas devem implementar
        pass

# Classes Concretas
# Implementações da interface

class Paciente(Usuario):
    # Implementação concreta de um Paciente.
    def __init__(self, nome: str, cpf: str, cartao_sus: str):
        super().__init__(nome, cpf)
        self.cartao_sus = cartao_sus

    def descrever_funcao(self):
        return f"Paciente: {self.nome} (SUS: {self.cartao_sus})"

class Medico(Usuario):
    # Implementação concreta de um Médico.
    def __init__(self, nome: str, cpf: str, crm: str):
        super().__init__(nome, cpf)
        self.crm = crm

    def descrever_funcao(self):
        return f"Médico: {self.nome} (CRM: {self.crm})"

class Enfermeiro(Usuario):
    # Implementação concreta de um Enfermeiro.
    def __init__(self, nome: str, cpf: str, coren: str):
        super().__init__(nome, cpf)
        self.coren = coren

    def descrever_funcao(self):
        return f"Enfermeiro: {self.nome} (COREN: {self.coren})"