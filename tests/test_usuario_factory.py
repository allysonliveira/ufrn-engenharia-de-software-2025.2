# tests/test_usuario_factory.py

import pytest

# Importamos a classe que queremos testar (usando import absoluto 'src.')
from src.factories.usuario_factory import UsuarioFactory
# Importamos os tipos que esperamos que ela retorne
from src.models.usuario import Paciente, Medico, Enfermeiro

# Um "Fixture" é uma função de setup que o Pytest executa antes de cada teste
# Aqui, ele cria uma instância da fábrica para usarmos nos testes
@pytest.fixture
def factory():
    return UsuarioFactory()

# --- DADOS DE TESTE ---
dados_paciente = {
    "nome": "Paciente Teste", "cpf": "111", "cartao_sus": "123"
}
dados_medico = {
    "nome": "Medico Teste", "cpf": "222", "crm": "456"
}
dados_enfermeiro = {
    "nome": "Enfermeiro Teste", "cpf": "333", "coren": "789"
}

# --- TESTES DE SUCESSO ---

def test_cria_paciente_com_sucesso(factory):
    # CHAMA A FUNÇÃO
    usuario = factory.criar_usuario("paciente", dados_paciente)
    
    # VERIFICA O RESULTADO
    assert isinstance(usuario, Paciente)
    assert usuario.nome == "Paciente Teste"
    assert usuario.cartao_sus == "123"

def test_cria_medico_com_sucesso(factory):
    # CHAMA A FUNÇÃO
    usuario = factory.criar_usuario("medico", dados_medico)
    
    # VERIFICA O RESULTADO
    assert isinstance(usuario, Medico)
    assert usuario.nome == "Medico Teste"
    assert usuario.crm == "456"

def test_cria_enfermeiro_com_sucesso(factory):
    # CHAMA A FUNÇÃO
    usuario = factory.criar_usuario("enfermeiro", dados_enfermeiro)
    
    # VERIFICA O RESULTADO
    assert isinstance(usuario, Enfermeiro)
    assert usuario.nome == "Enfermeiro Teste"
    assert usuario.coren == "789"

# --- TESTES DE FALHA (Exceções) ---

def test_falha_com_tipo_desconhecido(factory):
    # Verifica se o código dentro do 'with' levanta um ValueError
    with pytest.raises(ValueError) as e:
        factory.criar_usuario("farmaceutico", dados_paciente)
    
    # Verifica se a mensagem de erro está correta
    assert "Tipo de usuário desconhecido" in str(e.value)

def test_falha_com_dados_faltando(factory):
    dados_incompletos = {"nome": "Paciente Incompleto", "cpf": "999"}
    
    # Verifica se o código levanta um ValueError (que vem do KeyError)
    with pytest.raises(ValueError) as e:
        factory.criar_usuario("paciente", dados_incompletos)
    
    # Verifica se a mensagem de erro está correta
    assert "Dado obrigatório ausente" in str(e.value)