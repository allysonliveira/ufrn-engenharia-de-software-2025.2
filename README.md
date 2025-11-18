# Projeto de Engenharia de Software - DCA - UFRN

Repositório referente às atividades da disciplina de Engenharia de Software, Departamento de Engenharia de Computação, Universidade Federal do Rio Grande do Norte.

> *Repositório em construção, será atualizado durante a implementação do projeto.*

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Status do Projeto: MVP Web com Flask](#status-do-projeto-mvp-web-com-flask)
- [Arquitetura e Modelagem (UML)](#arquitetura-e-modelagem-uml)
- [Como Executar o MVP](#como-executar-o-mvp)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Licença](#licença)

## Sobre o Projeto

### Título
"Meu Posto de Saúde"

### Descrição
Trata-se da implementação de um sistema web para utilização em rotinas de um posto de saúde, como cadastro de usuários (pacientes, médicos, enfermeiros, etc.), agendamento de consultas e exames, e verificação de receitas médicas.

### Componentes
- ALLYSON MATHEUS GUEDES DE OLIVEIRA
- NICOLAS DANIEL DA ROCHA SILVA

## Status do Projeto: MVP Web com Flask

O projeto atingiu a etapa de **Produto Mínimo Viável (MVP)**. 

O backend é construído em **Python** (mantendo a lógica de negócio na pasta `src/`) e o frontend é construído com **HTML/CSS** (o arquivo `static/style.css`). O framework **Flask** é utilizado como a ponte que serve as páginas HTML e conecta a interface do usuário ao backend.

O design da lógica de negócios aplica os Padrões de Projeto **Facade**, **Factory Method** e **Singleton** para garantir um código de baixo acoplamento e alta coesão.

Para uma explicação detalhada da arquitetura e da aplicação dos padrões de projeto, consulte o relatório:

* **[Relatório de Padrões do MVP](./docs/padroes-de-mvp.md)**

## Arquitetura e Modelagem (UML)

A modelagem UML (Diagrama de Casos de Uso, Diagrama de Classes) que serviu de base para a construção do MVP pode ser encontrada no diretório `uml/`.

* **[Documentação dos Diagramas UML](./uml/diagramas.md)**

## Como Executar o MVP

A aplicação agora roda como um servidor web local usando Flask.

1.  **Clone o repositório:** Navegue até a pasta raiz do projeto.
2.  **Crie o Ambiente Virtual** (só na primeira vez):
    ```bash
    python -m venv .venv
    ```
    ou

    ```bash
    python3 -m venv .venv
    ```

3.  **Ative o Ambiente Virtual:**
    ```bash
    source .venv/bin/activate
    ```
    *(Seu terminal mostrará `(.venv)` no início)*
4.  **Instale as dependências** (só na primeira vez):
    ```bash
    pip install Flask
    ```
5.  **Execute o servidor Flask:**
    ```bash
    python -m venv .venv
    ```
    ou

    ```bash
    python3 app.py
    ```
6.  **Acesse o site:** Abra seu navegador e acesse: `http://127.0.0.1:5000`

## Estrutura do Projeto

```bash
ufrn-engenharia-de-software-2025.2/
├── .venv/
├── app.py
├── docs/
│   ├── historias-de-usuario.md
│   ├── principios-de-projeto.md
│   └── padroes-de-mvp.md
├── src/
│   ├── __init__.py
│   ├── factories/
│   │   ├── __init__.py
│   │   └── usuario_factory.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── usuario.py
│   └── services/
│       ├── __init__.py
│       ├── cadastro_facade.py
│       └── logger_service.py
├── static/
│   └── style.css
├── templates/
│   ├── agendar.html
│   ├── base.html
│   ├── cadastro.html
│   ├── dashboard.html
│   └── index.html
├── uml/
│   ├── diagrama-de-casos-de-uso.drawio
│   ├── diagrama-de-casos-de-uso.png
│   ├── diagrama-estrutural.drawio
│   ├── diagrama-estrutural.png
│   └── diagramas.md
├── .gitignore
├── LICENSE
└── README.md
```

- **`app.py`**: O servidor web Flask. É o "coração" da aplicação que conecta tudo.
- **`templates/`**: Contém todos os arquivos HTML que compõem o frontend (as páginas do site).
- **`static/`**: Contém os arquivos de estilo (CSS), imagens e (futuramente) JavaScript.
- **`src/`**: Contém toda a lógica de negócio do backend (Padrões de Projeto, etc.), separada da interface.
- **`src/models/`**: Define as classes de entidade (ex: `Paciente`, `Medico`).
- **`src/factories/`**: Contém o padrão Factory para a criação de objetos.
- **`src/services/`**: Contém a lógica de negócio (Facade, Logger, etc.).
- **`docs/`**: Contém a documentação de apoio (Histórias de Usuário, relatórios de princípios e padrões).
- **`uml/`**: Contém os artefatos de modelagem UML.
- **`.venv/`**: Pasta do ambiente virtual do Python (ignorada pelo Git).

## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.