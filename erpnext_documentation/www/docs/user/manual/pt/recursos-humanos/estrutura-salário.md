<!-- add-breadcrumbs -->
# Estrutura de Salário

**Estrutura de Salário são os detalhes dos salarios oferecidos a um Funcionario, dos diferentes componentes que constituem a sua compensação.**

Qualquer alteração a Estrutura de Salário i.e. entre os componentes pode ter grande impacto no que o Funcionario faz, como as Isenções Reivindicadas de Impostos.

O ERPNext permite que voce defina as Remunerações e Deduções de uma Estrutura de Salario, Frequencia do Processamento, Modo do Pagamento e outras funcionalidades.

Para aceder a Estrutura de Salário, vá para:
> Home > Recursos Humanos > Folha de Pagamento > Estrutura de Salário


## 1. Pre-requisitos

Antes de voce criar a Estrutura de Salário, é aconselhavel ter os seguintes:

* [Componentes de Salario](/docs/user/manual/pt/recursos-humanos/componente-de-salário)


## 2. Como criar uma Estrutura de Salário

1. Vá para a lista de Estrutura de Salário, clique em Novo.
2. Digite o Nome da Estrutura de Salário.
3. Selecione o Nome da Empresa e a Frequencia do Processamento.
3. Salvar e Submeter.


## 2. Funcionalidades

### 2.1 Remunerações e Deduções

Remunerações especificam Componentes de Salario que são ganhos pelo Funcionario. Estas componentes tipicamente incluem base, premios, bonus e incentivos que são adicionados ao Total do Salario. Nisto, Deduções especificam os Componentes de Salario que são deduzidos do Total do Salario do Funcionario. Normalmente inclui Impostos.

>**Nota:** Somente os Componente de Salario definidos como 'Remunerações' são mostrados na tabela Remunerações e componentes definidos como 'Deduções' na tabela de Deduções.


Para criar Remunerações e Deduções, selecione o Componente de Salario na coluna de Componentes. Digite a Formula/Condição se não foi especificado ao criar o [Componente de Salario](/docs/user/manual/pt/recursos-humanos/componente-de-salário). Adicionalmente, voce pode tambem digitar o valor pre-definido na coluna Valor.



<img class="screenshot" alt="Salary Structure" src="{{docs_base_url}}/assets/img/human-resources/salary-structure.png">


> **Nota:** Tenha a certeza de fazer o clique em ceta para baixo e activar a caixa 'Valor com base na Formula' no caso do componente de salario for calculado usando uma formula.


### 2.2 Conta

Nesta secção, o [Modo de Pagamento](/docs/user/manual/pt/contabilidade/modo-de-pagamento) e [Conta de Pagamento](/docs/user/manual/pt/contabilidade/plano-de-contas) é usado para pagar o salario pode ser especificado.

### 2.3 Estrutura de Salario para Salario com base em Timesheets

No ERPNext voce pode definir a Estrutura de Salario para o Recibo de Salario com base no Timesheet, no qual permite a Empresa pagar os Funcionarios por Horas trabalhadas.

Passos para criar a Estrutura de Salario com base em Timesheets:

1. Vá para a lista de Estrutura de Salario, cliquem em Novo.
1. Selecione a caixa **Recibo de Salario com base em Timesheet**.
1. Digite o Componente de Salario. 
1. Digite o Valor Hora. Com base no valor digitado, o valor para horas de trabalho para o Componente de Salario selecionado será calculado de acordo.
1. Salvar e Submeter.

 <img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/assets/img/human-resources/salary-structure-for-salary-based-on-timesheets.png">


### 2.4 Licença com Subsidio de Pagamento Por Dia

Caso exista Licenças com Subsidio de Pagamento para um Funcionario, voce pode definiar o valor da licença / Subsidio de licença por dia nesta campo para esta estrutura de salario em particular. Com base na definição 'Componente de Remuneração' no [Tipo de Licença](/docs/user/manual/pt/recursos-humanos/tipo-de-licença) e o valor por dia, o valor do componente de salario será calculado de acordo no recibo de salario.


### 2.5 Maximo de Beneficios (Valor)

Neste campo, o Valor Maximo de Beneficios para a Estrutura de Salario pode ser especificado. Se este campo for preenchido, tenha a certeza que a Estrutura de Salario tenha na [Componente de Salario](/docs/user/manual/pt/recursos-humanos/componente-de-salário) "É Beneficio Flexivel" activo, contra o qual este valor será pago.



Uma vez toda a informação preenchida e salva e submetida, voce pode atribuir a Estrutura de Salario a um Funcionario pelo Botão **Atribuir Estrutura de Salario** ou criando uma nova [Atribuição de Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/atribuição-estrutura-salário) pelo dashboard.

Voce pode tambem atribuir a Estrutura de Salario criad para varios funcionarios com no [Grau do Funcionario](/docs/user/manual/pt/recursos-humanos/grau-funcionario), [Departamento](/docs/user/manual/pt/recursos-humanos/departamento), [Designação](/docs/user/manual/pt/recursos-humanos/designação), etc. pelo botão 'Atribuir a Funcionarios'.
Adicionalmente, o Recibo de Salario pode ser criado directamente pelo dashboard.

## 3. Topicos Relacionados

1. [Componente de Salario](/docs/user/manual/pt/recursos-humanos/componente-de-salário)
1. [Atribuição da Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/atribuição-estrutura-salário)
1. [Entrada da Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento)
