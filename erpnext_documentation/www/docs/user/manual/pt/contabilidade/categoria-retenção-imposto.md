<!-- add-breadcrumbs -->
# Categoria de Retenção de Imposto

**Categoria de Retenção de Imposto é o Imposto Deduzido na Fonte.**

Assim sendo, uma pessoa responsavel por fazer pagamentos deve deduzir o imposta afonte a taxa pre-estabelecida. Em vez de receber o imposto nos seus lucros apartir de si num periodo mais tarde, o governos quer que os contribuintes façam a dedução antecipada e o seu deposito no governo.

Para aceder a lista de Categoria de Retenção de Imposto, deve ir:
> Home > Contabilidaed > Impostos > Categoria de Retenção de Imposto

## 1. Pre-requisitos
Antes de criar e utilizar a Categoria de Retenção de Imposto, é aconselhavel criar o seguinte primeiro:
1. [Fornecedor](/docs/user/manual/pt/comprar/fornecedor)

## 2. Como criar uma Categoria de Retenção de Imposto
No ERPNext, as Categorias de Retenção de Imposto normalmente estão disponveis por defeito, contudo, voçê pode criar mais se necessário.

1. Ir para a lista de Categoria de Retenção de Imposto e click em Novo.
1. Digite um nome unico, eg: Secção 194C Indiviual.
1. Digite o Nome da Categoria (Dividendos, Taxas Profissional, etc,.).
1. Digite a Percentagem da Retenção do Imposto para o [Ano Fiscal](/docs/user/manual/pt/contabilidade/ano-fiscal).
1. Voçê pode definir o limite para uma unica factura ou para a soma de varias facturas.
1. Selecionar a conta a favor a sua Empresa para o qual o Imposto será creditado.
1. Adicione mais empresas e contas caso necessário.
1. Salvar.

 ![Categoria de Retenção de Imposto](/docs/assets/img/accounts/tax-withholding-category.png)

De baixo dos detalhes de contas, a conta TDS é adicionada para cada Empresa no sistema.

### 2.1 Atribuindo Rentenção de Imposto a um Fornecedor

Depois de salvar, pode ser atribuido a um Fornecedor:
<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-1.png">

### 2.2 Como funciona o threshold?
Considere um Fornecedor a quem a Categoria de Retenção de Imposto é aplicada.

Por exemplo, digamos que a percentagem de 5% será aplicada na factura aonde o thresfold Singular é de 20,000 e o threshold Acumulado é de 30,000. Caso a factura seja criada com o valor total de 20,000 então o threshold singular será activado e a percentagem de 5% será cobrada.

But if the invoice amount totaled up to be 15,000 then no tax will be charged as it didn't cross the threshold. If again another invoice is created against the same supplier with a total of 15,000 then although it didn't cross the Single threshold, charges will be deducted since the sum of the last invoice and this invoice adds up to be 30,000 which is equal to the specified Cumulative threshold.

## 3. Using Tax Withholding
### 3.1 Use in Purchase Invoice
In the following example, we have selected 'TDS - 194C - Individual' which has a single threshold of 30,000, cumulative threshold of 1,00,000 and rate of 1%.

1. If the **Supplier** has the tax withholding field set, then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not.

 <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-2.png">

1. Let's create an invoice for 90,000. Saving the invoice automatically calculates tax and appends it in the taxes table.

 <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-6.png">

1. To see the effect of Cumulative threshold, let's create an invoice with of amount 20,000 and submit it. 

 <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-8.png">

 Although the invoice amount didn't cross the Single threshold (30,000), we see that tax has been charged. This is because the previous and the current invoice adds up to be 1,10,000 which exceeds the Cumulative threshold. Hence, tax based on the rate provided in the **Tax Withholding Category** is applied accordingly.

> Note: On submitting the invoice, three GL Entries are created:

>1. First for debit from the expense head
>1. Second for credit in Creditors account
>1. Third for credit in the account selected in Tax Withholding Category.

![Tax Withholding Ledger](/docs/assets/img/accounts/tax-withholding-ledger.png)

### 4. Related Topics
1. [Tax Rule](/docs/user/manual/pt/accounts/tax-rule)
1. [Supplier](/docs/user/manual/pt/comprar/supplier)