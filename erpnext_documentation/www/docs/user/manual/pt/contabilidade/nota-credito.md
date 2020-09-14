<!-- add-breadcrumbs -->
# Nota de Credito

**Uma Nota de Credito é um documento enviado pelo vendedor para um Cliente, notificando que um credito foi feito na conta deles a favor dos bens devolvidos pelo comprador.**

Uma Nota de Credito é criada para o valor de bens devolvidos pelo Cliente, pode ser menos ou igual ao valot total da ordem. 

## 1. Como criar uma Nota de Credito

O usuário pode criar uma Nota de Credito contra a Factura de Venda ou ele podem criar directamente a Nota de Credito apartir da Factura de Venda sem Refenrencia. De notar que para criar uma Nota de Credito, a factura deve estar paga usando o [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento).

1. Vá para a Factura de Venda respectiva e clique em **Criar > Retorno / Nota de Credito**.
    ![Nota de Credito apartir da Factura](/docs/assets/img/accounts/credit-note-from-invoice.png)
1. O Cliente e detalhes do Item serão inseridos como foram criados na Factura de Vendas.
1. Se o Cliente fez o pagamento parcial ou completo, faça um Registo de Pagamento contra a Factura de Venda original.
1. Salvar e Submeter.
    <img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/credit-note.png">

A quantidade do Item e valor de Pagamento será negativo vendo tratar-se de uma devolução.

### 1.1 Como uma Nota de Credito afecta o razão
Uma vez o Registo de Pagamento for criado contra a Factura de Venda original, o valor será adicionado a conta do Cliente a negativo para que da proxima vez que fizer uma compra, o valor será ajustado. 

Aqui está como o Razão é afectado depois do registo de pagamento contra a devolução da factura:
![Razão Nota de Credito](/docs/assets/img/accounts/credit-note-ledger.png)

Veja a página [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas) para qualquer outro detalhe.

### 1.2 Nenhum pagamento foi feito contra a Factura de Venda
No caso de **nenhum pagamento** ter sido feito contra a factura original, voçê pode simplesmente cancelar a Factura de Venda. Mas, se somente 5 dos 10 Itens estão a ser devolvidos da factura, criando uma Nota de Credito é util para actualizar o razão.

## 2. Exemplo

O Cliente Rohan comprou tubos de PVC no valor de Rs 300 + impostos e na altura da entrega, o Cliente encontrou que os produtos estavam danificados. Agora o Rohan devolveu os produtos e uma Nota de Credito será criada.

Nota de Credito com registo de pagamento no ERPNext para o exemplo acima será assim:

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/credit_note_example1.gif">

### 3. Topicos Relacionados
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Nota de Debito](/docs/user/manual/pt/contabilidade/nota-debito)
1. [Retorno de Vendas](/docs/user/manual/pt/inventario/retorno-vendas)