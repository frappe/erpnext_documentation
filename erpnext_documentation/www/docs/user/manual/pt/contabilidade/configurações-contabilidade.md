<!-- add-breadcrumbs -->
# Configurações de Contabilidade

Existem varias contigurações de contabilidade no ERPNext para restringir e configurar acções no modulo de Contabilidade.

![Configurações de Contabilidade]({{docs_base_url}}/assets/img/accounts/account-settings.png)

## 1. Contas Congeladas Até
Congelar transações contabilisticas até uma certa data, aonde ninguem pode criar/modificar os registos excepto quem tevir a Permissão certa.

## 2. Perfil Autorizado para Definir as Contas Congeladas e Editar Registos Congelados
Usuários com este Perfil estão autorizados a definir as contas congeladas e criar/modificar registos de contas contra estas contas congeladas.

## 3. Determinar o Endereço do Formulario de Categoria de Imposto
[Categoria do Imposto](/docs/user/manual/pt/contabilidade/categoria-imposto) pode ser definido nos Endereços. Um Endereço pode ser de Envio ou Cobrança. Definina o endereço a usar quando aplicar a Categoria do Impostos.

## 4. Percentagem Permitida Ultrapassada de Cobrança
A percentagem pelo qual pode utrapassar nas cobranças. Por exemplo, caso a valor da ordem é de $100 para um Item e a percentagem aqui está para 10% então voçê está permitido a cobrar $110.

## 5. Controlador de Credito
Selecione o perfil que está autorizado a submeter transações que excedam o limite de credito definido. O limite de Credito pode ser definido no Formulario de Cliente.

## 6. Verificar o Numero de Factura de Fornecedor Unico
Quando activo, Factura de Compra com o mesmo 'Numero da Factura de Fornecedor' não será autorizado para evitar registo duplicados. 

## 7. Fazer Pagamento atravez do Lançamento de Contabilistico
Quando activo, e se o usuario proseguir com o pagamento para um factura, o sistema irá abrir o Lançamento Contabilistico em vez do Registo de Pagamento.

## 8. Desvincular o Pagamento no Cancelamento de uma Factura
Caso activo, o sistema irá desvincular o pagamento conra a respectiva factura. Por defeito, se um Registo de Pagamento é submetido, a factura vinculada não pode ser cancelada até que o Registo de Pagamento tambem o seja. Ao desvincular, voçê pode cancelar e emender as facturas. Mas os pagamentos não vinculados são considerados como adiantamento de Pagamento. But the payments not be linked and considered as advance payments.

## 9. Desvincular Adiantamento de Pagamento no Cancelamento de um Ordem
Similar a opção anterior, este desvincula qualquer adiantamento de pagamento feito contra uma Compra/Ordem de Venda. 


## 10. Entrada de Depreciação Automatica de Activos
Quando activo, um registo automatico para a depreciação de um activo será criado baseado na data definida. Por exemplo, depreciação anual para um item será agendada para os proximos 3/4 anos baseados no Numero de Depreciações Agendadas no Registo Mestre de Activos. Para mais detalhes, visite a pagina [Depreciação de Activos](/docs/user/manual/pt/activos/depreciação-activos).

## 11. Permitir Centros de Custo nas Contas de Registo da Folha de Balanço
Caso activo, o sistema irá permitir o usuário marcar os registos nas Contas de Registo da Folha de Balanço contra o Centro de Custo. Por defeito o Centro de Custo está disponivel somente para contas de Lucros/Percas.

## 12. Adicionar Automaticamente Impostos e Taxas apartir do Modelo de Impostos do Item
Activando irá preencher as tabelas de Impostos nas transações caso algum [Modelo de Imposto de Item](/docs/user/manual/pt/contabilidade/modelo-imposto-item) seja definido para um Item e essa Item for selecionado para a transação.

## 13. Busca Automaticamente os Termos de Pagamento
Activando este irá automaticamente buscar os Termos de Pagamento baseados no Fornecedor. 

## 14. Configurações de Impressão

![Configurações de Contabilidade]({{docs_base_url}}/assets/img/accounts/account-settings-1.png)

* **Mostrar ao Imprimir Inclusivo de Imposto**: O imposto aplicado será mostrado ao imprimir.
* **Mostrar ao Imprimir o Agendamento de Pagamento**: A table de Agendamento de Pagamento está visivel ao usar [Termos de Pagamento](/docs/user/manual/pt/contabilidade/termos-pagamento). Activando isto irá mostrar esta tabela ao imprimir.

## 15. Permitir Taxa de Cambio Fixa/Parada Allow Stale Exchange Rate
Deve estar não activo caso voçê queira que o ERPNext verifique o tempo dos registo procurados apartir da Taxa de Cambio em transações de Moedas estrangeiras. Caso não activo, o campo taxa de cambio será de leitura somente nos documentos.

Dias Parados é o numero de dias para usar até decidir se o registo da Taxa de Cambio é Fixo. É valido quando 'Permitir Cambios Parados' está **desactivo**. Portanto, caso os Dias Parados for 10, as taxa fixas que tem 10 dias serao permitidas. Caso Permitir Cambios Parados estiver activo, então não tem um tempo limit na idade das Taxas paradas.

Caso as taxas paradas estiverem activas, a forma de procura é:

* Ultima taxa de cambio apartir do Formulario Taxa de Cambio
* Se não tiver uma Taxa de Cambio a ultima taxa do mercado será adicionada automaticamente

Caso as taxas paradas estiver desactiva, a ordem de procura é:

* Ultima taxa apartir do Formulario Taxa de Cambio até o numero de dias definido no 'Dias Parados'
* Cas não tiver uma Taxa de Cambio a ultima tax de acordo o mercado será adicionada automaticamente


## 16. Usar o Formato de Fluxo de Caixa
Voçê pode escolher em usar os Formatos de Fluxo de Caixa Customizados para customizar como o Relatorio de Fluxo de Caixa irá ficar. Para saber mais, [visita esta pagina](/docs/user/manual/pt/contabilidade/artigos/como-customizar-relatorio-de-fluxo-de-caixa).