<!-- add-breadcrumbs -->
# Configuração Empresa

**A empresa é uma entidade legal feita da associação de pessoas para levar a cabo uma activadade comercial ou industrial.**

No ERPNext, as primeira Empresa é criada uma conta é criada. Para cada Empresa, voçê pode definir como Fabrico, Venda Retalho ou serviços dependendo da actividade do seu negocio.

Caso tenha mais que uma empresa, voçê pode adicionar por aqui:

> Home > Contabilidade > Empresa

## 1. Como criar uma nova Empresa
1. Vai para lista de Empresa, Click em Novo.
1. Digite o nome, abreviatura e a moeda por defeito da empresa.
1. Salvar.

A abreviatura para a sua empresa é criada por defeito. Por exemplo, FT para Frappe Technologies. A abreviatura ajuda em diferenciar os ativos de uma empresa em relação a outra.

A abreviatura tambem aparece na sua empresa em varias contas, centros de custo, modelos de impostos, armazens, etc. 

Voçê pode tambem adicionar o Logo da empresa e adiconar uma descrição da Empresa.

![Empresa Mestre](/docs/assets/img/setup/company-master.png)

### 1.1 Estrutura de Multi Empresa

Vamos assumir que voçê gere um grupo de empresas, algumas podem ser grandes e outras pequenas que fazem parte da empresa(s) grande.

No ERPNext, voçê pode adicionar varias empresas. A estrutura da empresa pode ser paralela, ex. sister companies, empresa mãe-filhos, ou uma combinação de ambas.

Uma empresa parente é uma empresa grande que consiste em ter uma ou mais empresas filhas. Um empresa filha é uma subsidiaria da uma empresa mãe.

A visão em arvore da empresa mostra a estrutura de todas as suas empresas.

<img class="screenshot" alt="Company Tree" src="{{docs_base_url}}/assets/img/accounts/company-tree.png">

Quando constroe uma arvore de empresa, o ERPNext vai validade se as contas das empresas filhas são iguais as contas das empresa parent. Todas as contas podem ser combinadas num plano de contas consolidado.

### 1.2 Outras Opções ao Criar a Empresa

* **Dominio**: O dominio de trabalho em que a empresa tem. Eg: fabrico, serviços, etc. Escolha uma ao configurar a sua conta.
* **É Grupo**: Caso selecionada, ficará a Empresa Mãe.
* **Empresa Mãe**: Caso seja uma empresa filha, digite a empresa maẽ aqui eg., selecione o grupo de empresa que ela pertença. Se uma empresa mãe existe, o plano de contas para anova empresa a ser criada será com base na empresa mãe.

### 1.3 Plano de Contas
Para cada Empresa, o Plano de Contas é mantido separado. Faz com tenha uma contabilidade separada para cada empresa de acordo as regras legais. Voçê pode importa plano de contas usando [Importar Plano de Contas](/docs/user/manual/pt/configuração/importar-plano-de-contas).

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa.png">

O ERPNext tem um Plano de Contas disponivel para alguns paise. Ao criar a nova Empresa, voçê pode escolher o Plano de Contas atravez de uma das seguintes opções.

* Plano de Contas Standard
* Baseado no Plano de Contas de um Empresa Existente

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa-2.png">

De nota que, se a Empresa mãe for selecionar ao criar a nova Empresa, o Plano de Contas será com base na empresa mãe.

### 1.4 Defaults
Dentro dos registo de Empresa, voçẽ pode definir valores iniciais para contas. Estas contas iniciais vão ajudar rapidamente a criar transações de contabilidade, aonde o valor inicial será da Empresa mestre. Assim que a empesa for criada, o Plano de Contas e Centro de Custo tambem são criados.

O seguintes valores iniciais podem ser posto para a empresa:

* Livro de Finanças Inicial
* Cabeçalho de Carta Inicial
* Lista de Feriados Inicial
* Horario de Trabalho Inicial
* Termos e Condições Inicial
* País
* NIF
* Data de Inicio

## 2. Funcionalidades
### 2.1 Metas de Vendas Mensal
Defina o numero da meta de vendas mensal na moeda da empresa, por exemplo, $10,000. Total de vendas mensal ficará visivel uma vez que as transações sejam feitas. Para saber mais[click here](/docs/user/manual/pt/configuração/configurar-objectivos-vendas-empresa).

### 2.2 Configurações da Contabilidade
Algumas da seguintes contas seram postas por defeito quando criar a empesa, outras pode ser criadas depois. As contas podem ser vistas no [Chart of Accounts](/docs/user/manual/pt/contabilidade/plano-de-contas). Este valores podem ser alterados depois caso seja necessário.

* Conta do Banco Inicial
* Conta do Dinheiro Inicial
* Conta de Recebimentos Inicial
* Conta de Arredondamento
* Arredondamento Centro de Custo
* Conta de Write Off
* Conta de Desconto Permitido
* Conta de Desconto Recebido
* Ganhos Cambiais / Conta de Perca
* Ganhos Cambiais não Realizados/Conta de Perca
* Conta de Pagamento Inicial
* Conta de Adiantamento a Funcionario Inicial
* Conta de Custo de Bens Vendidos Inicial
* Conta de Lucros Inicial
* Conta de Default Deferred Revenue
* Conta de Despesas Default Deferred Expense
* Conta de Pagamento Salario Inicial
* Conta de Pagamento de Reembolso de Despesas
* Conta de Centro de Custo Incial
* Limite de Credito
* Modelo de Termos de Pagamento Inicial

### 2.3 Configurações de Stock
Funcionalidade de Stock Perpetual leva as transações de Stock que tem impacto no livros de Contabilidade da Empresa. Saiba mais [aqui](/docs/user/manual/pt/inventario/perpetual-inventory). Está activo por defeito.

* Conta de Stocks Inicial
* Conta de Ajuste de Stock
* Stock Recebido Mas não Cobrado
* Despesas Incluidas no Valor Valuation

    ![Configuração de Stock na Empresa](/docs/assets/img/setup/company-stock-settings.png)

### 2.4 Configurações da Depreciação do Activos
Para gerir os activos da empresa, as seguintes contas são necessárias. Seram criadas por defeitas muitas delas. Podem ser vistas aqui [Plano de Contas](/docs/user/manual/pt/contabilidade/plano-de-contas).

* Conta de Depreciação Acumulada
* Conta de Depreciação de Despesas
* Registo para Depreciação de Activo Series (Journal Entry)
* Despesas Incluidas no Valor do Activo
* Conta de Ganhos/Percas Disposal de Activos
* Centro de Custo para Depreciação de Activos
* Conta de Capital em Curso
* Activos Recebidos Mas não Cobrados

    ![Depreciação de Activos](/docs/assets/img/setup/company-asset-depreciation.png)

### 2.5 HRA Settings

Define a componente inicial para os seguintes Componentes de Salario.

> Para um usuario Indiano, pondo o valor default nesta area ira ajudar nos calculos de Declaração de Impostos para Funcionario, especialmente o valor da Isenção.

* Componente Basico
* Componente HRA
* Arrear Component

### 2.6 Configuração do Bank Remittance

*Somente para India.*

Using the Payment Order feature (in Accounts), you can give a single document of transfer for multiple bank transfers. Updating value in the following fields will help you generate Bank Remittance in a format which can be accepted and can be also uploaded on the bank's portal.

Payment order allows a user to combine several payment entries/payment requests into a single document. Bank Remittance allows a user to send **that** single document to the bank as text format, this text format can be manually uploaded to Kotak bank payments platform.

Client Code and Product Code are codes given by the bank to you. This is required to be added in the text file as per the format specified by Kotak bank.


### 2.7 Orçamento
Excepção de Regra do Aprovador de Orçamento: A regra selionada aqui pode passar o valor das despesas aprovadas no orçamento.

### 2.8 Detalhes da Empresa
Para referencia, os seguintes detalhes da sua empresa pode salvos no ERPNext:

* Data de Inicio
* Telefone No
* Fax
* Email
* Pagina Web
* Endereço
* Detalhes de Registo (NIF)

> Nota: Quando definir o endereço aqui, é importante assinalar a caixa 'É o Endereço da Sua Empresa'.

![Endereço da Empresa](/docs/assets/img/setup/company-address.png)

**Para India**, different addresses can be added with different GSTIN numbers if the company has multiple locations. For example, if your company has offices in Mumbai, Delhi, and Bangalore, you'll have to add different addresses with different GSTIN numbers.

Ao salvar a empresa, os seguintes detalhes/acções ficam visiveis no dashboard:
![Empresa depois de Salvar](/docs/assets/img/setup/company-after-save.png)

**Detalhes de Registo**: Aqui voçê pode salvar imposto/check/numero do banco para referencia.

### 2.9 Apagando todas as Transações da Empresa
Voçê pode apagar todas as transações (Ordens, Facturas) de um Empresa. *Use com cuidado*, as transacções quando apagadas não podem ser recuperadas.

#### Requesitos

* O Usuário tem que ser um Gestor do Sistema
* O Usuário tem que ser o que criou a Empresa

#### Passos
1. Click no botão **Apagar Transações da Empresa**
1. Verificar a sua senha
1. Digitar o Nome da Empresa para confirmar
    ![Empresa depois de salva](/docs/assets/img/setup/company-delete-transactions.png)

E está feito. Os dados mestre como Item, Contas, Funcioanarios, LDM, etc vão permanecer.

#### O que vai afectar?

* Venda/Ordens de Compra/Recibos de Facturas/Guias seram apagadas
* As vendas mensais e o historico de vendas será limpo
* Todas as notificações seram limpas
* Endereços de Lead para o qual a Empresa esta ligada será apagada
* Todas as comunicações ligadas a Empresa seram apagadas
* Todos os All naming series seram zerados
* As Entradas de Stocks ligadas ao Armazem desta Empresa será apagado

### 3. Topicos Relacionados
1. [Configurar Impostos](/docs/user/manual/pt/configuração/configurar-impostos)
1. [Configurações do Sistema](/docs/user/manual/pt/configuração/configurações/configurações-sistema)
1. [Importar Plano de Contas](/docs/user/manual/pt/configuração/importar-plano-de-contas)
1. [Usuários e Permissões](/docs/user/manual/pt/configuração/usuarios-e-permissṍes)
1. [Adicionar Usuários](/docs/user/manual/pt/configuração/usuarios-e-permissões/adicionar-usuarios)
1. [Cabeçalho de Carta](/docs/user/manual/pt/configuração/impressão/cabeçalho-carta)
1. [Conta de Email](/docs/user/manual/pt/configuração/email/conta-email)
1. [Administrador](/docs/user/manual/pt/configuração/usuarios-e-permissões/administrador)
