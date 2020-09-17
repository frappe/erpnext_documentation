<!-- add-breadcrumbs -->
# Categoria de Impostos e Taxas para Compras

Considere que o campo Impostos ou Taxas em Compras Impostos e Taxas tenha trê valores.

- Total
- Avaliação
- Total e Avaliação

<img alt="Purchase Tax and Charges Categories" class="screenshot" src="{{docs_base_url}}/assets/img/articles/purchase-other-charges-1.png">

Vamos considerar o exemplo para entender o efeito do tipo de cada taxa. Vamos comprar dez unidades de um item, ao preço de 800. Valor total da compra é de 800. Itens comprados tem IVA de 4%, e INR 100 de taxa de transporte.

####Total:

Imposto ou Taxas categorizadas como **Total** será incluido no total das transações de compra. Mas não terá impacto no preço de Avaliação do item comprado.

Se o IVA 4% é aplicado a um item, terá uma valor de INR 32 (o preço base de 800). Então o IVA é a taxa de consumo, dever ser valor adicionado da Ordem de Compra/Factura, vendo que será incluido nos a pagar para o fornecedor. Mas não deve ser adicionado ao valor do item comprado.

Quando uma Factura de Compra é submetida, o razão geral postado sera feito para categorizar o Total do Imposto/Taxa.

####Avaliação:

Imposto ou Taxa categorizada como **Avaliação** será adicionada ao valor do item comprado, mas não no total da transação da compra.

Taxas de transporte de INR 100 deve ser categorizado como avaliação. Com isto, o valor do item comprado irá aumentar de 800 para 900. Tambem, a taxa não será adiconada ao total das transações da compra, porque a sua despesa, não deve ser reflectida ao fornecedor.

Verique [aqui](/docs/user/manual/pt/inventario/perpetual-inventory) para aprender sobre despesa categorizada como Avaliação.

####Total e Avaliação:

Imposto ou Taxa categorizadas como **Total e Avaliação** será adicionada a avaliação do item, vem como nos totais de transação de compras.

Vamos assumir que o transporte foi arranjado pelo fornecedor, mas nós precisamos pagar as taxas a eles. Neste caso, taxa de transporte, categoria selecionada deve ser Total e Avaliação. Com isto,  INR 100 taxa de transporte será adiconado ao valor da compra de 800. Tambem, INR 100 irá reflectir no total, como será a pagar para nós para com o fornecedor.

{next}
