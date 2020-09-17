<!-- add-breadcrumbs -->
# Gerir a Diferença de Cambio de Moedas

No ERPNext, voçẽ pode gerir transações em moeda estrangeira tambem. Quando criar uma transação em moeda estrangeira, o sistema actualiza a taxa de cambio com a moeda do respectivo cliente/fornecedor e a moeda base da empresa. Vendo que a taxa de cambio esta sempre a mudar, pode receber um pagamento de um cliente num cambio diferente do que foi mencionado na factura de Vendas/Compras. De seguidas as instruções de como gerir valores diferentes no registo de pagamento devido a taxa de cambio.

#### Adicione Conta de Despesa

Para gerir a diferença de moeda, crie a Conta **Moeda Estrangeira Ganho/Perda**. Esta conta é geralmente criada no extracto de Despesas ao lado P&L. Contudo, voçê pode posicionar em qualquer grupo de acordo o requesito de contabildade.

<img alt="Accounts Frozen Date" class="screenshot" src="{{docs_base_url}}/assets/img/articles/exchange-rate-difference-1.png">

#### Alocar Registo de Pagamento

No voucher do pagamento, actualize o valor contra a conta do Cliente ou Fornecedor, depois actualize o valor do pagamento actual contra a conta Banco/Dinheiro. Adicione uma linha e selecione Moeda Extrangeira Ganho/Perda para actualizar a diferença do valor da moeda.

No cenario seguinte, Factura de Venda foi feita em EUR, ao cambio de 1.090. A este cambio, o valor da Factura de Venda em USD (moeda base) foi $1000.

Um recibo de pagamento, taxa de cambio alterou. De acordo a nova taxa de cambio, pagamento recebido na moeda base foi de $1080. Isto significa que o ganho foi de $80 devido a taxa de cambio. De seguinda como Ganho de Taxa de Cambio será alocada.

<img alt="Accounts Frozen Date" class="screenshot" src="{{docs_base_url}}/assets/img/articles/exchange-rate-difference-2.gif">

No caso de perda devido a taxa de cambio, o valor de diferença será actualizado na Conta a debito de Taxa de Cambio Ganho/Perda. Voçê pode adicionar outra linha para actualizar despesas como taxas de banco, taxas de envio, etc.

<!-- markdown -->

{next}
