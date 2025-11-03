# Estrutura do MVP (Produto Mínimo Viável) do Projeto "Meu Posto de Saúde"

Este documento descreve os padrões de projeto utilizados na implementação do MVP (Produto Mínimo Viável) do sistema "Meu Posto de Saúde".

O MVP implementado consiste na funcionalidade principal de **Cadastro de Paciente** através de uma GUI (interface gráfica). A arquitetura foi desenhada para ser flexível, manutenível e de baixo acoplamento, aplicando os seguintes padrões:

## 1. Padrões de Projeto Utilizados

### Padrão Singleton (Criacional)

* **O que é:** Garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a ela.
* **Onde foi aplicado:** Foi utilizado para criar a classe `LoggerService` (no arquivo `src/services/logger_service.py`).
* **Justificativa:** O sistema precisa de um único ponto de log para registrar eventos que ocorrem em diferentes módulos (como a GUI, a Facade, etc.). Se cada parte do sistema criasse sua própria instância de logger, os registros ficariam espalhados e desordenados. O Singleton garante que todos os componentes acessem e escrevam na *mesma* instância de log, centralizando o registro de atividades.

### Padrão Factory Method (Fábrica) (Criacional)

* **O que é:** Define uma interface para criar um objeto, mas deixa as subclasses (ou, no nosso caso, um método centralizador) decidirem qual classe concreta instanciar.
* **Onde foi aplicado:** Foi utilizado na criação da classe `UsuarioFactory` (no arquivo `src/factories/usuario_factory.py`).
* **Justificativa:** Nosso sistema, conforme os diagramas, precisa lidar com a criação de diferentes tipos de usuários (`Paciente`, `Medico`, `Enfermeiro`). Em vez de espalhar a lógica de `if/else` para instanciar a classe correta em vários pontos do código, a `UsuarioFactory` centraliza essa responsabilidade. O cliente (a Facade) agora só precisa pedir à fábrica um "paciente" ou "medico", sem saber os detalhes de como esses objetos são construídos. Isso diminui o acoplamento e facilita a adição de novos tipos de usuário no futuro.

### Padrão Facade (Fachada) (Estrutural)

* **O que é:** Fornece uma interface unificada e simplificada para um conjunto de interfaces em um subsistema complexo.
* **Onde foi aplicado:** Foi utilizado na criação da classe `CadastroFacade` (no arquivo `src/services/cadastro_facade.py`).
* **Justificativa:** Este é o padrão central da nossa arquitetura de MVP. O processo de cadastro é um subsistema complexo que envolve múltiplos componentes: o `LoggerService`, a `UsuarioFactory` e (futuramente) um `ValidationService` e um `PacienteRepository`. A nossa `gui_app.py` (o cliente) não deve conhecer toda essa complexidade. A `CadastroFacade` age como uma "portaria", fornecendo um único método (`cadastrar_usuario()`) que esconde toda a orquestração interna. Isso **reduz o acoplamento** e torna o código cliente (`gui_app`) muito mais limpo e focado apenas na interface.

## 2. Padrões de Projeto Não Utilizados (Justificativa)

A atividade também pede para justificar por que outros padrões não foram usados. É importante não usar padrões desnecessariamente, o que seria um *overengineering*.

* **Padrão Strategy (Estratégia):**
    * **O que é:** Permite que um algoritmo seja selecionado e trocado em tempo de execução.
    * **Justificativa (Por que não?):** Nosso MVP de *cadastro* possui um fluxo único e linear. Não temos, no momento, diferentes "Estratégias de Cadastro" (por exemplo, "Cadastro Rápido" vs "Cadastro Completo") para escolher. Se essa necessidade surgir, o padrão Strategy será aplicado.

* **Padrão Observer (Observador):**
    * **O que é:** Define uma relação onde um objeto (Sujeito) notifica automaticamente múltiplos outros objetos (Observadores) sobre mudanças de estado.
    * **Justificativa (Por que não?):** O fluxo de cadastro do nosso MVP é síncrono (o usuário clica e espera a resposta). A ação de cadastrar um paciente não precisa "notificar" outras partes do sistema em tempo real. Se, no futuro, tivéssemos um painel de administrador (`Dashboard`) que devesse se atualizar ao vivo com "Novos Pacientes", o padrão Observer seria ideal.

## 3. Conclusão

Os padrões Singleton, Factory e Facade foram escolhidos porque resolviam problemas imediatos e claros no nosso MVP:
1.  **Singleton:** Resolveu o problema de **acesso global** ao log.
2.  **Factory:** Resolveu o problema da **criação de objetos complexos**.
3.  **Facade:** Resolveu o problema de **simplificar um subsistema complexo** para o cliente (a GUI).

A arquitetura resultante segue os princípios de Responsabilidade Única e Baixo Acoplamento.