<!-- add-breadcrumbs -->
# Nota de Debito

**Uma Nota de Debito é um documente enviado pelo comprador para o Fornecedor notificando que um debito foi feito contra os bens devolvidos ao Fornecedor.**

Uma Nota de Debito é criad pelo valor dos bens devolvidos. Em alguns casos, os vendedores são vistos a enviar Nota de Debito que deveriam ter sido tratadas como outra factura.

Uma Nota de Debito é um registo de debito contra os Itens devolvidos.

## 1. Como criar uma Nota de Debito

O usuário pode criar uma Nota de Debito contra uma Factura de Compra ou eles podem fazer directamente a Nota de Debito apartir da Factura de Compra sem referencia.

1. Vá para a respectiva Factura de Compra e clique em **Criar > Devolver / Nota de Debito**.
 ![Nota de Debito apartir da Factura](/docs/assets/img/accounts/debit-note-from-invoice.png)
1. O Fornecedor e os detalhes do Item serão inseridos como criados na Factura de Compra.
1. Se voçê fez um pagamento parciala ou completo, faça a Registo de Pagamento contra a Factura de Compra original.
1. Salvar e Submeter.
 <img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/debit-note.png">

Os outros passos são similares a [Factura de Compras](/docs/user/manual/pt/contabilidade/factura-compra).


### 1.1 Como uma Nota de Debito afecta o razão
Uma vez o Registo de Pagamento criado contra a Factura de Compra original, o valor será adicionado a conta do Fornecedor a negativo para que na proxima compra, este valor seja ajustado. 

Assim fica o razão depois do registo de pagamento contra a factura devolvida:
![Razão Nota de Debito](/docs/assets/img/accounts/debit-note-ledger.png)

Veja esta pagina [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra) para outros detalhes.

### 1.2 Nenhum pagamento foi feito contra a Factura de Venda
No caso de **nenhum pagamento** ter sido feito contra a factura original, voçê pode simplesmente cancelar a Factura de Venda. Mas, se 5 dos 10 Itens estão a ser devolvidos de uma factura, criando uma Nota de Debito é util para actualizar o razão.

## 2. Exemplo
Apartir do Fornecedor Blue Mills, voçê comprou Algodão no valor deRs 2400 + impostos e no hora da entrega, voçê encontrou produtos danificados. Agora voçê devolveu os produtos e uma Nota de Debito foi criada.

Nota de Debito com registo de pagamento no ERPNext para o exemplo acima citado aqui está:

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/debit_note_example1.gif">

### 3. Topicos Relacionados
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Nota de Credito](/docs/user/manual/pt/contabilidade/nota-credito)
