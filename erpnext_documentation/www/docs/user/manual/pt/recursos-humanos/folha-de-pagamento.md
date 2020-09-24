<!-- add-breadcrumbs -->
# Entrada de Folha de Pagamento

**Folha de Pagamento é a soma total de todas as compensações que um negocio deve pagar aos seu funcionarios por uma periodo de horas ou dias.**

No ERPNext, Entrada de Folha de Pagamento possibilita o processamento em massa de funcionarios. Em outras palavras, processar recibo de salario para todos os funcionarios de uma só vez. O processamento em massa pode ser para empresa completa ou com base nas seguintes categorias: Filiais, Departamentos ou Designações. 

Para aceder a Entrada de Folha de Pagamento, vá para:

> Home > Recursos Humanos > Folha de Pagamento > Entrada de Folha de Pagamento



## 1. Como criar uma Entrada de Folha de Pagamento


1. Vá para a lista de Entrada de Folha de Pagamento, clique em Novo.
1. Selecione a Frequencia de Pagamento.
1. Selecione a Filial, Designação e Departamento para filtrar os funcionarios (opcional).
1. Selecione Projeto (opcional) se voce quer correr contra um projecto.
1. Selcione 'Validar Assiduidade' e 'Recibo de Salario com base no Timesheet' caso queira deduzir o salario com base na assiduidade e se voce quer considerar os timesheets dos funcionarios.
1. Selecione a Conta de Pagamento para criar o Registo Bancário.
1. Salvar.


Uma vez a informação salva. Clique no botão **Obter Funcionários** para obter a lista de Funcionarios para o qual o Recibo de Salario será criado com base nos criterios selecionados.

Uma vez a Lista de Funcionarios inserida, clique no botão **Criar Recibos de Salario** para gerar os Recibos de Salario.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-entry-get-employees.png">

> **Nota:** Se os Recibos de Salario já foram criados, o sistema não irá criar novamente os recibos. Voce pode salvar o formulario em rascunho e criar os Recibos de Salario depois.


## 2. Funcionalidades

### 2.1 Accrual do Salario

Depois de verificar os Recibos de Salario, voce pode submeter todos de uma só vez fazendo o clique no botão **Submeter Recibos de Salario**.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-entry.png">

Este irá tambem alocal nas contas Padrão a Pagar da Contabilidade contra as respectivas contas de despesas (como configuradas nos Componentes de Salario) para registar o accrual dos salarios dos funcionarios.

**Centro de Custo:**
Voce pode selecionar o Centro de Custo na Entrada de Folha de Pagamento contra as despesas no qual serão criadas.

Se voce quiser alocar despesas contra varios centros de custo com base no Funcionario/Departamento, voce pode fazer configurando o Centro de Custo na ficha do Funcionario/Departamento. Centro de Custo atribuido ao Funcionario/Departamenteo irá ter prioridade em relação ao Centro de Custo selecionado na Entrada de Folha de Pagamento.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-make-accrual-entry.png">

> **Nota:** Submetendo Recibos de Salario um por um manualmente não irá criar o Lançamento Contabilistico para o registo do accrual do Salario.

### 2.2 Pagamento do Salario

O passo final é alocar o Pagamento do Salario.

Salarios no negocioas são normalmente geridos com extram privacidade. Em muito dos casos, as empresa fazem um unico pagamento ao Banco combinando todos os salarios e o Banco faz a ditribuição para cada conta de salario dos Funcionarios. 

Desta forma somente tera uma registo de pagamento nas contas da empresa e qualquer com acesso não irá ver os valores individuais .

O registo de pagamento de salario é um Lançamento Contabilistico que debita o total de Remunerações e credita o total de Deduções para todos os Funcionarios para a conta padrão definida em cada componente de salario.

Para gerar o seu registo de pagamento de salario a partir da Entrada da Folha de Pagamento, clique no botão **Criar Lançamento Bancário / Make Bank Entry**.

Registo de Pagamento irá reenviar para o Lançamento Contabilístico com os filtros necessarios para visualizar em rascunho o Jornal criado. Voce irá ter de definir o Numero de Referencia e Data para as transações e Submeter o Lançamento Contabilístico.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-make-bank-entry.png">

> **Nota:** Para os Componentes de Salario no qual são Beneficios Flexivies e tem selecionado _Criar Pagamento Separado contra a Reivindicação de Benefícios_, o ERPNext irá alocar Registos de Jornal separados.


## 3. Topicos Relacionados

1. [Componente de Salario](/docs/user/manual/pt/recursos-humanos/componente-de-salário)
1. [Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/estrutura-salário)
1. [Periodo da Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/periodo-folha-de-pagamento)
1. [Lançamento Contabilístico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)

{next}
