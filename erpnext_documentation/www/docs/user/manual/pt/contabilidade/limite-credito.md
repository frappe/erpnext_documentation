<!-- add-breadcrumbs -->
# Limite de Credito

**Limite de Credito é o valor maximo de credito que voçê está disposto a oferecer a um Cliente.**

Um Limite de Credito é o valor maximo de credito que a instituição financeira or 
ou outro emprestador irá extender a um devedor para uma linha de credito em particular. Do ponto de vista
de um Cliente, é o valor maxiom de bens ou serviços que les podem ter sem fazer qualquer pagamento adiantado.

Voçê pode definir o Limite de Credito no Cliente, Grupo de Cliente e na Empresa.
Quando uma Ordem de Venda ou uma Factura de Venda é submetida, o Limite de Credito será verificado.

A ordem de precedencia para verificar o Limite de Credito é da seguinte forma:

* Limite de Credito é definido no Cliente
* Limite de Credito é definido no Grupo de Cliente
* Limite de Credito é definido na Empresa


## 1. Como Definir o Limite de Credito
1. Vá para: **Vendas > Vendas > Cliente > Cliente**.
1. Na secção Limite de Credito e Termos de Pagamento, defina o Limite de Credito.
1. Se voçê deixar o Limite de Credito como defeito, ex. 0, não tem efeito.
1. Salvar.

    <img class="screenshot" alt="Credit Limit" src="{{docs_base_url}}/assets/img/accounts/customer-credit-limit.png">

## 2. Funcionalidades
### 2.1 Controlador de Credito
Voçê pode permitir os usuário com um papel especifico de passar por cima da validação do Limite de Credito ao submter a Ordem de VEnda ou a Factura de Vendas mesmo quando o Limite de Credito do Cliente já foi utilizado por completo.

Para definir o papel de Controlador de Credito:

1. Vá para: **Contabilidade > Configuraçãoes > Configurações de Contabilidade**
1. Defina o papel no campo Controlador de Credito.

<img class="screenshot" alt="Credit Limit" src="{{docs_base_url}}/assets/img/accounts/credit_controller_role.png">

### 2.2 Bypass o Verificador do Controlador de Credito para Ordens de Venda

Para clientes especificos, voçê pode definir o limite de credito para ser vificado sobre o montante acumulado de uma factura de vendas em falta e não e na Ordem de Venda. Voçê pode fazer selecionando a caixa 'Bypass o Verificador do Controlador de Credito para Ordens de Venda' na secção 'Limite de Credito e Termos de Pagamento' do cliente.

<img class="screenshot" alt="Customer Credit Limit" src="{{docs_base_url}}/assets/img/accounts/customer-credit-limit-bypass.png">


### 2.3 Limite de Credito para Grupo de Clientes
Para definir o Limite de Credito a nivel de Grupo de Clientes:

1. Vá para **Vendas > Clientes > Grupo de Clientes**.
1. Abra o Grupo de Cliente e defina o Limite de Credito.

### 2.4 Limite de Credito para Empresa
Ao definir o Limite de Credito a nivel de Empresa, todos os Clientes irão ter este Limite de Credito aplicado.

Para definir o Limite de Credito a nivel da Empresa:

1. Vá para **Contabilidade > Mestres Contabeis > Empresa**.
1. Abra a Empres e defina o Limite de Credito.

### 3. Topicos Relacionados
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Cliente](/docs/user/manual/pt/CRM/cliente)
