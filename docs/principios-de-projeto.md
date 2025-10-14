# Relatório de Aplicação dos Princípios de Projeto - Meu Posto de Saúde

[cite_start]Este documento descreve como os princípios de projeto de software, baseados no material de aula[cite: 1], serão aplicados no desenvolvimento do sistema "Meu Posto de Saúde". A aplicação desses princípios visa garantir um código mais robusto, manutenível e extensível.

## Propriedades de Projeto Fundamentais

### 1. Integridade Conceitual

[cite_start]A integridade conceitual é a consideração mais importante no projeto de sistemas[cite: 160]. Para nosso projeto, isso significa manter a consistência em todas as partes do sistema.

* **Aplicação Prática:**
    * **Interface com o Usuário:** Todos os formulários (Cadastro de Paciente, Login, Agendamento de Consulta) seguirão o mesmo padrão de design. [cite_start]Botões de "Salvar" ou "Cancelar" terão a mesma aparência e posição em todas as telas[cite: 152].
    * [cite_start]**Código:** Adotaremos um padrão de nomenclatura consistente para variáveis, funções e classes (ex: `camelCase` para variáveis e `PascalCase` para classes)[cite: 157]. As rotas da nossa API seguirão um padrão RESTful claro (ex: `/pacientes`, `/consultas`).

### 2. Ocultamento de Informação (Encapsulamento)

[cite_start]Classes devem ocultar detalhes internos de implementação, expondo apenas uma interface pública estável[cite: 295, 298]. Isso permite que a implementação interna de uma classe mude sem quebrar o código que a utiliza.

* **Aplicação Prática:**
    * A classe `Paciente` terá seus atributos (`cpf`, `cartaoSUS`, etc.) definidos como `private`. O acesso e a modificação desses dados serão feitos através de métodos públicos (ex: `getCPF()`, `validarCPF()`). Dessa forma, a lógica de validação de um CPF, por exemplo, fica "escondida" e centralizada dentro da própria classe `Paciente`, e não exposta para quem a utiliza.

### 3. Coesão (Princípio da Responsabilidade Única - SRP)

[cite_start]Uma classe deve ter uma única função ou responsabilidade[cite: 368, 560]. Isso torna as classes mais fáceis de entender, testar e manter.

* **Aplicação Prática:**
    * [cite_start]Seguindo o exemplo da aula que separa a lógica de negócio da apresentação[cite: 584, 610], não colocaremos a lógica para salvar um agendamento no banco de dados dentro da mesma classe que desenha a tela de agendamento. Teremos classes com responsabilidades distintas:
        * `AgendamentoController`: Responsável por receber os dados da interface web.
        * `AgendamentoService`: Responsável pelas regras de negócio (verificar se o horário está disponível, validar os dados da consulta).
        * `AgendamentoRepository`: Responsável por interagir com o banco de dados (salvar, buscar, deletar agendamentos).

### 4. Acoplamento (Princípio da Inversão de Dependências - DIP)

[cite_start]Devemos minimizar o acoplamento ruim, fazendo com que as classes dependam de abstrações (interfaces) e não de implementações concretas[cite: 510, 653].

* **Aplicação Prática:**
    * Imagine que, após um agendamento de consulta, o sistema precise notificar o paciente. Hoje, a notificação pode ser por e-mail, mas no futuro, pode ser por SMS ou WhatsApp.
    * Em vez de a classe `AgendamentoService` depender diretamente de uma classe `EmailNotificador`, ela dependerá de uma interface `INotificador`. Teremos então classes como `EmailNotificador` e `SMSNotificador` que implementam essa interface.
    * [cite_start]Isso nos permite trocar a forma de notificação sem alterar o código da `AgendamentoService`, tornando o sistema flexível e de baixo acoplamento, como no exemplo do `ControleRemoto` e `TVGenerica` dos slides[cite: 666, 686].

## Conclusão

A adoção consciente desses princípios desde o início do projeto "Meu Posto de Saúde" será fundamental para evitar a complexidade acidental e garantir que o software possa crescer e se adaptar a novas necessidades no futuro com menor esforço e maior qualidade.git