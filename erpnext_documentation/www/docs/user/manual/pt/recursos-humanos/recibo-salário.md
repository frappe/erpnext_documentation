<!-- add-breadcrumbs -->
# Recibo de Salário

**Um  Recibo de Salário é um documento gerado para um funcionario. Contem uma descrição detalhada dos componentes de salario e valores.**

Para aceder Recibo de Salário, vá para:
> Home > Recursos Humanos > Folha de Pagamento > Recibo de Salário

## 1. Pre-requisitos
Antes de criar Recibo de Salário, é aconselhavel criar estes:

* [Funcionario](/docs/user/manual/pt/recursos-humanos/funcionario)
* [Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/estrutura-salário)
* [Atribuição de Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/atribuição-estrutura-salário)

## 2. Como criar um Recibo de Salário


1. Vá para Recibo de Salário, clique em Novo.
1. Selecion o Funcionario. Ao selecionar o Funcionario todos os detalhes do Funcionario serão inseridos a partir da Estrutura de Salario no qual foi atribuido. Isto incluid detalhes como Frequencia de Processamento, Remunerações, Deduções, etc.
1. Selecione a Data de Inicio e Fim.
1. Salvar.

## 3. Funcionalidades

### 3.1. Recibo de Salário com base na Assiduidade/Licença

Usuarios do RH podem criar Recibo de Salário com base na Assiduidade ou Licença.
Os dias Trabalhados serão calculados com base da Licença/Assiduidade, dependendo do campo **Calcular Dias de Trabalho Com Base em** nas [Configurações do RH](/docs/user/manual/pt/recursos-humanos/configuração-recursos-humanos). Se a Folha de Pagamento for com base em Assiduidade então, o **Licença sem pagamento** será considerado como ausencia e **meio-dia** irá ser considerado como meio-dia de ausencia.

### 3.2. Recibo de Salário com base em Timesheet

Para criar Recibo de Salário como base em timesheet voce precisa criar a Estrutura de Salario para Timesheets.

O ERPNext tambem providencia uma opção para criar os Recibos de Salário com base em Horas Trabalhadas [Timesheet](/docs/user/manual/pt/projectos/timesheets).
Voce pode criar Recibo de Salario depois de submeter a Timesheet fazendo o clique directamente no botão **Criar Recibo de Salario** no topo a direita.

<img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/assets/img/human-resources/create-salary-slip-based-on-timesheets.png">

O Valor de Pagamento é calculado com base na Taxa Hora definida na Estrutura de Salario e é reflectida na tabela de Remunerações.

