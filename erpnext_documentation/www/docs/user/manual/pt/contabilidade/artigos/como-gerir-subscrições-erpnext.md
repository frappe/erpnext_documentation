<!-- add-breadcrumbs -->
# Como Gerir Subscrições com o ERPNext

O ERPNext agora permite gerir as suas subscriçãoes de forma facil. Uma simples subscrição pode conter varios planos. Ao mesmo tempo, 
uma unica subscrição pode ter varias subscrições. O ERPNext tambem gere automaticamente as suas subscrições gerando novas facturas 
quando proximo de expirar e alterando o Status para voçê.

## Doctypes Relacionados
### Subscritor
Como o nome sugere, o Doctype subscritor representa os seu subscritores e cada regist está ligado a um unico Cliente.

<img alt="Subscriber form" class="screenshot" src="{{docs_base_url}}/assets/img/articles/subscriber.png">

### Plano de Subscrição
Cada Plnao de Subscrição esta ligado a um unito Item e contem cobranças e informação de preços em cada Item. Voçê pode ter varios planos
 de subscrição para um unico Item. Um exemplo é a situação aonde voçê quer isto e quer preços diferentes para o mesmo Item como quando voçê 
 tem um opção basica e uma opção Premio para um serviço.

<img alt="Subscription Plan Form" class="screenshot" src="{{docs_base_url}}/assets/img/articles/subscription-plan.png">

### Configurações de Subscrição
Configurações de Subscrição é aonde voçê mexe com o comportamento do Dcotype da Subscrição. Por exemplo, voçê pode definir o tempo de graça para um factura.
Voçê pode tambem eleger ter uma subscrição cancelada se o periodo de tempo da factura expirou e não está paga..

<img alt="Subscription Settings Form" class="screenshot" src="{{docs_base_url}}/assets/img/articles/subscription-settings.png">

## Criando uma Subcrição
Para criar uma subcrição, vá para o formulario de Subscrição
`Explorar > Contabilidade > Subscrições`

<img alt="Subscription form" class="screenshot" src="{{docs_base_url}}/assets/img/articles/subscription-1.png">

Selecione um Subscritor.

Se voçê quer cancel a Subscrição no fim do present ciclo de cobrança, verifique a caixa 'Cancelar no Fim do Periodo'.

Selecione a Data de Inicio da subscrição. Por defeito, a data de inicio será a de hoje. (Opcional).

Se voçê estiver a dar uma subscrição de borla, digite o periodo de borla, Data de Inicio e Fim.

Se a sua factura não estiver paga, voçê pode definir o numero de dias antes da factura expirar no campo 'Dias Até Expirar'.

Se voçê precisa mais do que um plano, defina a 'Quantidade' no campo. Por exemplo, um desenvolvedor de Pagina está subscrito no seu serviço de hospedagem.
O desenvolvedor compra o plano para cliente. Em vez de ter varias subscrições para o mesmo plano, voçê pode simplesmente autmentar a quantidade necessaria.

Na table 'Plano', adicione os Planos de Subscrição necessarios. Voçê poide ter varios Planos de Subscrição numa unica Subscrição o tempo que durar o seu 
ciclo de cobrança. Se o mesmo Subscritor precisar de planos diferentes com ciclos de cobrança diferente, voçê terá de usar uma subscrição separada.

Selecione o Modelo de Impostos e Taxas de Venda se voçê precisa cobrar impostos nas suas facturas.

Preencha os campos necessarios na secção 'Descontos' se voçê precisa adicionar descontos as suas facturas.

Clique em Salvar.

### Status das Subscrições
As Subscrições no ERPNext tem cinco valores de estado:
- **Testando** - Uma subscrição que está em modo de testes
- **Activo** - Uma subscrição que não tem facturas não pagas
- **Expirada** - Uma subscrição na qual maioria das facturas não está paga mas dentro do periodo da data de expiração
- **Não Paga** - Uma subscrição no qual as facturas mais recentes não estão pagas e passou do periodo da data de expiração
- **Cancelada** - Uma subscrição na qual as factura mais recentes não estão pagas e passou do periodo da data de expiração. Neste estado, o ERPNext já não monotoriza a subscrição.

### Processamento da Subscrição no Background
A cada hora de intervalo, o ERPNext processa todas as Subscrições e actualiza cada alteração no estado. Irá criar facturas caso necessário. Quando facturas pendenntes são pagas, o ERPNext actualiza o estado das subscrições de acordo.

### Actualizar Subscrições Manualmente
Uma vez que salvou as subscrições, voçê pode alterar os campos 'Dias Até Expirar', 'Quantidade', 'Planos', 'Modelo de Impostos e Taxas de Vendas', 
'Aplicar Desconto Adiconal Em', 'Percentagem de Desconto Adicional' e 'Valor de Desconto Adicional'.

De notar que alterar qualquer valor irá reflectir somente nas novas Facturas. As facturas geradas anteriormente não sofrem qualquer alteração.

### Cancelando Subscrições
Para cancelar uma subscrição, simplesmente clique no botão 'Cancelar Subscrição'. A subscrição irá actualizar o seu campo 'Data de Cancelamento'
e a subscrição já não será monotorizada.

Se voçê cancelou uma subscrição activa, a factura será gerada imediatamente. A factura gerara será feita na base 
pro-rata por defeito. Se voçê quer que o ERPNext sempre crie as facturas pelo valor completo, remova a seleção no campo 'Prorate'
nas Configurações de Subscrição.

### Recomeçando as Subscrições
Para recomeçar uma subscrição cancelada, basta simplesmente fazer o clique no botão 'Recomeçar a Subscrição'. De notar que a subscrição irá apagar a tabela de facturas. 
Note que as factura ainda existiram mas a Subscrição já não irá restrear. A Data de inicio da subscrição tambem irá mudar para a data em a Subscrição foi reiniciada.
O inicio do ciclo de cobrança tambem será definido para a Data de reinicio da Subscrição.

### Recalculando a Subscrição
Algumas vezez, o estado da Subscrição pode ser altarado mas pode não ser reflectido na Subscrição. Voçê pode forçar o ERPNext a actualizar a subscrição fazer o clique 
'Obter Actualização das Subscrições'.

### Configurações de Subscrição
**Periodo de Graça** representa o numero de dias após uma factura de subscrição expirar que o ERPNext deve atrasar antes de mudar o estado da subscrição para 
'Cancelado' ou 'Não Paga'.

**Cancelar uma Factura Depois do Periodo de Graça** irá fazar com que o ERPNext automaticamente cancele uma subscrição caso não esteja paga antes dos termino do periodo. Esta configuração está desactiva por defeito.

**Pro rata** irá fazer com que o ERPNext gere uma factura pro rata quando uma subscrição activa é cancelada por defeito.
Se preferir uma factura completa, desactive esta opção nas configurações.

{next}
