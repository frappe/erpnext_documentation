<!-- add-breadcrumbs -->
# Declaração de Isenção de Imposto do Funcionário

**Isenção de Imposto é isenção monetária do rendimento, propriedade ou transação a partir de impostos que de outra forma seria cobrada a um Funcionario.**

No inicio do Período da Folha de Pagamento, funcionários podem declarar o valor da isenção que eles querem reivindicar dos seus salários tributáveis. O ERPNext permite que você especifique a categoria/subcategoria da isenção do imposto, valor da isenção do imposto e outras informações relacionadas na Declaração de Isenção de Imposto do Funcionário.
 

Para aceder a Declaração de Isenção de Imposto do Funcionário:

> Home > Recursos Humanos > Imposto de Funcionários e Beneficios > Declaração de Isenção de Imposto do Funcionário


## 1. Pre-requisitos

Antes de criar a Declaração de Isenção de Imposto do Funcionário, é aconselhavel criar estes primeiro:

* [Funcionario](/docs/user/manual/pt/recursos-humanos/funcionario)
* [Categoria de Isenção de Imposto do Funcionario](#31-categoria-de-isenção-de-imposto-do-funcionário)
* [Subcategoria de Isenção de Imposto do Funcionário](#32-subcategoria-de-isenção-de-imposto-do-funcionário)


## 2. Como criar uma Declaração de Isenção de Imposto do Funcionário

Para criar uma nova Declaração de Isenção de Imposto do Funcionário:

1. Vá para: Declaração de Isenção de Imposto do Funcionário > Novo.
1. Selecione a Subcategoria da Isenção e a Categoria da Isenção.
1. Digite o Valor Maximo da Isenção e o Valor Declarado.
1. Salvar e Submeter.

    <img class="screenshot" alt="Employee Tax Exemption Declaration" src="{{docs_base_url}}/assets/img/human-resources/employee-tax-exemption-declaration.png">

O Valor Total da Isenção será isentado dos rendimentos tributaveis anuais do funcionario ao clacular as deduções do processamento.

> **Nota:** Funcionarios podem somente submeter um Declaração de Isenção de Imposto do Funcionário por um Periodo de Folha de Pagamento.

## 3. Funcionalidades

###3.1 Categoria de Isenção de Imposto do Funcionário

Isenções de salarios tributaveis são restritos em categorias particulares decididas pelo Governo ou agencias de regulamentos. O ERPNext permite voce configurar varias categorias que podem esta isentas. Exemplo (para India) pode ser, 80G, 80C, B0CC etc.

Voce pode configurar a Categoria de Isenção de Imposto do Funcionario indo em, **Imposto de Funcionario e Beneficios > Categorai de Isenção de Imposto de Funcionario**

 <img class="screenshot" alt="Employee Tax Exemption Category" src="{{docs_base_url}}/assets/img/human-resources/employee-tax-exemption-sub-category1.png">


### 3.2 Subcategoria de Isenção de Imposto do Funcionário

Em baixo de varias categorias, pode ter mais no qual isenções são permitidas. Por exemplo, na India, subcategoria em baixo de 80C pode se Prémio de Seguro de Vida

Voce pode configurar a Categoria de Isenção de Imposto do Funcionario indo em, **Imposto do Funcionario e Beneficios > Subcategoria de Isenção de Impsto de Funcionario**

 <img class="screenshot" alt="Employee Tax Exemption Category" src="{{docs_base_url}}/assets/img/human-resources/employee-tax-exemption-category1.png">


### 3.3 Isenção HRA (Regional - India)

Para o ano fiscal corrente, na India, a Isenção do Rendimento de Aluguer de Casa (HRA) a partir dos rendimentos tributaveis é no minimo:

* O valor actual entregue pelo empregador como HRA.
* Renda Actual paga menos 10% do salario base.
* 50% do salario base, se o funcionario fica dentro da cidade (40% para fora da cidade).

Como parte da Declaração de Isenção de Imposto do Funcionario, os funcionarios podem preencher a isenção do HRA. O ERPNext calcula a isenção elegivel para HRA e isenta ao calcular os rendimentos tributaveis. 

Digita o Valor da Renda Mensal e selecione a caixa 'Arrendado dentro da Cidade' se aplicavel e submeter o formulario. A isenção Anual e Mensal do HRA será automaticamente calculada.

Uma vez submetida a declaração, voce pode submeter a prova da sua isenção de imposto fazendo clique no botão _Submeter Prova_.


<img class="screenshot" alt="Employee Tax Exemption Declaration" src="{{docs_base_url}}/assets/img/human-resources/hra-exemption.png">

> Nota: Componente HRA precisa ser configurado na ficha Empresa em baixo da secção Configurações HRA para a isenção de HRA funcionar.


## 4. Topicos Relacionados

1. [Submissão da Prova de Isenção de Imposto do Funcionario](/docs/user/manual/pt/recursos-humanos/submissão-prova-isenção-imposto-funcionário)
1. [Solicitação de Beneficio do Funcionario](/docs/user/manual/pt/recursos-humanos/aplicação-beneficio-funcionário)
1. [Reivindicação de Beneficio do Funcionario](/docs/user/manual/pt/recursos-humanos/reivindicação-beneficio-funcionário)

{next}
