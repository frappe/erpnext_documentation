<!-- add-breadcrumbs -->
# Plano de Contas

**O Plano de Contas é o blueprint das contas nas suas empresas.**

A estrutura geral do seu Plano de Contas é basead num sistema duplo de registo de contabilidade que se tornou
normal em todo o mundo para quantificar como uma 
empresa está financeiramente.

O Plano de Contas é uma arvore dos nomes das Contas (Livros-razão e Grupos) que a Empresa
precisa para gerir os seus Livros de Contas. O ERPNext define um simples Plano de Contas
para cada Empresa que voçê criar, mas voçê pode modificar de acordo as 
suas necessidade e requesitos legais.

Para cada empresa, Plano de Contas significa a maneira de classificar os registos contabilisticos, principalmente
baseados nos requesitos do estatuto (imposto, compliance aos regulamentos necessarios do governo).

![Arvore PdC](/docs/assets/img/accounts/chart-of-accounts-tree.png)

O Plano de Contas ajuda-lhe a responder perguntas como:

 * O que vale a sua empresa?
 * Quanto debito voçê tem?
 * Quanto lucro está a fazer (e claro pagar imposto)?
 * Quanto está a vender?
 * Qual o seu break-up de despesas?

Como alguem que gere um negocio, é de muito valor ver o quão bem
o seu negocio anda.

> **Dica**: Se voçê não pode ler um Balanço é uma boa oportunidade para começar a aprender. Irá valer o esforço. Voçê pode tambem ter a ajuda dos seus contabilistas para configurar o seu Plano de Contas.

Para aceder a lista do Plano de Contas, vá para:
> Home > Contabilidade > Mestre Contabil > Plano de Contas

## 1. Como Criar/Editar Contas
O ERPNext vem com um Plano de Contas normal definido. Em vez de criar/modificar, voçê pode usar a ferramenta [Importador de Plano de Contas](/docs/user/manual/pt/configurações/importar-plano-de-contas). Note que o Plano de Contas existente irá passar por cima quando utilizar esta ferramenta.

1. Vá para a lista de Plano de Contas.
 
 Aqui voçê pode abrir um grupo de contas que contem contas. Tem opções para "Adicionar Contas Filhas" ao plano, Editar ou Apagar a conta.

 <img class="screenshot" alt="Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/chart-of-accounts-add.gif">

1. A opção para criar uma conta filha apenas irá aparecer quando voçê fizer o clique na Conta do Tipo de Grupo (pasta).
1. Digite o nome da conta.
1. Digite o numero para a conta.
1. Selecione 'É um Grupo' se voçê quiser que esta seja uma conta de grupo que pode conter outras contas.
1. Selecione o Tipo de Conta. Selecionando este é importante pois alguns campos permitem selecionar apenas um tipo especifico de contas.
1. Altere a moeda se esta conta irá ser utilizada em transações com moedas diferentes. Por defeito, é a moeda da Empresa. Para saber mais, visite a pagina [Contabilidade Multi Moedas](/docs/user/manual/pt/contabilidade/contabilidade-multi-moedas).
1. Clique em **Criar Novo**.

Tipicamente, voçê poderá querer criar Contas para:

 * Viagem, salários, tefefone, etc. em **Despesas**.
 * Imposto de Valor Acrescentado (IVA), Imposto de Vendas, Equidade, etc. em **Responsabilidades Correntes**.
 * Venda de Produtos, Venda de Serviços, etc. em **Recebimentos**.
 * Predios, equipamentos, mobiliario, etc. em **Activos**.

<img class="screenshot" alt="Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/chart-of-accounts-1.png">

> Dica: Contas com moedas diferentes são criadas quando voçê recebe or faz pagamentos para ou apartir de diferentes moedas. Por exemplo se voçê esta na India e fizer transações com USA, voçê poderá precisar criar contas como 'US Debitos', 'US Creditos', etc.

Vamos entender os grupos principais do Plano de Contas.

## 2. Tipo de Contas
Tipo de Contas são classificadas principalmente como recebimentos, despesas, activos ou reponsabilidade.

### 2.1 Contas de Balanço

Contas de Balanço são 'Aplicação de Fundos (Activos)' ou 'Fonte de Fundos (Responsabilidades)
que significam o valor net-worth da sua empresa em qualquer momento.
Quando voçê começa ou termina o periodo financeiro, todas os Activos são iguais as 
Responsabilidades.

> **Uma nota na Contabilidade**: Se voçê for novo em contabilidade, voçê pode ficar pensando, como pode
Activo ser igual a Responsabilidades? Isto significaria que a empresa não tem nada que seja dela.
Isto é correcto! Todos os "investimentos" feito na empresa para comprar activos (como terra, mobiliario, equipamento)
percente aos donos. Os são uma responsabilidade para com a empresa vendo que os lucros pertencem aos donos.

> Se a empresa tiver que fechar, seria necessario vender todos os activos
e pagar de volta todas as responsabilidades (incluindo lucros) aos donos,
deixando ela sem nada.

Todas as contas no Balanço representam um activo pretencente a empresa como "Conta Bancária",
"Terra e Propriedade", "Mobiliario" ou uma responsabilidade (fundos qua a empresa deve a outros)
como "Dono dos fundos", "Debito" etc.

Duas contas especiais para notar aqui são Contas de Recebimento (dinnheiro que voçê tem que recolher dos seus
Clientes) e Contas a Pagar (dinheiro que voçê tem que pagar aos seus Fornecedores) respectivamente
dentro dos Activos e Responsabilidades.


### 2.2 Conta de Lucros e Percas

Lucros e Percas é um grupo de contas de 'Recebimentos' e 'Despesas' que representam as suas
transações de contabilidade dentro de um periodo.

Não como as contas de Balanço, Contas de Lucro e Percas (ou Contas PL) não representam liquido (Activos)
net worth (Assets), mas representam sim o montante de dinheiro gasto e recolhido em servir os
clientes durante o periodo. Assim, sendo no inicio e fim do seu Ano Fiscal, eles passam para zero.

No ERPNext é bastante facil manter registo dos Lucros e Percas usando o Grafico de Lucros e Percas.

![Relatorio de Lucros e Percas]({{docs_base_url}}/assets/img/accounts/profit_n_loss_report_1.png)


Note que, no primeiro dia do ano voçê não tem nenhum lucro ou perca, mas voçê ainda tem
activos, daí as contas de balanço nunca ficarem zero no inicio ou fim do periodo.

### 2.3 Grupos e Livros-Razão

Exitem dois tipos principais de Contas no ERPNext - Grupos e Livros-Razão. Grupos podem ter sub-grupos e 
Livros-Razão dentro deles, aonde os Livros-Razão são os nodulos de folhas do seu Grafico e não podem ter
mais contas dentro delas.

Transações de Contabilidade podem ser feitas apenas a favor de Contas de Livros-Razão (não Grupos)

> Info: O termo "Livros-Razão" significam uma folha num livro de contabilidade aonde os registos são feitos.
Existe normalmente um Livros-Razão para cada conta (como um Cliente ou um Fornecedor).

> Nota: Uma Conta "Livros-Razão" é tambem as vezes chamado de Conta "Cabeça".

<img class="screenshot" alt="Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/chart-of-accounts-2.png">


### 2.4 Outro Tipo de Contas

No ERPNext, voçê pode tambem especificar mais informação quando voçê cria uma nova Conta, está lá para o ajudar a selecionar
aquela conta em particular num cenario como 'Conta Bancária' ou uma 'Conta de Imposto' e não tem efeito no Grafico em si.

Explicação do Tipo de Contas:

* **Depreciação Acumulada**: Para guardar a informação do total acumulado da depreciação dos activos da Empresa. Depreciação Acumulada aparece na folha de Balanço.
* **Activos Recebidos Mas Não Cobrados**: Uma conta temporaria de responsabilidade aonde guarda o valor dos Activos recebidos mas não cobrados ainda.
* **Banco**: O tipo de conta aonde as Contas Bancárias serão criadas. Deve existir pelo menos um grupo de Contas to tipo "Banco" na PdC.
* **Caixa**: O tipo de conta aonde as Contas de Dinheiro serão criadas. Deve existir pelo menos um grupo de Contas to tipo "Dinheiro" no PdC.
* **Chargeable**: Taxas adicionais aplicadas a Itens podem ser guardas neste tipo de contas. Por exemplo, "Frete e Forwarding Taxas".
* **Trabalho Capital em Progresso**: Taxas correntes ao criar os Activos são guardados em contas CWIP. Por exemplo, custos de construção ao construir um predio. No ERPNext os Activos são alocados contra contas CWIP quando não estão a ser utilizadas. 
* **Custo dos Bens Vendidos**: Uma conta deste tipo é usada para alocar o total acumulado de todos os custos incorridos enquanto o fabrico/compra de produtos ou serviços, vendidos por uma empresa.
* **Depreciação**: A conta de despesa para alocar a depreciação de um Activo. Este aparece como um extracto de Recebimento.
* **Equidade**: Este tipo de contas representam transações com pessoas que detem o negocio, ex. os acionistas/donos.
* **Despesas Incluidas na Valuação de Activos**: A conta para alocar as despesas (para alem do custo directo de material dos Activos) incluidas no custo landed de um Activo.
* **Despesas Incluidas na Valuacao**: A conta para alocar as despesas (para alem do custo directo de material) incuida no custo landed de um item/produto, usado no Inventario Perpetual.
* **Activos Fixos**: A conta para manter o custo dos Activos fixos.
* **Conta de Recebimentos**: Este tipo de conta representa todo a fonte de recebimento ou rendimento alocado para a Empresa.
* **Pagaveis**: O tipo de conta representa o valor devido pela empresa aos seus credores (Fornecedores).
* **Recebimentos**: O tipo de conta representa o valor devido a uma empresa pelos seus devedores (Clientes).
* **Round Off**: Em muitas Facturas podem haver [rounding off](/docs/user/manual/pt/contabilidade/argtigos/round-off-account-validation) no montante final. Para melhor rastreio, estes valores são alocados em contas deste tipo.
* **Stock**: O grupo de contas no qual [Contas de Armazem](/docs/user/manual/pt/contabilidade/artigos/round-off-account-validation) são criadas. 
* **Ajuste de Stock**: Uma conta de despesa para alocar qualquer registo de ajuste de stock/inventario. Normalmente vem ao mesmo nivel que o Custo de Bens Vendidos.
* **Stock Recebido Mas Não Cobrado**: Uma conta de responsabilidade temporaria para alocar o valor do stock recebido mas não foi cobrado ainda e é usado no Perpetual Inventory.
* **Impostos**: Todas as contas de Imposto como IVA, Retenção na fonte, etc. vão para estes tipo de contas.
* **Temporario**: Uma conta Temporaria é util para balancear recebimentos, despesas e anular quando estiver a mudar para o ERPNext no meio do ano com Lançamentos Contabilisticos pendentes.

> **Nota**: Ao fazer um Registo de Pagamento, a conta por defeito do banco será inserida na seguinte ordem se foi definido:
    
>       * Formulario da Empresa
>       * Conta defeito para Modo de Pagamento
>       * Conta Bancária de Cliente/Fornecedor
>       * Selecione manualmente no Registo de Pagamento

### 2.5 Extractos Financeiros
Extractos Financeiros para uma empresa são facilmente visiveis no ERPNext. Voçê pode ver os extractos da folha de Balanço, Lucros e Percas, 
e Fluxo de Caixa.

Um Exemplo de varios extractos financeiros estão aqui em baixo:

1. Relatorio de Fluxo de Caixa:
 <img class="screenshot" alt="Cash Flow Report" src="{{docs_base_url}}/assets/img/accounts/cash_flow_report.png">

1. Relatorio de Lucros e Percas:
 <img class="screenshot" alt="Profit and Loss Report" src="{{docs_base_url}}/assets/img/accounts/profit_n_loss_report.png">
 
1. Relatorio da Folha de Balanço:
 <img class="screenshot" alt="Balance Sheet Report" src="{{docs_base_url}}/assets/img/accounts/balance_sheet_report.png">

### 2.6 Numero de Conta
Um Plano de Contas normal está organizado de acordo um sistema numerico. Cada categoria começa com um certo numero, e a sub-categoria dentro irá iniciar com o mesmo numero. Por exemplo, se os activos estão classificado por numeros começando pelo digito 1000, então as contas de caixa podem ser 1100, contas bancárias pode ser 1200, contas de recebimentos pode ser 1300 e assim sucessivamente. Uma falha entre os numeros normalmente existe para adicionar contas futuras.

Voçê pode atribuir um numero enquanto estiver a criar a conta no Plano de Contas. Voçê pode tambem ediar o numero da conta, fazendo o clique no botão **Actualizar Nome da Conta / Numero**. Ao actualizar o numero da conta, o sistema renomeia automaticamente o nome da conta para incluir o numero no nome.

![Numero de Conta]({{docs_base_url}}/assets/img/accounts/acc-no.png)

## 3. Video

<div>
 <div class="embed-container">
 <iframe src='https://www.youtube.com/embed//AcfMCT7wLLo' frameborder='0' allowfullscreen>
 </iframe>
 </div>
</div>

### 4. Topicos Relacionados
1. [Saldo de Abertura](/docs/user/manual/pt/contabilidade/saldo-abertura)
1. [Configurações de Contabilidade](/docs/user/manual/pt/contabilidade/configurações-contabilidade)
1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)
1. [Lançamento Contabilistico Inter Empresa](/docs/user/manual/pt/contabilidade/lançamento-contabilistico-inter-empresa)
1. [Relatorio de Contabilidade](/docs/user/manual/pt/contabilidade/relatorios-contabilidade)
1. [Contabilidade Multi Moeda](/docs/user/manual/pt/contabilidade/contabilidade-multi-moedas)
