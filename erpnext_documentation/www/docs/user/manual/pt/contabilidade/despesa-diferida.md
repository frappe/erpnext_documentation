# Despesa Diferida

**Despesa Diferida é um custo que já ocorreu, mas que ainda não consumido.**

O custo é gravado como um Activo por um periodo até que o bem ou serviço seja utilizado; nesta altura, o custo é carregado para despesas. Uma Despesa Diferida é inicialmente registada como um activo, para que apareça na folha de Balanço (normalmente como um Activo Corrente, vendo que não utilizado até o momento e irá provavelmente ser consumido dentro de um ano).

## 1. Como utilizar uma Despesa Diferida

Como um exemplo de Despesa Diferida, a Unico Plastics paga $10,000 em Abril a sua renda de Maio. É deferido o custo nessa altura do pagamento (em Abril) na conta pre-paga da renda do activo. Em Maio, Unico Plastics já consumiu o activo pre-pago, então é creditado o pre-pagamento da renda na conta de activos e debitado na conta de renda das despesas.

Outros exemplos de Despesa Diferida são:

* Custos Interest que são capitalizados como parte de um activo fixo pelo qual os custos incorreram
* Seguro pado em adiantado para cobrir meses futuros
* O custo do activo fixo que foi cobrado para despesa durante o seu periodo de vida em forma de depreciação
* O custo incorrido para registar o issuance de um instrumento de debito
* O custo de um activo intangible que foi cobrado para despesa durante o seu periodo de via é amortizado
* Para uma Subscrição de Internet, o valor é pago antecipadamente e o serviço entregue mensalmente. Portanto é uma Despesa Diferida para o Cliente.

De seguida está a configuração da conta de Despesas Diferida no ERPNext para automatizar o processo.

### 1.1 Item

Na ficha do Item, em baixo da secção de Despesa Diferida, selecione o campo **Activar Despesa Diferida**. Neste secção, voçê pode selecionar uma conta Despesa Diferida (Conta de Activos, de preferencia Activo Corrente) para este item em particula e o numero de meses.

<img class="screenshot" alt="Item - Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/deferred-item-expense.png">


### 1.2 Factura de Compras

Ao criar uma Factura de Compras para um Item de Despesa Diferida, em vez de postar na Conta de Despesas, a Conta Despesa Diferida (Conta de Activo) é Creditada pelo valor da compra. Vamos considerar um exemplo simples de uma Subscrição de Internet:

<img class="screenshot" alt="Item - Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/deferred-purchase-invoice.gif">

### 1.3 Lançamento Contabilistico

Baseado na Data de Inicio e Fim definido na tabela do Item da Factura de Compra, Lançamento Contabilistico é criado automaticamente no fim de mês. Debita o valor da conta Despesa Diferida e credita na conta de Despesa selecionada para um Item na Factura de Compras. 


{next}
