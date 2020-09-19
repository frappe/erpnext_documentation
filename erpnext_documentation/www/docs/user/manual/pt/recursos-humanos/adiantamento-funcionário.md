<!-- add-breadcrumbs -->
# Adiantamento a Funcionário

**Algumas vezes os funcionários vão para fora a trabalho pela empresa e a empresa paga algum valor para as suas despesas adiantada. Isto é quando o Funcionário pode criar o formulario de Adiantamento a Funcionário aonde detalhes como o Motivo da Despesa e o Valor da Despesa pode ser registado.**

Uma o Adiantamento a Funcionário feito pelo Funcionário, o Aprovador de Despesas pode submeter o registo após validação. Depois do formulario submtedio, a contabilidade libera o pagamento e faz um Registo de Pagamento.

Para aceder ao Adiantamento a Funcionário, vá para:

> Recursos Humanos > Reembolsos de Despesas > Relatorio de Despesas

## 1. Pre-requisitos

1. [Funcionáro](/docs/user/manual/pt/recursos-humanos/funcioário)
1. [Departamento](/docs/user/manual/pt/recursos-humanos/departamento)
1. [Plano de Contas](/docs/user/manual/pt/contabilidade/plano-de-contas)

## 2. Como criar um Adiantamento a Funcionário
1. Vá para: Adiantamento a Funcionário > Novo.
1. Selecion o Funcionário par quem voçê precisa fazer o adiantamento.
1. Digite o Motivo e o Valor do Adiantamento.
1. Selecion a Conta do Adiatamento e o Modo do Pagamento.
1. Salvar.

    <img class="screenshot" alt="Expense Claim" src="{{docs_base_url}}/assets/img/human-resources/employee-advance.png">

> Nota: O Funcionário pode somente Salvar o Adiantamento a Funcionário mas não pode Submeter. Somente o Aprovador de Despesas o pode.

## 3. Funcionalidade

### 3.1 Submissão do Adiantamento a Funcionário

O registo do Adiantamento a Funcionário pode ser criado por qualquer funcionário mas não o podem submeter.

Depois de salvo, o Funcionário deve [Atribuir o documento ao Aprovador](/docs/user/manual/pt/usando-erpnext/atribuição). Na atribuição, o usuário aprovador irá receber uma notificação por email. Para automatizar a notificação do email, voçê pode configurar [Alerta de Email](/docs/user/manual/pt/configuração/notificações.html).

Depois da verificação, o Aprovador de Despesas pode Submeter (Aceitar) o formulario de Adiantamento a Funcionário ou Rejeitar o pedido.

### 3.2 Fazer o Registo de Pagamento

##### Adiantamento a Funcionário via Registo de Pagamento
Depois da submissão do registo, o contabilista irá poder criar um [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento) usando o botão 'Criar'.

O Registo de Pagamento ficará assim:

<img class="screenshot" alt="Employee Advance Payment via Payment Entry" src="{{docs_base_url}}/assets/img/human-resources/employee-advance-payment-entry.png">

#### Adiantamento a Funcionário via Lançamento Contabilistico
Alternativamente, um [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico) pode tambem ser criado contra o Adiantamento a Funcionário.


<img class="screenshot" alt="Employee Advance Payment via Journal Entry" src="{{docs_base_url}}/assets/img/human-resources/employee-advance-journal-entry1.png">

> Nota: Tenha a certeza que o Tipo de Parte selecionado seja Funcionário e o Tipo de Referencia seja Adiantamento a Funcionário

<img class="screenshot" alt="Employee Advance Payment via Journal Entry" src="{{docs_base_url}}/assets/img/human-resources/employee-advance-journal-entry2.png">

#### Adiantamento a Funcionário está Pago
Ao submter o Registo de Pagamento/Lançamento Contabilistico, o valor pago e o staus será actualizado no registo Adiantamento a Funcionário.

### 3.3 Ajustar Adiantamentos em Reembolso de Despesas

Depois do funcionário fizer o Relatorio de Despesas, um registo de adiantamento pode inserido no [Relatorio de Despesas](/docs/user/manual/pt/human-resources/relatorio-despesas) e ligar ao registo.


### 3.4 Valor Devolvido
Quando o adiantamento foi pago ao Funcionário, existem três situações:

* O valor pode não ter sido usado
* Foi usado todo por completo
* Foi usado uma parte


Crie um Adiantamento a Funcionário, crie o registo de pagamento para indicar que o valor esta pago. 

* SE o valor for não usado, clique no botão **Retorno** para retornar o valor do Adiantamento pago
    ![Botão Retornar](/docs/assets/img/human-resources/advance-return-button.png)
* Se todo o adiantamento foi usado, irá reflectir no campo do Valor Reportado
* Se algum foi usado e o resto devolvido, o valor devolvido irá aparecer no campo 'Valor Devolvido'.
    ![Devolver Valor adiantamento](/docs/assets/img/human-resources/advance-returned-amount.png)

## 4. Topicos Relacionados

1. [Relatorio de Despesas](/docs/user/manual/pt/human-resources/relatorio-despesas)



{next}
