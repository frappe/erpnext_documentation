<!-- add-breadcrumbs -->
# Actualizar Activos Fixos

Para importar todos os Activos Fixos existentes primeiro deve criar o registo de activo e depois um Lançamento Contabilistico para Actualizar o Razão Geral.

## 1. Criar Registo de Activos

Criar registo de Activos para cada activo na sua empresa na qual não estão completamente depreciados.

Para criar um novo Activo:

1. Criar em [Item](/docs/user/manual/pt/inventario/item) como o 'É Activo Fixo' activo.
1. Vá para **Activos > Activo > Novo**.
1. Digite o Nome do Activo.
1. Digite o Codigo do Item.
1. Digite a Localização.
1. Digite a Data de Compra.
1. Digite o Valor de Compra.
1. Selecione **É Activo Existente.**
1. Salvar.

    <img class="screenshot" alt="Stock Asset Ledger" src="{{docs_base_url}}/assets/img/accounts/asset_opening_balance.png">

> Para saber mais sobre Activos em detalhe, [visite esta pagina](/docs/user/manual/pt/activos/activo).

## 2. Crie um Lançamento Contabilistico para Actualizar o Razão

Quando voçẽ cria um Activo com a opção 'É Activo Existente' activa, o Razão Geral não é actualizado. Voçê tem que actualizar o valor pelo Lançamento Contabilistico.

Para criar um novo Lançamento Contabilistico:

1. Vá para: **Contabilidade > Razão Geral > Lançamento Contabilistico > Novo.**
1. Digite a Data de Postagem.
1. Selecione o razão do Activo Fixo apropriado na coluna Contas e digite o valor do Debito.
1. Selecione razão 'Abertura Temporaria' na coluna Conta e digite o valor do balanço na coluna Credito.
1. Defina 'É Abertura' para Sim.

<img class="screenshot" alt="Stock Asset Ledger" src="{{docs_base_url}}/assets/img/accounts/journal_entry_for_fixed_asset_opening_balance.png">

{next}
