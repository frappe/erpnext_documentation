<!-- add-breadcrumbs -->
# Estrategia de Implementação

Antes de começar a gerir as suas Operações no ERPNext, voçê deve se familiarizar
com o sistema e os termos usados. para isto nós recomendamos que a
implementação deve ser feita em duas fases.

  * Uma **Fase de Teste**, aonde voçê entra registos burros para representar o seu dia a dia de transações e um **Teste de Produção**, aonde vai iniciar os seus dados reais.

### Fase de Teste

  * Leia o Manual
  * Crie uma conta livre no [https://erpnext.com](https://erpnext.com) (a forma mais facil de experimentar).
  * Crie o seu primeiro Cliente, Fornecedor e Item. Adicione alguns mais para se familiarizar.
  * Crie Grupo de Clientes, Grupo de Itens, Armazens, Grupo de Fornecedores, para classificar os Itens.
  * Complete o ciclo normal de vendas - Lider > Oportunidade > Proforma > Ordem de Vendas > Guia de Remessa > Factura de Vendas > Pagamento (Jornal de Entrada)
  * Complete o ciclo normal de compras - Requisição de Material > Ordem de Compra > Recibo de Compra > Pagamento (Jornal de Entrada).
  * Complete o ciclo de fabrico (caso necessário) - LDM > Ferramenta de Produção > Ordem de Trabalho > Pedido de Material
  * Crie um cenario real do dia a dia no sistema.
  * Crie campos customizados, formato de impressão, etc caso necessário.

### Teste de Produção

Uma vez familiar com o ERPNext, começe por inserir os seus dados!

  * Limpe a conta de testes ou melhor começe uma nova instalação.
  * Caso queira somente limpar as transações e não os seus ficheiros mestres como Item, Clientes Fornecedor, LDM, etc, voçê pode apagar as transações da sua Empresa e começar do zero. Para tal,abra o Registo de Empresa pelo Contabilidade > Mestre Contábeis > Empresa e apague as transações da empresa fazendo o click no botão **Eliminar Transações da Empresa** no fim do formulário da Empresa.
  * Voçê pode configurar uma nova conta em [https://erpnext.com](https://erpnext.com), e usar por 14-day de teste. [Encontre outras formas de instalar o ERPNext](iniciando-com-erpnext)
  * Configurar todos os modulos com Grupo de Clientes, Grupo de Itens, Armazens, LDM, etc.
  * Importe Clientes, Fornecedores, Itens, Contactos e Endereços usando a Ferramento de Importação de Dados.
  * Importe stocks de abertura usando a Ferramenta de Reconciliação de Stocks.
  * Crie entradas de abertura de saldo pelo Jornal de Entrada e crie Factura de Vendas e Compras de inicio/abertura.
  * Caso precise de ajuda, [voçê pode comprar o suporte](https://erpnext.com/pricing) ou [peça no forum de usuário](https://discuss.erpnext.com).

{next}
