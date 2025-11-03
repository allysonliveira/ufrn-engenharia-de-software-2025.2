
#GUI da aplicação usando Tkinter para aparecer uma janela simples de cadastro de paciente.

import tkinter as tk
from tkinter import ttk, messagebox

# Importação do facade para a GUI
from src.services.cadastro_facade import CadastroFacade

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Meu Posto de Saúde - Cadastro de Paciente")
        self.geometry("400x280") # Tamanho da janela

        # GUI ligada apenas a Facade
        self.facade = CadastroFacade()
        
        self.frame = ttk.Frame(self, padding="20")
        self.frame.pack(expand=True, fill=tk.BOTH)

        #Nome
        ttk.Label(self.frame, text="Nome Completo:").pack(anchor=tk.W)
        self.nome_entry = ttk.Entry(self.frame, width=40)
        self.nome_entry.pack(fill=tk.X, pady=5)

        #CPF
        ttk.Label(self.frame, text="CPF:").pack(anchor=tk.W)
        self.cpf_entry = ttk.Entry(self.frame, width=40)
        self.cpf_entry.pack(fill=tk.X, pady=5)

        #Cartão SUS
        ttk.Label(self.frame, text="Cartão SUS:").pack(anchor=tk.W)
        self.sus_entry = ttk.Entry(self.frame, width=40)
        self.sus_entry.pack(fill=tk.X, pady=5)

        # Botão
        self.cadastrar_btn = ttk.Button(
            self.frame,
            text="Cadastrar Paciente",
            command=self.realizar_cadastro # Comando para o clique do mouse
        )
        self.cadastrar_btn.pack(pady=20)

        # Tecla enter
        self.bind("<Return>", self.realizar_cadastro)

    def realizar_cadastro(self, event=None): # Adicionado 'event=None'
        """
        Função chamada ao clicar no botão de cadastro.
        """
        # 1. Coleta dados da interface
        dados_paciente = {
            "nome": self.nome_entry.get(),
            "cpf": self.cpf_entry.get(),
            "cartao_sus": self.sus_entry.get()
        }
        
        # 2. Chama o método simples da Facade
        sucesso = self.facade.cadastrar_usuario("paciente", dados_paciente)
        
        # 3. Exibe o resultado para o usuário
        if sucesso:
            # Mensagem do sistema
            messagebox.showinfo(
                "Cadastro Realizado",
                f"Paciente {dados_paciente['nome']} cadastrado com sucesso!"
            )
            # Limpa os campos após o sucesso
            self.nome_entry.delete(0, tk.END)
            self.cpf_entry.delete(0, tk.END)
            self.sus_entry.delete(0, tk.END)
        else:
            # Mensagem do sistema em caso de erro
            messagebox.showerror(
                "Erro no Cadastro",
                "Não foi possível cadastrar o paciente. Verifique os dados ou contate o suporte."
            )