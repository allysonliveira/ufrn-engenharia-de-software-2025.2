#Este arquivo implementa a fábrica para criação de usuários do sistema,
#seguindo o padrão de projeto "Factory Method".

from src.models.usuario import Usuario, Paciente, Medico, Enfermeiro

class UsuarioFactory:
    
    def criar_usuario(self, tipo: str, dados: dict) -> Usuario:
        try:
            if tipo == "paciente":
                return Paciente(
                    nome=dados["nome"],
                    cpf=dados["cpf"],
                    cartao_sus=dados["cartao_sus"]
                )
            elif tipo == "medico":
                return Medico(
                    nome=dados["nome"],
                    cpf=dados["cpf"],
                    crm=dados["crm"]
                )
            elif tipo == "enfermeiro":
                return Enfermeiro(
                    nome=dados["nome"],
                    cpf=dados["cpf"],
                    coren=dados["coren"]
                )
            else:
                raise ValueError(f"Tipo de usuário desconhecido: {tipo}")
        except KeyError as e:
            raise ValueError(f"Dado obrigatório ausente para {tipo}: {e}")