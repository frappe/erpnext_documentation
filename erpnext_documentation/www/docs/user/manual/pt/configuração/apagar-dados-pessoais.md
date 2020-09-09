<!--add breadcrumbs-->

# Eliminação de Dados Pessoais

Sendo parte do GDPR de cumplicadade, o ERPNext tem a Eliminação de DAdos Pessoais.

Ferramenta para Eliminar os Dados Pessoais permite um utilizador eliminar todos os dados que um usuário tenha gerado usando o ERPNext. Quer dizer dados pessoais indentificados. That is, personally identifiable information will be randomized. Isto inclue dados pessoais indentificados pela conta do usuário como: usuário, nome completo, data de nascimento, numero de telefone, movel, localização, interesses, biografica, Email, Contactos, Endereços, Comunicações, etc. Inclue tambem dados de Leads e Oportunidades, os detalhes que salvou como numero de telefone, movel, fax, pagina web, e nome.

Contudo, excluindo os dados exigidos pela lei para manter o negocio.

## 1. Como pedir para apagar os dados do usuário

1. Para apagar os dados, voçê precisa visitar  [host-name]/request-to-delete-data (e.g. example.erpnext.com/request-to-delete-data) no caminho URL.

    <img class="screenshot" alt="Request Data Webform" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/request-to-delete-data-webform.png">

2. Digite o email associado a sua conta ERPNext. Depois de submeter o pedido, irá receber uma resposta de sucesso..

    <img class="screenshot" alt="Deletion Request Success" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/deletion-request-success.png">

3. Será enviado um email com o link de verificação para apagar os dados para a conta de emails associada ao usuário.

    <img class="screenshot" alt="Verification Email" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/verification-email.png">

4. Uma vez que o usuário fizer o click no link de verificação. Uma mensagem de confirmação será mostrada.
    <img class="screenshot" alt="Confirmed Verification" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/confirmed-verification.png">

## 2. Como funciona o apagar dados pessoais

O pedido para apagar os dados é guardado num doctype "Pedido para Apagar Dados Pessoais".

<img class="screenshot" alt="Personal Data Download Request Doctype" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/personal-data-deletion-request-doctype.png">

Este doctype mantem três estados para completar o processo de eliminação dos dados do usuário.

### 2.1 Verificação Pendente
Este estado significa que o usuário fez um pedido para apgar via web-form. Contudo, a verificação deste pedido ainda está pendente. Procure pelo Pedido de Eliminar Dados Pessoais na barra de procura.

<img class="screenshot" alt="Pending Verification" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/pending-verification.png">

### 2.2 Aprovação Pendente
Este indica que o usuário verificou o pedido por email. Este habilita a opção de "Apagar Dados" para os Gestores de Sistema.

<img class="screenshot" alt="Pending Approval" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/pending-approval.png">

### 2.3 Eliminados
Este indica que o Gestor de Sistema fez o click sobre o botão "Apagar Dados". Significa que os dados pessoais do usuário foram completamente eliminados.

<img class="screenshot" alt="Deleted User" src="{{docs_base_url}}/assets/img/setup/personal-data-deletion-request/deleted-user.png">

### 3. Topicos Relacionados
1. [Descarregar Dados Pessoais](/docs/user/manual/pt/configuração/descarregar-dados-pessoais)

