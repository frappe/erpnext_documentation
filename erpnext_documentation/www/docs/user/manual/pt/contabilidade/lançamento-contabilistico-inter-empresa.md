<!-- add-breadcrumbs -->
# Lançamento Contabilistico Inter Empresa

**Um Lançamento Contabilistico Inter Empresa é feito entre organizações que pertencem ao mesmo grupo.**

Voçê pode criar Lançamento Contabilistico Inter Empresa se estiver a fazer transações com multiplas Empresas.
Voçê pode selecionar as Contas que voçê deseja usar nas transações de Inter Empresa. Um possivel uso seria uma empresa comprando bens em nome de outra empresa.

Antes de criar Lançamento Contabilistico Inter Empresa, voçê precisa de definir o seu Plano de Contas.

1. Go to: **Contabilidade > Emppresa e Contas > Plano de Contas**.
1. Selecione a Conta que deseja definir como Conta Interna para as transações, e selecione a caixa 'Conta Inter Empresa'. Esta conta pode agora ser usado para transações de Lançamento Contabilistico Inter Empresa. É recomendado criar uma nova conta para transações Inter Empresa.
    <img class="screenshot" alt="Internal Account" src="{{docs_base_url}}/assets/img/accounts/internal-account.png">
Voçê precisa fazer o memso para todas as Contas das Empresas que pretende usar em transações de Lançamento Contabilistico Inter Empresa.

No caso de empresas mãe-filho, quando uma conta é criada na empresa mãe, é adicionado na empresa filho. Isto funciona somente se voçê selecionou a opção para cirar o Plano de Contas para empresas filho baseado no Empresa mãe.

Lançamento Contabilistico Inter Empresa são criados usando o formulario de Lançamento Contabilistico no ERPNext. Para ter acesso a lista de Lançamento Contabilistico, vá para:

> Home > Contabilidade > Empresa e Contas > Lançamento Contabilistico

## 1. Pre-requisitos
Antes de criar o Lançamento Contabilistico Inter Empresa, voçê deve seguir:

* Pelo menos ter duas [Empresas](/docs/user/manual/pt/configuração/configuração-empresa)
* Configurando Contas Inter Empresa no [Plano de Contas](/docs/user/manual/pt/contabilidade/plano-de-contas)

## 2. Como criar Lançamento Contabilistico Inter Empresa
1. Vá para a lista de Lançamento Contabilistico, e clique em Novo.
1. Selecione o Tipo de Registo como 'Lançamento Contabilistico Inter Empresa'.
1. Defina a Empresa que está a comprar Itens em nome da outra empresa.
1. Adicione linhas para os registos de contas individuais. Somente contas inter Empresa podem ser inseridas aqui.
1. Em cada linha, voçê deve especificar:
  * A Conta Interna que será afectada. 
  * O valor do Debito ou Credito.
  * O Centro de Custo (Se for um Recebimento ou Despesa).
1. Ao submeter o Lançamento Contabilistico, voçê irá ver um botão no topo em cima no lado direito, **Criar Lançamento Contabilistico Inter Empresa**.

   <img class="screenshot" alt="Submitted Inter Company Journal Entry" src="{{docs_base_url}}/assets/img/accounts/inter-company-jv-submit.png">

1. Clique no botão. Agora, voçê irá perguntado para selecionar a Empresa contra o qual deseja criar o Lançamento Contabilistico.

    <img class="screenshot" alt="Select Company" src="{{docs_base_url}}/assets/img/accounts/select-company-jv.png">

1. Ao selecionar a Empresa, voçê irá ser enviado para o Lançamento Contabilistico aonde os campos relativos serão mapeaddo, ex. Empresa, Tipo de Voucher, Referencia do Lançamento Contabilistico Inter Empresa etc. 

    <img class="screenshot" alt="Linked Journal Entry" src="{{docs_base_url}}/assets/img/accounts/linked-jv.png">

1. Selecione a Conta Interna para a segunda Empresa na Tabela.
1. Submter o Lançamento Contabilistico.
1. Tenha a certeza que o total do Debito e Credito são iguais como os Valores dos Lançamentos Contabilisticos anteriores de Debito e Credito mas os debitos e creditos serão o oposto.

**Nota:** As contas no segundo Lançamento Contabilistico devem ser o oposto do que fez no primeiro Lançamento.
Por exemplo, Empresa A comprou algo da Empresa B. Assim deverá ser o ciclo de pagamento entre as duas empresa usando o Lançamento Contabilistico Inter Empresa.

1. Debitar Conta Banco 500 e creditar 500 na conta Devedor da Empresa B.
1. Agora, no Lançamento Contabilistico Inter Empresa, debitar 500 na conta Credor da Empresa A e creditar 500 na conta Banco. 
1. Voçê tambem precisa selecionar as partes da conta Credor e Devedor antes de proceder com o Lançamento Contabilistico.

Voçê vai encontrar o botão de ligação, no qual será adiconado em ambos Lançamentos Contabilisticos e será removido caso alguns dos registos seja cancelado.

### 3. Topicos Relacionados
1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)
1. [Facturas Inter Empresa](/docs/user/manual/pt/accounts/factura-inter-empresa)
