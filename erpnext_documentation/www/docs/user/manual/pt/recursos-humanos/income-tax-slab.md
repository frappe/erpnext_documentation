<!-- add-breadcrumbs -->
# Laje de Imposto de Renda - Income Tax Slab

**Laje de Imposto de Renda é um documento para definir a taxa do Imposto de Renda com base em diferentes Lajes de Imposto de Renda.** 

Em muitos países, imposto de renda é atribuido a contribuintes individuais com base num sistema de Lajes com diferentes taxas de imposto pre-escritas e tais taxas continuam a aumentar. No ERPNext, voce pode definir varias Lajes de Imposto de Renda e ligar a estrutura salarial dos funcionario via a Atribuição da Estrutura Salarial.

Para aceder a Laje de Imposto de Renda, vá para:
> Home > Recursos Humanos > Folha de Pagamento > Laje de Imposto de Renda

## 1. Como criar uma Laje de Imposto de Renda

Para criar uma nova Laje de Imposto de Renda:

1. Digite o Nome para a Laje IT, Empresa e data no qual terá inicio.
1. Active a caixa 'Permitir Isenção de Imposto' se for aplicavel.
1. Salvar e Submeter.

## 2. Funcionalidades

### 2.1 Lajes de Imposto

Na tabela Laje de Imposto, voce pode definiar a taxa para as diferentes lajes. Para definir a laje, o valor De e Para deve ser digitado. Para primeira laje, o Valor De é opcional e para a ultima laje, o Valor Para é opcional. Ambos são incluídos quando estiver a avaliar a taxa com base no rendimento tributavel. 


<img class="screenshot" alt="Income Tax Slab" src="/docs/assets/img/human-resources/income-tax-slab.png">

A laje de imposto é aplicada com base em condições especificas. Conditções podem ser escritas usando todos os campos de Funcionario, Estrutura de Salario, Atribuição de Estrutura de Salario e Recibo de Salario.

Exemplos:

```
// Aplique a taxa se o funcionario nascido entre 31-12-1937 e 01-01-1958 (Idade entre 60 e 80)
date_of_birth > date(1937, 12, 31) and date_of_birth < date(1958, 01, 01)

// Aplicar taxa pelo Genero
gender == "Male"

// Aplicar taxa pelo Componente de Salario
base > 10000

// Rendimento Tributavel Anual é maior que 5 lakhs
annual_taxable_earning > 500000
```

### 2.2 Outrs Impostos e Taxas no Imposto de Renda

Se outros impostos são aplicaveis a calcular o Imposto de Renda, voce pode digitar nesta tabela. Voce pode tambem definir o valor minumo e maximo do imposto pelo qual a Taxa será aplicada.
Por exemplo, Saude e Educação são aplicados no Imposto de Renda adicionalmente para todos na India.

<img class="screenshot" alt="Other Charged on Income Tax" src="/docs/assets/img/human-resources/other-taxes-on-income-tax.png">


### 2.3 Outras Propriedades

- **Permitir Isenção de Imposto:** Isenção de Imposto pode ser permitido para uma Laje de Imposto de Renda especifica. Se activo, ao calcular os impostos com base nesta laje, Declaração de Isenção de Imposto do Funcionario e Prova de Submissão são considerados para calcular Rendimentos Tributaveis.
- **Valor de Isenção de Imposto Padrão:** Se a isenção é permitida, o Valor de Isenção de Imposto Padrão definido pelo Governo pode ser adicionado aqui. Esta isenção geralmente não precisa de qualquer documento para provar e é aplicavel para todos os funcionarios ligado a esta laje de imposto de renda.

## 3. Topicos Relacionados

1. [Componente de Salario](/docs/user/manual/pt/recursos-humanos/componente-de-salário)
1. [Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/estrutura-salário)
1. [Atribuição de Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/atribuição-estrutura-salário)
1. [Entrada de Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento)
1. [Declaração de Isenção de Imposto de Funcionario](/docs/user/manual/pt/recursos-humanos/declaração-de-isenção-de-imposto-funcionário) 
1. [Submissão de Prova de Isenção de Imposto de Funcionario](/docs/user/manual/pt/recursos-humanos/submissão-prova-isenção-imposto-funcionário)
