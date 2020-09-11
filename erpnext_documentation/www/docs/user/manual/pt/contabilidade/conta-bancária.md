<!-- add-breadcrumbs -->
# Conta Bancária

No ERPNext, Contas Bancárias podem ser criadas para uma Empresa bem como para partes como Clientes, Fornecedores, etc. Fazendo isto faz co que voçê registe todas as transações do banco correcta para o apuramento de contabilidade.

Voçê pode adicionar Contas Bancária no ERPNext para Empresa, Fornecedor, Cliente ou para qualquer outra parte com quem tiver transações. Depois a Contas Bancária pode ser selecionada em [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento) como [Modo de Pagamento](/docs/user/manual/pt/contabilidade/modo-de-pagamento).

Para aceder a Conta Bancária, vá para:
> Home > Contabilidade > Extracto do Banco > Contas Bancária

![Contas Bancárias](/docs/assets/img/contabilidade/bank-account.png)

## 1. Pre-requisitos
Antes de criar e utilizar as Contas Bancárias, é aconselhavel criar os seguintes primeiro:

* [Banco](/docs/user/manual/pt/contabilidade/banco)

## 2. Como criar uma Conta Bancária
1. Digite um Nome de Conta.
1. Ligue a conta do Razão Geral que está em 'Contas Bancárias' no [Plano de Contas](/docs/user/manual/pt/contabilidade/plano-de-contas).
1. Selecione o Banco.
1. Salvar.

### 2.1 Opções Adicionais ao criar uma Conta Bancária

* **É a Conta Principal**: Activando isto irá por esta como a conta principal do banck para todos registos de transação.
* **É Conta da Empresa**: Activar se esta Conta Bancária é a conta da Empresa.
* Um Tipo de Conta e Subtipo de Conta podem ser definidos para maior classinficação no relatorios, etc.

## 3. Funcionalidades
### 3.1 Detalhes das Partes

* **Tipo de Parte**: Caso não seja uma conta de empresa, defina a quem pertence. As opções disponiveis são: Cliente, Funcionário, Membro, Acionista, Estudante e Fornecedor. 
* **Parte**: Selecione o Cliente/Fornecedor especifico, etc.

### 3.2 Detalhes de Conta

Para referencia, os seguintes detalhes acerca Conta Bancária podem ser guardadas no ERPNext:

* IBAN
* No de Conta Bancária
* Codigo de Branch
* Numero de SWIFT

### 3.3 Endereço e Contacto

* **Endereço**: Um banco pode ter varios na mesma localidade. O endereço do branch do pode ser inserido aqui.
* **Contacto**: Uma Pessoa de Contacto pode ser vinculada aqui. Bancos normalmente apresentão um contacto dedicado para contas de Empresa, voçê pode adicionar esta pessoa de contacto aqui.
* **Pagina Web**: Voçê pode adicionar a Pagina Web do Banco aqui.

### 3.4 Detalhes de Integração

**Data da Ultima Integração**: Caso o seu Banco suporte [Integração Plaid](/docs/user/manual/pt/integração_erpnext/plaid_integration), configurando uma data aqui irá sincronizar neste periodo.Isto irá criar um registo de Transação Bancaria.
