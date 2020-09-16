<!-- add-breadcrumbs -->
# Como Customizar o Relatorio Fluxo de Caixa

Como o seu Plano de Contas começa a ficar mais complexo e normas de relatorios mudam constantemente, o relatorio fluxo de caixa padrão pode não ser suficiente. Isto porque o ERPNext pode não consiguir adivinhar a classificação e proposito de todas as contas no plano de contas. Por outra voçê pode ter de ajustar o relatorio para ir de acordo as suas necessidades.

Isto já não é um problema porque o ERPNext permite ao usuario customizar o relatorio de fluxo de caixa.


## Revisão Tecnica
Customização é possivel devido a introdução de dois novos tipo de doctypes - Cash Flow Mapper e Cash Flow Mapping. Ambos
contem a informação necessario para gerar um relatorio do fluxo de caixa.

O Cash Flow Mapping mostra como as contas no plano de contas estã mapeadas a linha de itens no seu relatorio fluxo de caixa enquanto 
que Cash Flow Mapper obtem todos os Cash Flow Mappings que se relacionam as três secções do extracto do fluxo de caixa.

Com isto, voçê gera relatorios de fluxo de caixa detalhados de acordo os seus requesitos. Pode não fazer muito sentido mas depois irá quando passarmos
por um exemplo.

## Exemplo
### Informação Background
Vamos assumir que temos uma empresa ficticia para o qual queremos gerar o relatorio de fluxo de caixa.
Este é como o relatorio de fluxo de caixa fica no momento:
<img alt="Default cash flow report" class="screenshot" src="{{docs_base_url}}/assets/img/articles/default-cash-flow-report.png">

Nós não gostamos do relatorio pelas seguintes razões:
- O formato do relatorio é feio.
- Os numeros do 'Caixa Liquido das Operações' estão errados

### Processo de Customização

Nós queremos que o relatorio de Fluxo de Caixa se pareça ao formato em baixo:
<img alt="cash flow format 1" class="screenshot" src="{{docs_base_url}}/assets/img/articles/format-1.png">
<img alt="cash flow format 1" class="screenshot" src="{{docs_base_url}}/assets/img/articles/format-2.png">

#### Activar o Relatorio Customizado do Fluxo de Caixa
Faça isto nas configurações de Contabilidade fazendo o clique na caixa 'Usar Formato Customizado do Fluxo de Caixa'. Isto fará o ERPNext usar
somente o seu formato customizado para este relatorio.

Depois disto, o seu relatorio de fluxo de caixa irá se parecer assim:
<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/no-mappers.png">

Mova para a proxima secção para construir o relatorio.

#### Criar Mapeamento do Fluxo de Caixa
Para cada linha, nós precisamos criar um mapeamento do documento.

<img alt="new cash flow mapping form" class="screenshot" src="{{docs_base_url}}/assets/img/articles/new-cash-flow-mapping.png">

Voçê pode pensar no Mapeamento do Fluxo de Caixa como a representação de cada linha no relatorio. Um Mapeamento do Fluxo de Caixa
é um filho do Cash Flow Mapper que será explicado depois. 

Vamos começar por criar o Mapeamento Fluxo de Caixa que ira representar despesas de caixa reconhecidas no extracto
de Lucros e Perdas. Nós queremos que apareçam no extracto de caixa como:
- Recebimentos de Impostos reconhecidos nos lucros ou perdas
- Custos Financeiros reconhecidos no lucros ou perdas
- Depreciação de activos não correntes

Começe por abrir um novo formulario Mapeamento Fluxo de Caixa.

Os campos no doctype Mapeados do Fluxo de Caixa são:
- **Nome**: É algo para identificar o documento. Nome é algo relacionado ao label
- **Label**: Este é o que irá aparecer no extracto do fluxo de caixa
- **Contas**: Esta tabela contem todas as contas que esta linha se relaciona com.

Com esta informação, vamos em frente e criar o Documento Mapeamento Fluxo de Caixa para a linha 'Recebimentos de Impostos reconhecidos em lucro ou perdas'

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-1.png">

Eu dei o nome de 'Taxa de Imposto de Recebimentos' e dei o label 'Recebimentos de Impostos reconhecidos em lucro ou perdas'. Nós queremos esta
linha para reflectir Taxas de Impostos de Recebimentos dos extractos dos nossos lucros ou perdas. A conta aonde acontece no nosso grafico plano de
contas é 'Imposto de Recebimentos' (uma despesa) que i adicionei 'Imposto de Recebimentos' na tabela de contas. Se voçẽ tiver mais
contas representando Imposto de despesas de recebimentos, voçê deve adicionar todos aqui.

Porque Imposto de Despeas de Recebimento precisa ser ajustado no extracto de fluxo de caixa, verifique a caixa 'É um Imposto de Despesa de Recebimento'.
Assim será o que irá ajudar o ERPNext a calcular correctamente os ajustamentos a serem feitos.

*Para melhores resultados, deixe as contas mãe ter contas filho que tem o mesmo tratamento para o relatorio fluxo de caixa
porque o ERPNext irá calcular a alteração liquida de todas as contas filho numa situação aonde as contas selecionadas são contas mãe.* 

Da mesma forma, que eu criei os outros dois mapeamentos em falta.

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-2.png">

Custo Financeiro tambem precisa de ser ajustado portanto tenha a certeza de marcar a caixa 'É Custo Financeiro'.

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-3.png">

Proximo iremos adicionar o Mapeamento Fluxo de Caixa para itens que mostram alterações no Capital Corrente:
- Aumento/(redução) em outras responsabilidades
- (Aumento)/redução em trocas e outros recebimentos
- Aumento/(redução) em trocas e outros pagamentos
- Pagamento IVA
- (Aumento)/redução em inventario

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-4.png">

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-5.png">

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-6.png">

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-7.png">

<img alt="custom cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-8.png">

Não se esqueça de dizer ao ERPNext que estes mapeamentos representam alterações ao long do capital em curso selecionando a caixa 'É Captial em Curso´.

Neste momento nós criamos todos os mapeamentos necessários para a secção de Operações de Actividades para o nosso extracto dofluxo de caixa.
Contudo, o ERPNext não sabe que criamos documentos de Mapeamento de Fluxo de Caixa. Nós iremos criar os documentos de Fluxo de Caixa a seguir.


#### Criar Mapeamentos Fluxo de Caixa
Mapeamento Fluxo de Caixa representam secções no extracto de fluxo de caixa. Um extracto normal do fluxo de caixa tem trê secções
portanto quando vir a lista de Mapeamentto, irá ver que foram criados três :
- Actividades de Operações
- Actividades Financeiras
- Actividades de Investimento

Voçẽ não poderá adiconar ou remover qualquer um mas eles podem ser editados e renomeados.
<img alt="cash flow mapper list" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapper-2.png">


Abra Operação de Actividades de Mapeamento de Fluxo de Caixa para que possamos adiconar os mapeamentos criados.


- **Nome da Secção**: Este é o cabeçalho da secção.
- **Leader da Secção**: Este é o primeiro Sub-cabeçalho depois dos numeros de lucro. Referentes somente as Operações de Actividades do Mapeamento
Fluxo de Caixa
- **Secçao Subtotal**: Este é o label para o subtotal na secção do extracto do fluxo de caixa. Referente somente as Operações de Actividades
do Mapeamento do Fluxo de Caixa
- **Secção do Rodapé**: Este é o label para o total na secção do extracto do fluxo de caixa.
- **Mapeamento**: Esta tabela contem todos os Mapeamentos de Fluxo de Caixa referentes ao Cash Flow Mapper.

Agora todos os Mapeamentos foram criados e salvos. Voçẽ deve ter algo assim:
<img alt="cash flow mapper for operating activities" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapper-4.png">

 Recarregue o extracto de fluxo de caixa e verifique as modificações.
<img alt="updated cash flow report" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapper-3.png">

Esta proximo as requesitos mas ainda falta. Crie um novo mapeamento para as secções 'Actividades de Investimento' e 'Actividades de Financiamento' 
para o extracto do fluxo de caixa.

<img alt="cash flow mapping" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-9.png">

<img alt="cash flow mapping" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapping-10.png">

<img alt="cash flow mapper for operating activities" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapper-5.png">

<img alt="cash flow mapper for operating activities" class="screenshot" src="{{docs_base_url}}/assets/img/articles/cash-flow-mapper-6.png">

Aqui esta como o nosso extracto de fluxo de caixa se parece:
<img alt="final cash flow statement" class="screenshot" src="{{docs_base_url}}/assets/img/articles/final-cash-flow.png">
