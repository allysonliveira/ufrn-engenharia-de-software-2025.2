# Projeto de Engenharia de Software - DCA - UFRN

Repositório referente às atividades da disciplina de Engenharia de Software, Departamento de Engenharia de Computação, Universidade Federal do Rio Grande do Norte.

> *Repositório em construção, será atualizado durante a implementação do projeto.*

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Status do Projeto: MVP Implementado](#status-do-projeto-mvp-implementado)
- [Arquitetura e Modelagem (UML)](#arquitetura-e-modelagem-uml)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar o MVP](#como-executar-o-mvp)
- [Licença](#licença)

## Sobre o Projeto

### Título
"Meu Posto de Saúde"

### Descrição
Trata-se da implementação de um sistema para utilização em rotinas de um posto de saúde, como cadastro de usuários (pacientes, médicos, enfermeiros, etc.), agendamento de consultas e exames, e verificação de receitas médicas.

### Componentes
- ALLYSON MATHEUS GUEDES DE OLIVEIRA
- DIEGO MEDEIROS PONTE
- NICOLAS DANIEL DA ROCHA SILVA

# Fase atual do projeto: estruturação de MVP 

O projeto atingiu a etapa de **Produto Mínimo Viável (MVP)**, com a implementação da funcionalidade central de cadastro de paciente.

A arquitetura do MVP foi construída em **Python**, utilizando **Tkinter** para a interface gráfica (GUI). O design aplica os Padrões de Projeto **Facade**, **Factory Method** e **Singleton** para garantir um código de baixo acoplamento e alta coesão.

Para uma explicação detalhada da arquitetura e da aplicação dos padrões de projeto, consulte o relatório:

* **[Relatório de Padrões do MVP](./docs/padroes-de-mvp.md)**

## Arquitetura e Modelagem (UML)

A modelagem UML (Diagrama de Casos de Uso, Diagrama de Classes) que serviu de base para a construção do MVP pode ser encontrada no diretório `uml/`.

* **[Documentação dos Diagramas UML](./uml/diagramas.md)**

## Como Executar o MVP:

1.  Certifique-se de ter o Python ou o Python 3 instalado (`python, python3`).
2.  Clone o repositório e navegue até a pasta raiz do projeto.
3.  Execute a aplicação através do módulo `main`:

    ```bash
    python src/main.py
    ```
    ou

    ```bash
    python3 src/main.py
    ```

4.  Insira um valor para "Nome Completo", "CPF" e "Cartão do SUS":
O sistema irá responder que o cadastro foi feito e os padrões mínimos do MVP solicitados estão implementados.

## Estrutura do Projeto
    ufrn-projeto-de-engenharia-de-software/

    ├── docs/
        └── historias-de-usuario.md
        └── principios-de-projeto.md    
        └── padroes-de-mvp.md 

    ├── src/
        ├── factories/
            └── usuario_factory.py
    
        ├── models/ 
            └── usuario.py 

        └── services/  
            └── cadastro_facade.py 
            └── logger_service.py 

    ├── gui_app.py 
    ├── main.py 

    ├── uml/
        └── diagrama-de-casos-de-uso.drawio
        └── diagrama-de-casos-de-uso.png
        └── diagrama-estrutural.drawio
        └── diagrama-estrutural.png
        └── diagramas.md

    ├── .gitignore 
    ├── LICENSE 
    ├── README.md  




- **`docs/`**: Contém a documentação de apoio (Histórias de Usuário, relatórios de princípios e padrões).
- **`src/`**: Contém o código-fonte do MVP em Python.
- **`src/models/`**: Define as classes de entidade (ex: `Paciente`, `Medico`).
- **`src/factories/`**: Contém o padrão Factory para a criação de objetos.
- **`src/services/`**: Contém a lógica de negócio (Facade, Logger, etc.).
- **`src/gui_app.py`**: A interface gráfica do usuário (em fase inicial).
- **`src/main.py`**: Ponto de entrada para executar a aplicação.
- **`uml/`**: Contém os artefatos de modelagem UML.

## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.
