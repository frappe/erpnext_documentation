<!-- add-breadcrumbs -->
# Integração do Stock e Modulo de Contabilidade

O valor de stock guardado no armazem precisa ser controlado.

Cada armazem está ligado a um razão no Plano de Contas atravez do campo Conta no armazem.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/stock_asset_ledger_in_warehouse.png">

Se o campo da Conta estiver vazio no armazem, então a Conta mencionada como Mãe deste armazem será usado. Se uma Conta não foi encontrada pela hiearquia, então a Conta do Inventário Padrão no formulario da Empresa será usado.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/default_inventory_account.png">

Quando uma Empresa é criada, o razão 'Stock Em Mão' é criado por defeito no Plano de Contas.

**Plano de Contas > Activos > Activo Currente > Activo de Stock > Stock Em Mão.**

Se necessário, voçê pode criar razões adicionais no grupo 'Activos de Stock'.

<img class="screenshot" alt="Stock Asset Ledger" src="{{docs_base_url}}/assets/img/accounts/stock_asset_ledger.png">
