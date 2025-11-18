# Projeto de Engenharia de Software - DCA - UFRN

Repositório referente às atividades da disciplina de Engenharia de Software, Departamento de Engenharia de Computação, Universidade Federal do Rio Grande do Norte.

> *Repositório em construção, será atualizado durante a implementação do projeto.*

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Status do Projeto: Fase de Testes CI/CD](#status-do-projeto-fase-de-testes)
- [Documentação do Projeto](#documentação-do-projeto)
- [Como Executar a Aplicação](#como-executar-a-aplicação)
- [Como Executar os Testes](#como-executar-os-testes)
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

## Status do Projeto: Fase de Testes e Qualidade (CI/CD)

O projeto atingiu a etapa de **Produto Mínimo Viável (MVP)** e agora está na fase de **Testes e Qualidade (CI/CD)**.

O backend é construído em **Python** (lógica de negócio na pasta `src/`) e o frontend com **HTML/CSS** (pastas `templates/` e `static/`). O framework web **Flask** é utilizado como a ponte que serve as páginas HTML e conecta a interface ao backend.

A fase atual de testes implementa **testes de unidade** com **Pytest** e **Pytest-Cov** para garantir a corretude da lógica de negócio e uma alta cobertura de código.

## Documentação do Projeto

Toda a documentação do projeto está contida nas pastas `docs/` e `uml/`:

* **[Relatório de Testes de Unidade](./docs/relatorio-de-testes.md)** (Fase Atual)
* **[Relatório de Padrões do MVP](./docs/padroes-de-mvp.md)**
* **[Documentação dos Diagramas UML](./uml/diagramas.md)**
* **[Histórias de Usuário](./docs/historias-de-usuario.md)**

## Como Executar a Aplicação

A aplicação roda como um servidor web local usando Flask.

1.  **Clone o repositório:** Navegue até a pasta raiz do projeto.
2.  **Crie o Ambiente Virtual** (só na primeira vez):
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
    pip install Flask pytest pytest-cov
    ```
5.  **Execute o servidor Flask:**
    ```bash
    python3 app.py
    ```
6.  **Acesse o site:** Abra seu navegador e acesse: `http://127.0.0.1:5000`

## Como Executar os Testes

Para validar a integridade do código, execute os testes de unidade.

1.  Certifique-se de que o ambiente virtual está ativado (`source .venv/bin/activate`).
2.  Execute o Pytest com o relatório de cobertura:
    ```bash
    python3 -m pytest --cov=src
    ```

## Estrutura do Projeto

```bash
ufrn-engenharia-de-software-2025.2/
├── .venv/
├── app.py
├── docs/
│   ├── historias-de-usuario.md
│   ├── principios-de-projeto.md
│   ├── padroes-de-mvp.md
│   └── relatorio-de-testes.md
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
├── tests/
│   └── test_usuario_factory.py
├── uml/
│   ├── (arquivos de diagramas...)
│   └── diagramas.md
├── .gitignore
├── LICENSE
└── README.md
```

- **`.venv/`**: Pasta do ambiente virtual do Python, é criado no momento em que é executada a aplicação (ignorada pelo Git).
- **`templates/`**: [Frontend] Contém todos os arquivos HTML que compõem o as páginas do site.
- **`static/`**: [Frontend] Contém os arquivos de estilo (CSS), imagens e (futuramente) JavaScript.
- **`src/`**: [Backend] Contém toda a lógica de negócio do backend (Padrões de Projeto, etc.), separada da interface.
- **`tests/`**: Contém os testes de unidade (Pytest) do projeto.
- **`docs/`**: Contém a documentação de apoio (Histórias de Usuário, relatórios de princípios e padrões).
- **`uml/`**: Contém os arquivos de modelagem UML.
- **`app.py`**: O servidor do framework web Flask. Elemento principal para executar a aplicação e conecta tudo as partes backend e frontend.


## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.
