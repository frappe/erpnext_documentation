<!-- add-breadcrumbs -->
# Configuração Folha de Pagamento

Salário é um valor fixo de dinheiro ou compensação paga a um funcionário por um empregador em retorno do seu trabalho feito.

Folha de Pagamento é a administração de registos financeiros dos salários, ofertas, bonus, valor liquido e reduções dos funcionários.

Para processar a Folha de Pagamento no ERPNext,

1. Defina [Período da Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/Período-folha-de-pagamento.html) (opcional)
1. Defina [Laje de Taxa de Renda](/docs/user/manual/pt/recursos-humanos/income-tax-slab.html) (opcional)
2. Crie a Estrutura de Salário com os Componentes de Salário (Remunerações e Deduções)
3. Atribua a Estrutura de Salário para cada Funcionário via Atribuição de Estrutura de Salário
4. Gere os Recibos de Salário via [Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento.html).
5. Aloque o Salário na sua Contabilidade.

## Período da Folha de Pagamento
[Período da Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/Período-folha-de-pagamento.html), no ERPNext, é o Período no qual o Funcionário é pago pela sua ocupação na Empresa. O Período ajuda a definir as lajes de Imposto aplicáveis nessa fase, tornando fácil gerir as alterações de leis.

> Nota: Configurando o Período da Folha de Pagamento é opcional se você não pretende usar Benefícios Flexíveis ou Lajes de Imposto

## Componente de Salário
Este documento permite que você defina cada componente de remuneração e dedução no qual pode ser usado na Estrutura de Salário e subsequentemente criar o Recibo de Salário ou Salário Adicional. você pode também configura o tipo, condição e formula bem como outras opções discutidas mais em baixo. você deve ter a possibilidada de ativar varias combinações das seguintes opções para configurar cada componente de acordo a necessidade da sua Empresa / Politicas da Região.

* Depende de Licença sem Pagamento: Licença sem Pagamento (LWP) acontece quando um Funcionário já não tem licenças alocadas ou tira uma licença sem aprovação (via Solicitação de Licença). Se activo, o ERPNext irá automaticamente deduzir o pagamento em proporção dos dias LWP dividido pelo total de dias trabalhados para o mês (com base na lista de Feriados).

	> Nota: Se você não que o ERPNext faça a gestão do LWP, não active esta opção em qualquer componente de salário

* Não incluir no total: Se esta opção estiver activa, o componente não será adicionado ao total das Remunerações ou Deduções para o Recibo de Salário

#### Remunerações

<img class="screenshot" alt="Salary Component Earnings"
	src="{{docs_base_url}}/assets/img/human-resources/salary-component.png">

* É um Componente Adicional: Esta opção especifica que o componente pode somente ser pago como um Salário Adicional. Exemplos deste componente podem ser os Bonus de Desempenho ou pagamento recebido por um trabalho extra, etc. Tais componentes não são considerado como parte da Estrutura Salárial normal. Em vez, Salário Adicional com estes componentes pode ser submetido sempre que necessário no qual irá ser adicionado automaticamente ao Recibo de Salário.

* É tributavel: Se o componente precisa ser considerado para calculo de Imposto pelo Período de Folha de Pagamento você pode quere activar esta opção. Será necessário ter um Período de Foha de Pagamento e Laje de Imposto de Renda configurado com as Lajes de Imposto validas para o processamento do salário.

* Para Pagar: Tais componentes podem ser alocados contra contras a pagar separadas e as Contas devem ser configuradas no Plano de Contas

* Beneficios Flexiveis: Beneficios Flexiveis são componentes de remuneração no qual Funcionários pode escolher receber em pro-rata ou anualmente quando reividicam. Muitas das vezes estão isentos de imposto, ha não ser que o funcionário falhe na entrega da reivindicação com os documentos certos. Se activo, você pode especificar o maximo de beneficios permitido para um funcioário durante um ano. Os Funcionários podem criar [Aplicação de Beneficio de Funcionário](/docs/user/manual/pt/recursos-humanos/aplicação-beneficio-funcionário) com os que eles decidirem.

	>Nota: Aplicação de Beneficio do Funcionário permite os Funcionário escolher somente os componentes flexiveis que estão presentes na Estrutura de Salário atribuidos a eles

	- Pagar contra a Reivindicação do Beneficio: Funcionários podem optar por receber os beneficios flexiveis anual via Reivindicação do Beneficio do Funcionário ou todos os meses no salário. Se activar isto, o valor alocado para o componente irá ser pago assim que o Funcionário submeter uma [Reivindicação de Beneficios de Funcionário](/docs/user/manual/pt/recursos-humanos/reivindicação-beneficio-funcionário.html). Caso contrário o valor será distribuido como parte do salário do Funcionário numa base pro-rata.

 - Imposto de Impacto Somente (Não depo reivindicar Mas Parte dos Rendimentos Tributaveis): Tais componentes são os que a empresa já pagou ao funcionário em dinheiro ou por outra via, por exemplo um carro comprado para o uso do Funcionário. O Funcionário não pode reivindicar mas é responsavel por pagar o imposto. O valor alocado para este componente é considerado ao calcular os Rendimentos Tributaveis para o Funcionário.

 - Criar Registo de Pagamento Separado conta a Reivindicação de Beneficios: Alguns beneficios flexiveis podem ser legalmente necessários serem pagos separados. Se você activar, ao processar o registo de banco o valor pago para tal componente será inserida como um registo separado para cada funcionário.

	<img class="screenshot" alt="Flexible Salary Component"
	src="{{docs_base_url}}/assets/img/human-resources/salary-component-1.png">

	> Nota: Calculo do Imposto Normal não inclui Beneficios Flexiveis como em muitos casos estão isentos do Imposto. Para incluir Imposto nestes componentes antes do processamento do salário, utilize "Deduzir Imposto para Beneficio de Funcionário não Reivindicado" na Folha de Pagamento / Recibo de Salário quando estiver a processar os Salários.

#### Dedução

<img class="screenshot" alt="Salary Component Deduction"
	src="{{docs_base_url}}/assets/img/human-resources/salary-component-2.png">

* Variavel com Base no Salário Tributavel: Se activo, o componente será considerado como um componente de Imposto Normal. Calculo do Imposto será feito na Laje de Imposto de Renda para o funcioário.

## Estrutura de Salário

Estrutura de Salário representa como os salários estão estruturados e calculados com base em Remunerações e Deduções. Estrutura de Salários são usado para ajudar as empresas:

1. Manter o nivel de pagamento que são competitivos com o mercado externo de trabalho,
2. Manter relacionamento de pagamento interno entre trabalhos,
3. Reconhecer e gratificar diferenças no nivel de responsabilidade, habilidade, desempenho e gerir despesas de pagamentos.

Componentes normais da Estutura de Salário (na India) incluem:

* Salário Base: É um imposto de renda base e normalmente não mais que 40%.

* Mesada de Arrendamento de Casa: O HRA constitue 40 a 50% do salário base.

* Mesadas Especiais: Makes up for the remainder part of the salary, mostly smaller than the basic salary which is completely taxable.

* Mesada para Licença de Viagem: Valor pago não tributavel pelo empregador para o funcionário para ferias/viagens com a familia dentro da India.

* Gratidão: É basicamente um valor lump sum pago pelo empregador quando o funcionário se despede da empresa ou vai para a reforma.

* PF: Fundo recebido durante emgergencia ou idade avançada. 12% do salário base é automaticamente deduzido e vai para o fundo de pensão.

* Mesada Medica: O Empregador paga ao funcionário por despesas medicas. É um valor de Rs.15,000 sem impostos.

* Bonus: Parte Tributavel do CTC, normalmente uma vez ao ano  lump sum, dado ao funcionário com base no desempenho na empresa durante o ano.

* Opções de Stock do Funcionário: ESOPS são de Borla/acções descontadas dadas ao funcionário. Isto é normalmente feito para aumentar a retenção do funcionário.

<img class="screenshot" alt="Submitted Salary Structure" src="{{docs_base_url}}/assets/img/human-resources/salary-structure.png">
Uma Estrutura de Salário submetida

### Criando um Nova Estrutura de Salário
Para criar um nova Estrutura de Salário vá para:

> Recursos Humanos > Folha de Pagamento > Estrutura Salarial > Nova Estrutura Salarial

Na nova Estrutura Salarial,

1. Nome da estrutura salarial e o nome da empresa, cabeçalho para o recibo e a frequencia do processamento, etc.
2. Defina a data de inicio (Nota: Somente pode haver uma Estrutura Salarial "Activa" para um Funcionário durante qualquer Período).
3. Configure o Valor Leave Encashment Amount  por Dia no qual será o valor a pagar a Funcionário que queiram Sair ao fazer o Pedido Leave Encashment.
4. Valor Maximo de Beneficios como Componente de Beneficios para o funcionário.

#### Recibo de Salário com Base no Timesheet

Recibo de Salário com base no Timesheet é aplicavel se você tiver o processamento de salario por timesheet

1. Marque "Recibo de Salário com Base em Timesheet"
2. Selecione o componente de salario e digite o Valor Hora (Nota: Este componente de salario é adiciondo as remunerações no Recibo de Salario)

<img class="screenshot" alt="Salary Slip based on Timesheet" src="{{docs_base_url}}/assets/img/human-resources/salary-timesheet.png">

#### Remunerações e Deduções na Estrutura Salarial

Nas tabelas “Remunerações" e "Deduções”, você pode selecionar os componentes das remunerações e deduções, a condição e formula configurada no Componente Salarial será inserido por defeito, mas você pode alterar. você pode querer selecion o componente Base na table Remunerações. De notar que o valor a considerar para cada Funcionário deve ser configurado na Atribuição da Estrutura Salarial.

Na condição e formula para qualquer remuneração ou dedução não configurado no Componente Salarial, você pode calcular os valores dos Componentes Salariais com base em,

#### Condição e Formula

<img class="screenshot" alt="Condition and Formula" src="{{docs_base_url}}/assets/img/human-resources/condition-formula.png">

#### Condição e Formula

<img class="screenshot" alt="Condition and Amount" src="{{docs_base_url}}/assets/img/human-resources/condition-amount.png">


Em condições e formulas,

  * Use campo "base" para usar o salario base do Funcionario
  * Use as Abreviaturas dos Componentes. Por exemplo: BS para Salario Base
  * Use o nome do campo para detalhes do funcionario. Por exemplo: Tipo de Contracto para employment_type

#### Destalhes da Conta

<img class="screenshot" alt="Salary Structure Account" src="{{docs_base_url}}/assets/img/human-resources/salary-structure-account.png">  

  * Selecione o Modo de Pagamento e Conta de Pagamento para os Recibos de Salario no qual será gerado usando esta Estrutura Salarial

Finalmente, *Salvar* a Estrurura Salarial.

### Licença sem Pagamento (LWP)

Licença sem Pagamento (LWP) acontece quando um Funcionário já não tem ferias alocadas ou saiu sem aprovação (via Solicitação de Licença). Se você quiser que o ERPNext deduza automaticamente o salario em caso de LWP, então deve selecionar  na coluna "Aplicar LWP” no Tipo de Remuneração e Dedução. O valor do pay cut é a proporção dos dias LWP divido pelo total de dias trabalhados para o mês (com base na lista de Feriados).

Se você não quer que o ERPNext faça a gestão do LWP, deixe o LWP não maracado em todoas os Tipos de Remunerações e Deduções.

## Atribuição da Estrutura Salarial

Atribuição da Estrutura Salarial permite que você atribua uma estrutura salarial e especifique o valor base para cada funcionario. É importante que voçẽ defina o valor base para casa vendo que será o salario base usando para os calculos de cada Estrutura Salarial.

Para criar uma nova Atribuição da Estrutura Salarial va para:

> Recursos Humanos > Folha de Pagamento > Atribuição da Estrutura Salarial > Nova Atribuição da Estrutura Salarial

<img class="screenshot" alt="Salary Structure Assignment" src="{{docs_base_url}}/assets/img/human-resources/salary-structure-assignment.png">  

* * *

#Processando Salários
Voçe pode processar o salário em massa para os Funcionarios de um departament, filial ou designaçao ou processar individualmente criando os Recidos de Salario para cada funcionario.

## Processando Salários usando a Entrada de Foha de Pagamento
Voçẽ pode tambem criar os recibos de salario para varios funcionarios usando a Folha de Pagamento:

> Recursos Humanos > Folha de Pagamento > Entrada da Folha de Pagamento > Nova Folha de Pagamento

#### Registo do Processamento

<img class="screenshot" alt="Payroll Entry" src="{{docs_base_url}}/assets/img/human-resources/payroll-entry.png">

No Registo de Procesamento,

1. Selecione a Empresa para o qual quer criar os Recibos de Salario. Voçẽ pode selecionar tambem outros campos como Filial, Departamento, Designão ou Projecto.
2. Assinale _Recibo de Salario com base no Timesheet_ se voçe quiser processar com base nos timesheets.
3. Selecione a Data de Postagem e a frequencia do processamento no qual quer criar os Recibos de Salario.
4. Clique em "Obter Detalhes de Funcionarios" para obter a lista de Funcionariios no qual os Recibos de Salario estaã a ser criados.
5. Digite a Data de Inicio e Fim do Período de processamento.
6. Voçẽ pode assinalar  _Deduzir Imposto para Benefincios de Funcionario não Reivindicado_ se voçe quiser deduzir os impostos para todos os beneficios (Componentes de Salario que são  _É Beneficio Flexivel_) pagos ao funcionarios ate o corrente processamento
7. Igualmente,  _Dudução de Imposto para Prova de Isenção não Submetida_ permite deduzir os impostos para as remunerações que estavam isentas nos processamentos antiores declaradas no [Declaração de Isenção de Imposto do Funcionario](/docs/user/manual/pt/recursos-humanos/declaração-de-isenção-de-imposto-funcionário) mas o Funcionario não submeteu a provas suficientes [Submissão de Prova de Isenção de Imposto do Funcionario](/docs/user/manual/pt/recursos-humanos/submissão-prova-isenção-imposto-funcionário)
8. Selecione o Centro de Custo e a Conta de Pagamento.
9. Salve o formulario e submeta para criar os Recibos de Salario para cada Funcionario activo para o Período selecionado. Se os Recibos já foram criados, o sistema não irá criar mais Recibos de Salario. Voçẽ pode ambem salvar o formulario em Rascunho e criar um Recibo de Salario depois.

<img class="screenshot" alt="Submitted Payroll Entry" src="/docs/assets/img/human-resources/created-payroll.png">

Uma vez todos os Recibos criados, voçe pode usar o  _Ver Recibos de Salario_ para verificar se estatudo criado correctamente ou editar caso queira fazer uma dedução da Licença sem Pagamento(LWP).

Depois de verificar, pode "Sumbeter" todos fazneod o clique em "Submeter Recibo de Salario".

>Nota: Ao Submeter os Recibos de Salario irá alocar os registos nas contas a pagar na Contabilidade.

#### Alocando Salarios na Contabilidade

O passo final é alocar os Salarios na sua Contabilidade.

Salarios em negocios são negociados em extremo sigilo. Em mutos caos, as empresas fazem um unico pagamento ao Banco combinando todas as contas e salarios e o banco faz a distribuição dos mesmos para cada conta dos funcionrios. Desta forma é um unico pagamento nos livros da Empresa e qualquer um com acesso não ra ver as contas individuais.

O registo do salario é um Lançamento Contabilistico que debita o total de remunerações e credita o total de deduções para todos os Funcionarios para uma conta padrão definido a nivel de Componente Salarial para cada componente.

Para gerar o seu voucher de pagamento de salario apartir da Folha de Pagamento, clique em -
> Criar > Lançamento Bancario

<img class="screenshot" alt="Payroll Make Entry" src="/docs/assets/img/human-resources/payroll-make-bank-entry.png">

Registo de Salario irá reencaminhar para o Lançamento Contabilistico com os filtros relevantes para ver o Journal Voucher em Rascunho. Voçe deve definir o nuero da referencia e a data para a transação e Submeter o Lançamento Contabilistico.

>Nota: Para Componentes de Salario que são Beneficios Flexiveis e tem  _Criar Contas de Pagamento Separadas contra o Registo de Reivindicação de Beneficios_ activos, o ERPNext irá alocar separados os Registos do Jornal.

<img class="screenshot" alt="Payroll Entry" src="/docs/assets/img/human-resources/payroll-journal-entry.png">

## Criando Recibos de Salario Manual

Uma vez a Estrutra Salaria criada e atribuida aos funcionarios via Atribuição da Estrutura Salarial, voçe pode criar os Recibos de Salario individuais. Va para:

> Recursos Humanos > Folha de Pagamento > Folha de Vencimento > Nova Folha de Vencimento

#### Recibo de Salario

<img class="screenshot" alt="Salary Slip" src="{{docs_base_url}}/assets/img/human-resources/salary-slip.png">

{next}
