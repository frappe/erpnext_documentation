<!-- add-breadcrumbs -->
# Gerindo Transações em Mutlipla Moedas

No ERPNext, transações podem ser criadas na moeda base como das partes (clientes ou fornecedores). Se a transação foi criada na moeda da parte, o simbolo da moeda é actualizado no formato de impressão.

Se voçê estiver a fazer uma proforma pra um Cliente em moeda diferente, voçêo irá ter que actualizar a taxa da cambio para permitir o ERPNext salvar a informação na sua moeda base. Isto irá ajudar a analizar as suas Proformas na sua moeda.

Vamos confiderar a Factura de Venda, aonde a sua moeda base é USD e da parte é EUR.

1. Crie a nova Factura de Venda: **Home > Contabilidade > Contas a Receber > Factura de Vendas > Nova**.

1. Selecione o Clinte. Se tiver moeda padrão na ficha do Cliente será usada.

1. Taxa de Cambio entre a moeda base e do cliente serão inseridos.

    <img alt="Accounts Frozen Date" class="screenshot" src="{{docs_base_url}}/assets/img/articles/multiple-currency-1.png">

1. Actualize os detalhes como Item, Impostos, Termos. Em impostos e outras taxas. Taxas serão actualizadas de acordo a moeda do Cliente.

1. Salvar a Factura de Venda e verificar a impressão. para todos os campos de Moeda (preço, valor totais) irá mostrar na moeda do Cliente.

    <img alt="Accounts Frozen Date" class="screenshot" src="{{docs_base_url}}/assets/img/articles/multiple-currency-2.png">

## Ficha de Taxa de Cambios

Se voçê chegou a condições com a parte para usar taxa de cambio normal, voçê pode guardar na tabela de Taxa de Cambios. Para criar, vá para:

> Home > Contabilidade > Multiplas Moedas > Taxa de Cambio

No ERPNext, taxas de cambio real são inseridas.

**Nota**: Se voçê criar uma Taxa de Cambio com um valor especifico, será usado em vez das taxas de cambio online. Por exemplo, se definir que $1 = ₹65 na Taxa de Cambio, e se online for ₹69, ₹65 será usado nas transações.

{next}
