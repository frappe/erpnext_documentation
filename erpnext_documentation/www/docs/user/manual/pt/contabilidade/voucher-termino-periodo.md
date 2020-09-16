<!-- add-breadcrumbs -->
# Voucher de Termino de Periodo

**Um Voucher de Termino de Periodo indica que o lucro/perca para um periodo contabilistico foi balanciado e os livros pode começar do inicio.**

No fim de cada ano ou (trimestral ou até mesmo mensal), depois de terminar a auditoria, voçê pode fechar os livros da contabilidade. Isto significa que voçê pode fazer todos os registos especiais como:

  * Depreciação
  * Alterar os valores dos Activos
  * Defer impostos e responsabilidades
  * Actualizar bad debts

Depois alocar os Lucros e Perdas.

Ao fazer isto, o seu balanço nas suas Contas de Recebimento e Despesas ficam zero. Voçẽ pode comerçar um novo Ano Fiscal (ou period) com a folha de Balanço balanciada e nova conta de Lucros e Perdas. No ERPNext depois de fazer todos os registos especiais via Lançamento Contabilistico para o Ano Fisco corrente, voçẽ deve definir todas as Contas de Recebimento e Despesas para Zero usando o Voucher de Termino de Periodo.

Para aceder a lista de Voucher de Termino de Periodo, vá para:
> Home > Contabilidade > Abertura e Fecho > Voucher de Termino de Periodo

## 1. Para criar um Voucher de Termino de Periodo

1. Vá para a lista de Voucher de Termino de Periodo e clique em Novo.
1. Defina a data de postagem.
1. Selecione a Conta, usualmente esta conta é de 'Reserves and Surplus'.
1. Digite qualquer observação.
1. Salvar e Submeter.
  ![Voucher de Termino de Periodo](/docs/assets/img/accounts/period-closing-voucher.png)

### 1.2 Os Campos explicados 

* **Data de Transação** será a Data de criação do Voucher de Termino de Periodo.
* **Data de Postagem** será quando este registo for executado. Se o seu Ano Fiscal termina em a 31 de Dezembro, então essa data deve ser selecionada como Data de Postagem no Voucher de Termino de Periodo.
* **Fechando o Ano Fiscal** será o ano no qual voçê esta a fechar o seu extracto Contabilistico.

### 1.3 O que acontece ao submeter?
O Voucher de Termino de Perido irá criar registos de contabilidade (GL Entry). Este irá fazer com que todos as suas contas de Recebimento e Despesas e transferir o Balanço de Lucros/Perdas para a Conta de Termino.

Voçê deve selecionar a conta de Responsabilidade como Reserves and Surplus, ou qualquer conta Revenue Reserve ou nas contas de Capital de Donos como Contas de Termino.

![Razão do Voucher de Termino de Periodo](/docs/assets/img/accounts/period-closing-voucher-ledger.png)

> **Nota:** Se os registos de contabilidade foram feito num Ano Fiscal a terminar, mesmo que o Voucher do Termino de Periodo tenha sido criado neste Ano Fiscal, voçê dever criar um outro Voucher de Termino de Periodo. Depois o Voucher será somente transferir para o balanço P&L para a Conta de Cabeça.

### 2. Topicos Relacionados
1. [Ano Fiscal](/docs/user/manual/pt/contabilidade/ano-fiscal)
1. [Categoria de Isenção de Impostos](/docs/user/manual/pt/contabilidade/categoria-insenção-impostos)
1. [Periodo Contabilistico](/docs/user/manual/pt/contabilidade/periodo-contabilistico)
