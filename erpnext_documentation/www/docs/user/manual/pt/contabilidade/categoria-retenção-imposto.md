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

Mas se o valor da factura totalizasse até 15,000 então não seria aplicado o Imposto vendo que não passou o limite threshold. Caso uma outra factura seja criada para o mesmo fornecedor com o mesmo total de 15,000 então apesar de não ter ultrapassado o limite Singular threshold, será aplicada a dedução vendo que a soma da ultima factura e a corrente dá 30,000 que é igual ao Limite Acumulado especificado.

## 3. Usando Retenção de Impostos
### 3.1 Usar em Facturas de Compra
No exemplo seguinte, nós selecionamos 'TDS - 194C - Individual' que tem um unico limite singular de 30,000, limite acumulado de 1,00,000 e a percentagem de 1%.

1. Caso o **Fornecedor** tenha o campo de retenção de imposto activo, então após selecionar o Fornecedor, uma caixa ficará visivel na Factura de Compra para selcionar se quer aplicar ou nao o Imposto.

 <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-2.png">

1. Vamos criar uma factura no valor de 90,000. Salvando a factura automaticamente o imposto é calculado e aodicionado a tabela de impostos.

 <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-6.png">

1. Para ver o efeito do Limite Acumulado, vamos criar uma factura com o valor de 20,000 e submeter. 

 <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-8.png">

 Apesar do valor da factura não ter ultrapassado o limite Singular (30,000), nós vemos que o imposto foi cobrado. Isto porque a factura anterior e a corrente somão mais de 1,10,000 que excede o Limite Acumulado. Daí, o imposto baseado na percentagem criada na  **Categoria de Retenção de Imposto** é aplicada de acordo.

> Nota: Ao submeter a factura, três entradas no GL são criadas:

>1. Primeiro para debito da conta de despesas
>1. Segundo para credito na conta de Credores
>1. Terçeiro para credito na conta selecionada na Categoria de Retenção de Imposto.

![Razão Retenção Imposto](/docs/assets/img/accounts/tax-withholding-ledger.png)

### 4. Topicos Relacionados
1. [Regra de Imposto](/docs/user/manual/pt/contabilidade/regra-imposto)
1. [Fornecedor](/docs/user/manual/pt/comprar/fornecedor)