<!-- add-breadcrumbs -->
# Periodo Contabil

**Um Periodo Contabil define um periodo de tempo em que os extractos finaneiros são registados.**

No ERPNext, definindo um Periodo Contabil congela os registos das transações num certo perido de tempo. Isto significa que as transações selecionadas não poderam ser submetidas no Periodo Contabil definido.

Considere que voçê quer gerar relatorios financeiros do negocio no 3 Quarto e voçê quer permitir submeter somente alguns registos especificos neste periodo. Ou voçê quer congelar todos os registos que afectem o Razão Geral. Periodo Contabil no ERPNext permite fazer isto.

## 1. Como criar um Periodo Contabil
1. Digite o nome do Periodo Contabil.
1. Defina o tempo configurando as Datas de Inicio e Fim.
1. Adicone ou remova transações da tabela. Note que todas as transações listadas na tabela ficaram congeladas.
1. Salvar.
    ![Periodo Contabil](/docs/assets/img/accounts/accounting-period.png)


Voçê irá ver uma janel se voçê tentar submeter uma transação deinida no Periodo Contabil.
![Periodo Contabil](/docs/assets/img/accounts/accounting-period-1.png)

> Nota: Nenhum perfil pode submter transações definidas no Periodo Contabil, até mesmo a Perfil definido em 'Perfil Permitido a Congelar Contas & Editar Registos Congelados' em [Configurações de Contabilidade](/docs/user/manual/pt/contabilidade/configurações-contabilidade).

## 2. Topicos Relacionados
* [Voucher de Termino de Periodo](/docs/user/manual/pt/contabilidade/voucher-termino-periodo)