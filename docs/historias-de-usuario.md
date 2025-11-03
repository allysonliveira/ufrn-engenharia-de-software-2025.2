# Histórias de Usuário - Meu Posto de Saúde

Este documento detalha as Histórias de Usuário (User Stories) do projeto, com os campos necessários para o planejamento e desenvolvimento.

---

Legenda: [AC1] = Critério de Aceitação 1; [AC2] = Critério de Aceitação 2; ... [ACT7] = Critério de Aceitação 7.

### História 1 – Cadastro de Paciente

* **Descrição:** Como paciente do posto de saúde, quero realizar meu cadastro online informando dados pessoais e cartão do SUS, para que eu possa agendar consultas e acessar meu histórico médico.
* **Prioridade:** Alta
* **Estimativa:** 5 Pontos
* **Critérios de Aceitação:**
    * [AC1] Dado que o usuário não está logado, ele deve poder acessar uma página/formulário de "Cadastro de Paciente".
    * [AC2] O formulário deve conter os campos: "Nome Completo", "CPF", "Data de Nascimento" e "Cartão do SUS".
    * [AC3] O sistema deve validar que todos os campos são obrigatórios.
    * [AC4] O sistema deve validar se o CPF e o Cartão do SUS já não existem no banco de dados.
    * [AC5] Ao submeter o formulário com dados válidos, um novo registro de "Paciente" deve ser criado no sistema.
    * [AC6] O usuário deve receber uma mensagem de "Cadastro realizado com sucesso".
    * [AC7] Se houver um erro de validação (ex: CPF duplicado), o usuário deve receber uma mensagem de erro clara.

---

### História 2 – Agendamento de Consulta

* **Descrição:** Como paciente do posto de saúde, quero agendar uma consulta escolhendo especialidade, médico e horário disponíveis, para que eu possa garantir meu atendimento de forma organizada.
* **Prioridade:** Alta
* **Estimativa:** 8 Pontos
* **Critérios de Aceitação:**
    * [AC1] O usuário deve estar logado como "Paciente" para acessar a tela de agendamento.
    * [AC2] O sistema deve exibir uma lista de "Especialidades" disponíveis no posto de saúde.
    * [AC3] Ao selecionar uma especialidade, o sistema deve exibir a lista de "Médicos" daquela especialidade.
    * [AC4] Ao selecionar um médico, o sistema deve exibir um calendário com os "Horários disponíveis" (dias e horas) daquele médico.
    * [AC5] O paciente deve poder selecionar um horário e clicar em "Confirmar Agendamento".
    * [AC6] Após a confirmação, o agendamento deve ser salvo no sistema, e aquele horário deve ficar indisponível para outros pacientes.
    * [AC7] O paciente deve receber uma mensagem de "Consulta agendada com sucesso".

---

### História 3 – Emissão de Receita Médica

* **Descrição:** Como médico do posto de saúde, quero emitir e salvar receitas médicas digitais vinculadas ao prontuário do paciente, para que o paciente e a farmácia do posto possam acessá-las de forma rápida e segura.
* **Prioridade:** Alta
* **Estimativa:** 5 Pontos
* **Critérios de Aceitação:**
    * [AC1] O usuário deve estar logado como "Médico".
    * [AC2] O médico deve poder buscar um paciente (por Nome ou CPF) para quem a receita será emitida.
    * [AC3] O sistema deve exibir um formulário para a receita com campos para "Medicamentos", "Dosagem" e "Observações".
    * [AC4] Ao salvar, a receita deve ser registrada no banco de dados.
    * [AC5] A receita salva deve ser automaticamente vinculada ao "Prontuário" do paciente selecionado.
    * [AC6] O médico deve receber uma mensagem de "Receita emitida com sucesso".
    * [AC7] (Opcional) O paciente deve poder visualizar a nova receita em seu histórico.

---