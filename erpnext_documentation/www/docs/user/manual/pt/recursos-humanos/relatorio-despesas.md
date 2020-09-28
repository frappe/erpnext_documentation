<!-- add-breadcrumbs -->
# Reembolso de Despesas

**Reembolso de Despesas é feito quando funcionarios tem despesas pelo seu bolso em nome da Empresa.**

Por exemplo, se eles levam um cliente a almoçar, eles podem pedir o reembolso via formulario Reembolso de Despesas.

Para aceder o Reembolso de Despesas, vá para:

> Human Resources > Expense Claims > Expense Claim 

## 1. Pre-requisitos

1. [Funcionario](/docs/user/manual/pt/recursos-humanos/funcionario)
1. [Departamento](/docs/user/manual/pt/recursos-humanos/departamento)
1. [Plano de Contas](/docs/user/manual/en/accounts/plano-de-contas)


## 2. Como criar Reembolso de Despesas

1. Vá para: Reembolso de Despesas > Novo.
1. Selecione o Nome do Funcionario no campo 'De Funcionario'.
1. Selecione o Aprovador de Despesas.
1. Digite a Data de Despesa, Tipo de Reembolso de Despesa e o Valor.
1. Adicionalmente, voce pode tambem digitar o Imposto e Taxas de Despesas.
1. Nos Detalhes de Contabilidade, selecionar a conta padrão a Pagar da Empresa.
1. Salvar e Submeter.

<img class="screenshot" alt="Expense Claim" src="{{docs_base_url}}/assets/img/human-resources/expense_claim.png">

Defina o ID do Funcionario, Data, lista de despesas, e impostos correspondentes que serão reembolsados e faça “Submeter .

<img class="screenshot" alt="Expense Claim" src="{{docs_base_url}}/assets/img/human-resources/expense-claim-expenses.png">

Fluxograma Reembolso de Despesas
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/5SZHJF--ZFY?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### Aprovando Despesas

Aprovador para Reembolso de Despesas é selecionado pelo Funcionario. O Funcioario pode escolher da lista de Usuarios que estão configurados como _Aprovadores de Despesas_ para o seu [Departamento](/docs/user/manual/pt/recursos-humanos/departamento).

Depois de salvar o Reembolso de Despesas, o Funcionario deve [Atribuir o Documento para o Aprovador](/docs/user/manual/pt/usando-erpnext/atribuição). Na atribuição, o usuario a aprovar irá receber uma notificação por email. Para automatizar a notificação por email, voce pode configurara o Alerta de Email.

O Aprovador de Reembolso de Despesas pode atualizar o “Valores Sancionados” contra o Valor Reembolsado para um Funcionario. Se ao submeter, o Status de Aprovação deve ser Aprovado ou Rejeitado. Se Aprovado, então o Reembolso de Despesas será submetido. Se rejeitado, então os Comentarios do Aprovador de Despesas podem ser adicionados na secção de Comentarios explicando o porque que foi aprovado ou rejeitado.

### Alocando a Despesa

Ao submeter o Reembolso de Despesas, o sistema aloca a despesa contra a conta de despesas e o valor
<img class="screenshot" alt="Expense Claim" src="{{docs_base_url}}/assets/img/human-resources/expense_claim_book.png">

O Usuario pode verificar despesas não pagas usando o relatorio "Reembolso de Despesas não Reembolsados"
<img class="screenshot" alt="Expense Claim" src="{{docs_base_url}}/assets/img/human-resources/unclaimed_expense_claims.png">

### Pagamento de um Reembolso de Despesas

Para fazer o pagamento contra o Reembolso de Despesas, usuario tem de fazer o clique em Criar > Pagamento.

#### Reembolso de Despesas

<img class="screenshot" alt="Create Payment" src="{{ docs_base_url }}/assets/img/human-resources/expense_claim_create_payment.png">

#### Registo de Pagamento

> Nota: Este valor deve não deve ser associado como Salario porque o valor será feito o imposto depois para o Funcionario.

<img class="screenshot" alt="Expense Claim" src="{{docs_base_url}}/assets/img/human-resources/expense_claim_payment_entry.png">

Alternativamente, o Registo de Pagamento pode ser feito para um funcionario e todas as suas despesas de reembolso em falta serão inseridas.

> Contabilidade > Registo de Pagamento > Novo Registo de Pagamento

Defina o Tipo de Pagamento para "Pagar", o Tipo de Parte para Funcionario, a Parte em que o funcionario está a ser pago e a conta de onde esta a ser pago. Todos os reembolsos de despesa em falta serão inseridos e os valores de pagamento podem ser alocados para cada despesa.

### Ligando com a Tarefa e Projeto

* Para Ligar Reembolso de Despesas com Tarefas ou Projeto especifique a Tarefa ou o Projeto quando estiver a criar o Reembolso de Despesas

<img class="screenshot" alt="Expense Claim - Project Link" src="{{docs_base_url}}/assets/img/project/project-expense-claim-1.png">

Este irá atualizar o custo do Projeto com os valores do Reembolso de Despesas

<img class="screenshot" alt="Expense Claim - Project Link" src="{{docs_base_url}}/assets/img/project/project-expense-claim-2.png">

{next}
