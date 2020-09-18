<!-- add-breadcrumbs -->
#Retirando Salário da Conta de Equidade do Dono

### Pergunta

Depois da reunião com o contabilista aqui nos US, eu fui informado que a minha empresa como sendo o unico membro, eu não devia pagar a mim mesmo um salario que atinga directamente as contas de despesas mas em vez disso fazer um "draw" que atinga as folhas de balanço e não as despesas. Pode me aconselhar como eu devo fazer esta configuração no ERPNext?

### Resposta

1. Criar uma Conta em Responsabilidades para **Equidade do Dono** se ainda não o tem. Esta conta será o seu investimento no negocio e o lucro acumulado (ou perda). Será do tipo de balanço "Credito".
2. Na versão 15, Equidade será um novo head (não em baixo de Responsabilidades). (Em qualquer um dos casos de ACtivos = Equidade do Dono + Responsabilidades,  para verificar a sua folha de balanço [Aprenda mais sobre a conta de equidade do dono](http://www.accountingcoach.com/blog/what-is-owners-equity)).
3. Criar uma conta **Draws do Dono** em **Equidade do Dono**.
4. De notar que o balanço do **Draws do Dono** será sempre negativo vendo que voçê esta a retirar dinheiro do total da sua equidade / lucros.

### Exemplo

Exemplo de um Lançamento Contabilistico (usando o Registo de Jornal no ERPNext) para o withdrawal de $1000 seria:

1. Credito **Dinheiro** $1000
2. Debito **Draws do Dono** $1000

<!-- markdown -->

{next}
