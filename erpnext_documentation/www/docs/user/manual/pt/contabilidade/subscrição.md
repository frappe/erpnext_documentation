<!-- add-breadcrumbs -->
# Subscrição

Se voçê oferece um serviços que requer renovção num certo periodo de tempo ou voçê paga despesas mensais como renda (anual, mensal, trimestral), voçê pode usar a funcionalidade de Subscrição no ERPNext para rastrear eles. A tabela de Subscrição capta todos os detalhes necessários para a auto-criação de Facturas de Venda ou Compra.

Vamos considerar o caso de Subscrição no ERPNext. Os nossos plano de hosting estão disponveis em base anual. Cada conta de Cliente tem uma data de expiração, que depois os clientes podem renovar as suas Subscrições.

Para gerir a Subscrição dos clientes e auto-gerar a renovação das Factura de Venda, nós usamos a funcionalidade de Subscrição.

Para aceder a lista de Subscrição, vá para:
> Home > Contabilidade > Gestão de Subscrição > Subscrição

## 1. Pre-requisitos
Antes de usar e criar uma Subscrição, é aconselhavel criar o seguinte:

1. [Plano de Subscrição](/docs/user/manual/pt/contabilidade/plano-subscrição)

## 2. Como definir uma Subscrição
1. Vá para a lista de Subscrição e clique em Novo.
1. Selecione o Tipo de Parte como 'Cliente' ou 'Fornecedor' e selecione a parte.
1. Defina a Data de Inicio para subscrição ficar activa.
1. Opcionalmente voçê pode tambem digitar o fim da data da subscrição se souber quando terminar.
1. Dias até termino é o numero de dias no qual o Cliente tem de pagar uma Factura de Vendas criada.
1. Selecione o [Plano de Subscrição](/docs/user/manual/pt/contabilidade/plano-subscrição).
1. Salvar.
 ![Subscrição](/docs/assets/img/accounts/subscription.png)

Baseado na data de inicio e fim da subscrição, as datas actuais das facturas serão calculadas.

## 3. Funcionalidades
### 3.1 Periodo de Teste
Se voçẽ estiver a oferecer um period de teste para uma subscrição, a Data de Inicio e Fim do Periodo de Teste pode ser definido. Facturas não serão geradas durante este periodo e o status da Subscrição irá mostrar 'Testando'.
![Subscrição de Teste](/docs/assets/img/accounts/subscription-trial.png)

### 3.2 Cancelar a Auto Renovação
Ao activar o 'Cancelar ao Fim do Periodo' a Subscrição irá ser cancelada no fim do seu periodo. Por exemplo, se for uma subscrição anual, o sistema irá parar de gerar facturas depois de um ano de subscrição.

### 3.3 Impostos
Voçê pode aplicar Impostos as Subscrições usando o Modelo de Impostos de Vendas e Taxas. Visite a pagina [Modelo de Impostos e Taxas de Vendas](/docs/user/manual/pt/vendas/modelo-impostos-taxas-vendas) para saber mais.

### 3.4 Aplicando Descontos
Voçê pode aplicar descontos adiconais na Subscrição baseado no Total Geral (antes do imposto) ou Total Liquido (depois do imposto). Um desconto de percentagem pode ser definid tambem. Por exemplo, um desconto de 2% em 12,000 seria de 240 o valor.
 ![Desconto de Subscrição](/docs/assets/img/accounts/subscription-discount.png)
Visite a pagina [Aplicando Desconto](/docs/user/manual/pt/vendas/artigos/aplicando-desconto) para mais detalhes.

### 3.5 Crie Facturas Automanticamente
Baseado no intervalo [Planos de Subscrição](/docs/user/manual/pt/accounts/subscription-plan), facturas podem ser criadas automaticamente. O 'Gerar Factura no Inicio do Periodo' precisa estar activo se voçê quiser gerar facturas assim que a subscrição estiver activa. Se "Gerar Novas Facturas Após Data de Expiração" estiver activo então novas facturas serão criadas apesar das facturas correntes não estarem pagas ou a data de expiração terminou.
 ![Subscrição de Facturas](/docs/assets/img/accounts/subscription-invoices.png)

### 3.6 Siga os Meses dos Calendario
Se 'Siga os Meses do Calendario' estiver activo então os meses do calendario serão seguidos mesmo que a Data de inicio da Subscrição seja no meio do mês. Por ex. Suponhamos que o intervalo de cobrança seja 'Mensal' e o intervalo de cobrança seja 3 no plano de subscrição e a Data de Inicio da Subscrição seja '15-04-2020' então se estiver activo 'Seguir Meses do Calendario' a primeira factura será gerada em '15-04-2020' para '30-06-2020' em vez de '15-04-2020' para '14-07-2020'

### 3.8 Cancelando uma Subscrição
Se o Cliente decide cancelar a Subscrição, pode ser cancelado no sistema usando o **Cancelar Subscrição**. O sistem irá parar de gerar facturas quando a Subscrição for cancelada.
 ![Cancelamento de Subscrição](/docs/assets/img/accounts/subscription-cancel.png)

### 3.9 Actualizando um Subscrição
Clique no botão **Procurar Actualização de Subscrição** irá actualizar a Subscrição com as ultimas facturas geradas.

## 4. Diferença entre Subscrição e Auto-Repetição

| Auto Repetição | Subscrição    |
|----------------|---------------|
| É aplicada em transações | É aplicada em Itens |
| Multiplas Transações como Ordem de Vendas, Ordem de Compra, Facturas, Lançamento Contabilistico, etc. são auto criadas | Somente Facturas de Venda e Compra são auto-criadas |
| Tem alguns controles | Tem muitas opções de controle para definir testes, data de expiração de cobrança e criar Planos de Subcrição |

### 5. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Facturas de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
1. [Item](/docs/user/manual/pt/inventario/item)
1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Plano de Subscrição](/docs/user/manual/pt/contabilidade/plano-subscrição)