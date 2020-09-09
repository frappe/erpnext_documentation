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

A visão em arvore da empresa mostra a estrutura de todoas as suas empresas.

<img class="screenshot" alt="Company Tree" src="{{docs_base_url}}/assets/img/accounts/company-tree.png">

Quando constroe uma arvore de empresa, o ERPNext vai validade se as contas das empresas filhas são iguais as contas das empresa parent. Todas as contas podem ser combinadas num plano de contas consolidado.

### 1.2 Outras Opções ao Criar a Empresa

* **Dominio**: O dominio de trabalho em que a empresa tem. Eg: fabrico, serviços, etc. Escolha uma ao configurar a sua conta.
* **É Grupo**: Caso selecionada, ficará a Empresa Mãe.
* **Empresa Mãe**: Caso seja uma empresa filha, digite a empresa maẽ aqui eg., selecione o grupo de empresa que ela pertença. Se uma empresa mãe existe, o plano de contas para anova empresa a ser criada será com base na empresa mãe.

### 1.3 Plano de Contas
Para cada Empresa, o Plano de Contas é mantido separado. Faz com tenha uma contabilidade separada para cada empresa de acordo as regras legais. Voçê pode importa plnao de contas usando [Importar Plano de Contas](/docs/user/manual/pt/configuração/importar-plano-de-contas).

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa.png">

ERPNext has localized Chart of Accounts readily available for some countries. When creating a new Company, you can choose to set up the Chart of Account for it from one of the following options.

* Standard Chart of Accounts
* Based on Existing Company's Chart of Account

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa-2.png">

Note that, if the Parent Company is selected when creating a new Company, the Chart of Accounts will be created based on the existing Parent Company.

### 1.4 Defaults
Within the Company master, you can set many of the default values for masters and accounts. These default accounts will help you in the quick posting of accounting transactions, where the value for the account will be fetched from the Company master if provided. As soon as the company is created, a default Chart Of Accounts and Cost Center is automatically created.

The following defaults can be set for a company:

* Default Finance Book
* Default Letter Head
* Default Holiday List
* Standard Working Hours
* Default Terms and Conditions
* Country
* Tax ID
* Date of Establishment

## 2. Features
### 2.1 Monthly Sales Target
Set the monthly sales target number in the company currency, for example, $10,000. Total monthly sales will be visible once transactions are made. To know more [click here](/docs/user/manual/pt/configuração/setting-company-sales-goal).

### 2.2 Account Settings
Some of the following accounts will be set by default when you create a new company, others can be created. The accounts can be seen in the [Chart of Accounts](/docs/user/manual/pt/accounts/chart-of-accounts). These values can be changed later on if needed.

* Default Bank Account
* Default Cash Account
* Default Receivable Account
* Round Off Account
* Round Off Cost Center
* Write Off Account
* Discount Allowed Account
* Discount Received Account
* Exchange Gain / Loss Account
* Unrealized Exchange Gain/Loss Account
* Default Payable Account
* Default Employee Advance Account
* Default Cost of Goods Sold Account
* Default Income Account
* Default Deferred Revenue Account
* Default Deferred Expense Account
* Default Payroll Payable Account
* Default Expense Claim Payable Account
* Default Cost Center
* Credit Limit
* Default Payment Terms Template

### 2.3 Stock Settings
Perpetual Inventory feature would lead to Stock transactions impacting the company's books of accounts. Know more [here](/docs/user/manual/pt/stock/perpetual-inventory). It is enabled by default.

* Default Inventory Account
* Stock Adjustment Account
* Stock Received But Not Billed
* Expenses Included In Valuation

    ![Stock Settings in Company](/docs/assets/img/setup/company-stock-settings.png)

### 2.4 Fixed Asset Depreciation Settings
For managing fixed assets in a company, the following accounts are needed. Most of them will be created by default. They can be seen in the [Chart of Accounts](/docs/user/manual/pt/accounts/chart-of-accounts).

* Accumulated Depreciation Account
* Depreciation Expense Account
* Series for Asset Depreciation Entry (Journal Entry)
* Expenses Included In Asset Valuation
* Gain/Loss Account on Asset Disposal
* Asset Depreciation Cost Center
* Capital Work In Progress Account
* Asset Received But Not Billed

    ![Fixed Asset Depreciation](/docs/assets/img/setup/company-asset-depreciation.png)

### 2.5 HRA Settings

Set the default Component for the following Salary Components.

> For the Indian user, setting the default value in this section will help in Employee Tax Declaration calculations, especially for HRA exemption amount.

* Basic Component
* HRA Component
* Arrear Component

### 2.6 Bank Remittance Settings

*Only for India.*

Using the Payment Order feature (in Accounts), you can give a single document of transfer for multiple bank transfers. Updating value in the following fields will help you generate Bank Remittance in a format which can be accepted and can be also uploaded on the bank's portal.

Payment order allows a user to combine several payment entries/payment requests into a single document. Bank Remittance allows a user to send **that** single document to the bank as text format, this text format can be manually uploaded to Kotak bank payments platform.

Client Code and Product Code are codes given by the bank to you. This is required to be added in the text file as per the format specified by Kotak bank.


### 2.7 Budget
Exception Budget Approver Role: The role selected here can bypass the set budget to approve expenses.

### 2.8 Company Info
For reference, the following details of your company can be saved in ERPNext:

* Date of Incorporation
* Phone No
* Fax
* Email
* Website
* Address
* Registration Details

> Note: When setting the address here, it is important to tick the 'Is Your Company Address' checkbox.

![Company Address](/docs/assets/img/setup/company-address.png)

**For India**, different addresses can be added with different GSTIN numbers if the company has multiple locations. For example, if your company has offices in Mumbai, Delhi, and Bangalore, you'll have to add different addresses with different GSTIN numbers.

On saving a company, the following details/actions will be visible in the dashboard:
![Company after Save](/docs/assets/img/setup/company-after-save.png)

**Registration Details**: Here you can save various tax/cheque/bank number for reference.

### 2.9 Deleting all Company Transactions
You can delete all transactions (Orders, Invoices) of a Company. *Use with caution*, transactions once deleted cannot be recovered.

#### Requirements

* The User has to be a System Manager
* The User has to be the creator of the Company

#### Steps
1. Click on the **Delete Company Transactions** button
1. Verify your password
1. Enter Company name for confirmation
    ![Company after Save](/docs/assets/img/setup/company-delete-transactions.png)

And you're done. The master data like Item, Account, Employee, BOM etc. will remain as it is.

#### What is affected?

* Sales/Purchase Orders/Invoices Receipts/Notes will be deleted
* The monthly sales and sales history will be cleared
* All notifications will be cleared
* Lead Addresses to which the Company is linked will be deleted
* All communications linked to the Company will be deleted
* All naming series will be reset
* Stock Entries linked to a Warehouse of this Company will be deleted

### 3. Related Topics
1. [Setting Up Taxes](/docs/user/manual/pt/configuração/setting-up-taxes)
1. [System Settings](/docs/user/manual/pt/configuração/settings/system-settings)
1. [Charts Of Accounts Importer](/docs/user/manual/pt/configuração/chart-of-accounts-importer)
1. [Users and Permissions](/docs/user/manual/pt/configuração/users-and-permissions)
1. [Adding Users](/docs/user/manual/pt/configuração/users-and-permissions/adding-users)
1. [Letter Head](/docs/user/manual/pt/configuração/print/letter-head)
1. [Email Account](/docs/user/manual/pt/configuração/email/email-account)
1. [Administrator](/docs/user/manual/pt/configuração/users-and-permissions/administrator)
