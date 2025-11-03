# Método Singleton na prática com python:
# - A instância é única no momento em que o módulo é lido.
# - O Python armazena este módulo em cache.
# - Qualquer outro arquivo que importar "logger" receberá esta *mesma* instância.

#Essa classe implementa um serviço de logging seguindo o padrão Singleton em Python.
class LoggerService:
       
    def __init__(self):
        # Esta mensagem serve para provar que o construtor
        # é chamado apenas uma vez, na primeira importação.
        print(">>> LoggerService inicializado (INSTÂNCIA ÚNICA CRIADA) <<<")
        self.logs = []

    def log(self, message: str):
        #Adiciona uma mensagem de log ao nosso registro.
        print(f"[LOG] {message}")
        self.logs.append(message)

    def mostrar_logs(self):
        print("\n--- Histórico de Logs ---")
        for log in self.logs:
            print(log)
        print("------------------------")

logger = LoggerService()