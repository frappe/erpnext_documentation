<!-- add-breadcrumbs -->
# Configurando Dedução de Imposto de Renda
Calculando Dedução de Imposto de Renda para vários funcionários todos os meses é um consumo de tempo enorme para muitas empresas, especialmente as grandes empresas. Se bem configurado, o ERPNext simplifica muito dos calculos de Imposto automaticamente calculando as deduçoes de imposto ao gerar o salario. Aqui esta como configurar o ERPNext para facilitar o seu processamento de salario -

# Isenção de Imposto de Renda
Em muitos países, especialmente na India, as leis permitem isenção de uma parte (ou toda) de alguns gastos por individuos para que não seja adicionado ao Imposto de Renda anual. Exemplos de tais gastos podem ser contribuições para Obras de caridade, o valor gasto na educação das crianças, investimentos especificos, etc. Para retirar a isenção do Imposto de Renda, os indivíduos devem submeter provas de tais gastos.

O ERPNext pmerite voce configurar as Lajes de Imposto de Renda e o imposto é calculado com base nos rendimentos anuais projectados do funcionario. Para isto, os fucnionarios devem clarar o valor da isenção que eles planeam reivindicar no inicio do ano financeiro para que as deduções do salario para o imposto seja calculado. Funcionarios pode declarar por aqui [Declaração de Isenção de Imposto Funcionário](/docs/user/manual/pt/recursos-humanos/declaração-de-isenção-de-imposto-funcionário).

Se não tiver uma declaracao submetida pelo funcionario, as deduções do mês serão calculadas sem qualquer isenção apartir dos ganhos anuais do funcionario. Contudo, se for submetida a declaracao entre o periodo de salario, a isenção de iposto será aplicada no proximo processamento de salario. Qualquer imposto coletado nos processamentos anteriores serão ajustados no ultimo processmento quando usar Deduzir Imposto para Prova de Isenção de Imposto não submetido_ no processamento do salario ou Recibo de salario.

Tambem, no fim do ano o funcionario submete a prova actual dos gastos para aquivar via [Submissão da Prova de Isenção de Imposto do Funcioario](/docs/user/manual/pt/recursos-humanos/submissão-prova-isenção-imposto-funcionário). NO ultimo processamento do Periodo da Folha de Pagamento, o ERPNext irá verificar as provas de submissão dos funcionarios e se não encontrar, imposto para os rendimentos isentos serao adicionados ao componente norma de dedução.

### Categoria de Isenção de Imposto de Funcionario
Isenções de Salario Tributavel são normalmente restritos para certas categorias decididas pelo governo ou orgão regulador. O ERPNext permite configura varias categorias no qual estao autorizadas a isenção. Exemplo podem ser, para India, 80G, 80C, B0CC, etc.

Voce pode configurar a Categoria de Isenção de Imposto do Funcionario indo em ,
> Recursos Humanos > Configuração Folha de Pagamento > Categoria de Isenção de Imposto de Funcionario > Nova Categoria de Isenção de Imposto do Funcionario

<img class="screenshot" alt="Employee Tax Exemption Category" src="/docs/assets/img/human-resources/employee-tax-exemption-category.png">

### Subcategoria de Isenção de Imposto do Funcionario
Em baixa de cada categoria, pode haver muitas mais no qual a isenção é permitida. Por exemplo, na India, subcategorias em baixa de 80C pode ser Premio de Seguro de Vida

Voce pode configurar a Subcategoria indo em ,
> Recursos Humanos > Configuração Folha de Pagamento > Subcategoria de Isenção de Imposto do Funcionario > Nova Subcategoria

<img class="screenshot" alt="Employee Tax Exemption Sub Category" src="/docs/assets/img/human-resources/employee-tax-exemption-subcategory.png">

### Isenção HRA - Regional, India
Para o ano fiscal 2018-19, na India, isenção de Renda de Casa (HRA) apartir dos rendimentos é no mínimo:
 * O valor actual dado empregado como HRA.
 * Renda actual paga menos de 10% do salario base.
 * 50% do salario base, se o funcionario fica numa cidade de metro (40% para fora da cidade).

 Como parte da Declaração de Isenção de Imposto do Funcionario, os mesmo podem preencher a Isenção HRA. O ERPNext irá calcular a isenção elegivel para o HRA e isentar quando estiver a calcular os rendimentos tributaveis.

 > Nota: Componente Basico e HRA de salario podem ser configurados na Empresa para isenção HRA de trabalho

### Opções na Folha de Pagamento e Recibo de Salario
O ERPNext simplifica a Folha de Pagamento processando automaticamente o mesmo em massa [Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento).

* Dedução do Imposto para Beneficios de Funcionario não reivindicados: Beneficios flexiveis (Componentes de Salario que são _É Beneficio Flexivel_) não são incluidos no rendimento tributavel do funcionario. Contudo, o valore recebido para estes componentes irão ser incluidos nos rendimentos tributaveis se o funcionario falhar no envio do [Reivindicação de Beneficio do Funcionario](/docs/user/manual/pt/recursos-humanos/reivindicação-beneficio-funcionário) enquanto estiver a calcular o imposto no ultimo processamento do periodo do salario.

Se voce quiser coletar os impostos para os beneficios antes do ultimo processamento, selecione esta opção e o ERPNext irá calcular o imposto e adicionar para todos os beneficios não taxados ao processar o recibo de salario.

* Deduzir Imposto para Prova de Isenção de Funcionario não Submetida: Esta opção permite que voce faça a dedução de impostos para os ganho no qual estava isento no processamento anterior como declarado na [Declaração de Isenção de Imposto to Funcionario](/docs/user/manual/pt/recursos-humanos/declaração-de-isenção-de-imposto-funcionário) mas o Funcionario fez a submissão via [Submissão da Prova de Isenção de Imposto do Funcionario](/docs/user/manual/pt/recursos-humanos/submissão-prova-isenção-imposto-funcionário). É de notar que se a opção estiver activa o ERPNext não considera a Declaração e não irá levar em conta _Submissão de Prova de Isenção de Imposto de Funcionario_ ao processar isenção anual dos rendimentos do funcionario.

> Nota: Caso necessario, voce pode processar o salario para os funcionarios individuais, criando manualmente o Recibo de Salario

# Laje de Rendimento Tributável
[Laje de Rendimento Tributável](/docs/user/manual/pt/recursos-humanos/income-tax-slab) ajuda voce definir as lajes de Imposto aplicaveis para um certo periodo, tornando facil a gestão devido as alterações de lei. Voce pode adicionar varias lajes de impostos para o periodo dependendo dos regulamentos de impostos. Note que voce pode usar campos no documento Funcionario no campo _Condição_ para aplicar as lajes de imposto com base nos atributos dos funcionarios.

# Componente do Salario
Para a dedução de imposto automatico com base na laje de impostos configurados na Laje de Rendimento Tributavel, voce tem que configurar o Componente de Salario do tipo _Dedução_ com a opção _Variavel com Base no Rendimento Tributavel_ activa. Esta caixa permite auto calcular o Rendimento Tributavel considerando as lajes de imposto e declarações submetidas pelo funcionario. O imposto será calculado anualmente sobre o salario dedutivel e igualmente dividido em 12 meses.

>**Nota Impostante:** Se voce configurar a condição e formula para o componente Dedução, a condição e formula serão consideradas para calcular o Componente de Salario e Lajes de Imposto configuradas na Laje de Rendimento Tributavel sera ignorado. Contudo, voce pode ainda usar a opção _Dedução de Imposto para Prova de Isenção de Imposto para Funcionario não Submetida_ na Folha de Pagamento / Recibo de Salar para deduzir os impostos com base nas Lajes de Imposto configuradas nas Lajes de Rendimento Tributavel, isentando [Submissão da Prova de Isenção do Imposto do Funcinario](/docs/user/manual/pt/recursos-humanos/submissão-prova-isenção-imposto-funcionário) que irá proceder a Laje de Imposto com base nas Deduções de imposto.
É bastante util se voce quer deduzir um valor fixo como dudução para cada processamento em vez do ERPNext fazer os calculos automaticos com base nos salario anual projectados do funcionario depois isenção declarada pelo funcionario via [Declaração de Insenção de Imposto de Funcionario](/docs/user/manual/pt/recursos-humanos/declaração-de-isenção-de-imposto-funcionário). No fim do ano fiscal, voce pode usar _Dedução de Imposto da Prova de Isenção de Imposto não Submetida_ para deduzir o restante do imposto de responsabilidade do funcionario para o periodo todo.

{next}
