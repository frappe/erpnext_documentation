<!-- add-breadcrumbs -->
# Salário Adicional

**Salário Adicional é algo que um Funcionario recebe pela empresa em que trabalha, outro pagamento fora do habitual.**


O ERPNext oferece uma funcionalidade chamada Salário Adicional para adicionar ou reduzir salario para um Funcionario durante o processamento. Alguns exemplo para Salário Adicional pode ser Bonus de Desempenho, Mesada por Mandato, Atrasos, Incentivos ou outros ajustes.

Para aceder Salário Adicional, vá para:

> Home > Recursos Humanos > Folha de Pagamento > Salário Adicional

## 1. Pre-requisitos

Antes de criar Salário Adicional, crie os seguintes:

* [Funcionario](/docs/user/manual/pt/recursos-humanos/funcionario)
* [Componente de Salario](/docs/user/manual/pt/recursos-humanos/componente-de-salário)


## 2. Como criar um Salário Adicional


1. Vá para Salário Adicional, clique em Novo.
2. Selecione o Funcionario.
3. Selecione o Componente de Salario.
4. Digite o Valor.
1. Digite a Data do Processamento. Se a Data de Processamento para o Salário Adicional estiver no intervalo ao processar o salario, irá adicionar aos Remunerações/Deduções.
1. Salvar e Submeter.

Selecione a caixa 'Subscreva o Valor da Estrutura de Salario' para subscrever o componente Salário Adicional no valor da Estrutura de Salario. Adicionalmente, a caixa 'Deduzir Imposto Completo na Data da Folha de Pagamento' pode ser selecionada se o Imposto completo precisa ser reduzido no componente Salário Adicional para aquela data em particular do Processamento.

<img class="screenshot" alt="Additional Salary" src="{{docs_base_url}}/assets/img/human-resources/additional-salary.png">

## 3. Funcionalidades

### 3.1 Salário Adicional Recorrente
Esta funcionalidade permite os usuarios em criar um Salário Adicional para um período fixo.
Quando 'É Recorrente' é selecionado voce precisa preencher 'Até a Data' e 'A partir da Data'. 
Este irá adicionar ou deduzir o valor do Salário Adicional para este funcionario dentro do periodo da data e irá reflectir no Recibo de Salario do Funcionario. O Salário Adicional irá repetir todos os entre o intervalo 'A partir da Data' e 'Até a Data'.

## 4. Topicos Relacionados

1. [Bonus de Retenção](/docs/user/manual/pt/recursos-humanos/bonus-de-retenção)
1. [Incentivo do Funcionario](/docs/user/manual/pt/recursos-humanos/incentivo-funcionário)
1. [Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/estrutura-salário)
1. [Atribuição de Estrutura de Salario](/docs/user/manual/pt/recursos-humanos/atribuição-estrutura-salário)
1. [Entrada de Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento)
1. [Periodo de Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/periodo-folha-de-pagamento)


{next}
