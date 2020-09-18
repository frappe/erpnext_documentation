<!-- add-breadcrumbs -->
# Mensagem de Validação de Arredondamento da Conta

**Pergunta** 

Ao submeter uma factura, porque que pede uma Conta de Arredondamento? Como aplicar?

<img class="screenshot" alt="Fees Section" src="{{docs_base_url}}/assets/img/accounts/round-off-account.png">

**Resposta**

Em Facturas de Compra, Total Geral é calculado com base nos varios calculos como:

- Qtd * Preço = Montante
- Imposto e outras traxas aplicadas em cada item
- Descontos aplicados para alguns ou todos itens
- Multiplicação da taxa de cambio, em caso de multiplas moedas

Como resultado dos calculos, poderá have perdas em arredondamento no total final. Esta perda de arredondamento é geralmente numa margem 0.034. Mas para accuracy de contabilidade, dever ser registado. Daí, voçê precisar definir uma conta de arredondamento na Empresa devido o resultado da perda de arredondamento para ser alocado.

Voçê precisa criar uma Conta de Arredondamento no Plano de Contas e actualizar. Os passos aqui.

* Contabilidade > Plano de Contas
* No Plano de Contas, verifique o crie uma nova conta em Despesas > Despesas Directas. Ignore se a conta para este movito já existe
* Vá para o formulario Empresa
  Contabilidade > Empresa
* Abra a Empresa na qual a conta de arredondamento de ver ser actualizada.
* Na Empresa, vá até Configurações de Contabilidade e selcione a Conta de Arredondamento e o Centro de Custo.
    <img class="screenshot" alt="Fees Section" src="{{docs_base_url}}/assets/img/accounts/company-round-off-account.png">

Uma vez a conta criada actualize, e tente submeter a Factura de Compra.

{next}
