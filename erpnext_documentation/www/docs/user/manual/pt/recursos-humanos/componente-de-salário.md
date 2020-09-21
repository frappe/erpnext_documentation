<!-- add-breadcrumbs -->
# Componentes de Salário

**Salários são pagos por empresas aos seus funcionários em troca de serviços prestados a eles. Os diferentes componentes que compoem a Estrutura de Salário são chamados de Componentes de Salário.** 

Salários pago aos funcionários compromente varios componentes diferentes, tal como o salário basico, mesadas, atrasos, etc. O ERPNext permite que voçê defina estes Componentes de Salário e tambem especifique os varios atributos.

Para aceder aos Componentes de Salário, vá para:
> Home > Recursos Humanos > Folha de Pagamento > Componente de Salário

## 1. Como criar uma Componente de Salário

Para criar uma nova Componente de Salário:

1. Vá para a lista de Componentes de Salário, clique em Novo.
2. Digite o Nome e Abreviatura.
3. Digite a Descrição do Componente de Salário (opcional).
1. Digite o Nome da Empresa e a Conta Padrão do Componente de Salário na tabela de Contabilidade.
3. Salvar.

 <img class="screenshot" alt="Salary Component" src="{{docs_base_url}}/assets/img/human-resources/salary-component1.png">

## 2. Funcionalidades

Apartir dos campos acima, algumas das funcionalidades dos Componente de Salário são:

### 2.1 Condição e Formula

Aqui nesta secção, a Condição e Formula é necessária para o calculo do Componente de Salário. Para especificar uma formula, active a caixa 'Valor com base em formula'. 

<img class="screenshot" alt="Salary Component" src="{{docs_base_url}}/assets/img/human-resources/salary-component2.png">

No caso do Componente de Salário ser com base num valor pre-definido, o ERPNext permite que digite directamente o valor no Campo Valor (desactive a caixa 'Valor com base em formula').

> **Nota:** Esta configuração em cima é opcional. Voçê pode definir Valor e Formula/Condição para um Componente de Salário directamente na Estrutura de Salário tambem. Se for especificado no Componente de Salário, a informação será inserida automaticamente na Estrutura de Salário quando o Componente for seleconado.

### 2.2 Propriedades Adicionais

Algumas das Propriedades Adicionais do Componente de Salário que podem ser activadas são as seguintes:

* **É para Pagar:** Selecione se o Componente de Salário é para ser pago.
* **Depende dos dias de Pagamento:** Se a caixa estiver activa então o Componente de Salário será calculado com base no numero de dias trabalhados.
* **É Tributavel:** Esta caixa é aplicada a Componentes de Remuneração. Selecionando esta caixa permita aplicar Imposto ao componente selecionado.
* **Deduz Imposto Completo na Data da Folha de Pagametno Selecionado:** Se selecionado e o componente é usado para Salário Adicional, o valor do Imposto aplicado no valor adicional será deduzido no Mês especifico. Se não estiver selecionada, o imposto será distribuido pelos meses restantes do peiodo do processamento do salário. Por exemplo, se um bonus é dado num mês especifico usando Salário Adicional, então voçê deduzir imposto completo somente para o mesmo mês.
* **Arrendondar para o numero inteiro mais proximo:** Selecionando esta caixa permite que arrendonde o valor deste Componente de Salário para o inteiro mais proximo.
* **Componente de Estatistica:** Se selecionado, o valor especificado ou calculado nesta componente não irá contribuir para as remunerações ou deduções. Contudo, o valor poderá ser referenciado pelos outros componentes que podem adicionar ou deduzir. Se voçê definir um Componente Salarial como Componente de Estatistica, então não precisa definir uma Conta de Contabilidade Padrão. Tambe, não será possivel definir este componente como um Beneficio Flexivel.
* **Não Incluir no Total:** Selecionando esta caixa tera a certeza que o Componente Salárial não seja incluido no Total do Salário. É usado para definir o componente que é parte do CTC mas não será pago (e.g. Uso do Carro da Empresa).
* **Variavel com Base no Imposto do Salário:** Este componente é calculado automaticamente em recebimento tributavel com base no Imposto de Renda aplicado (e.g. TDS or Imposto de Renda).
* **Isento do Imposto de Renda:** Se selecionado, o valor total será deduzido dos impostos antes de ser calculado o imposto de renda sem qualquer [declaração](/docs/user/manual/pt/recursos-humanos/declaração-de-isenção-de-imposto-funcionário) ou [prova de submissão](/docs/user/manual/pt/recursos-humanos/submissão-prova-isenção-imposto-funcionário). Por exemplo, Imposto de Profissional na India é deduzido apartir dos Rendimentos Tributaveis antes de calcuar o Imposto de Renda. 
* **Desactivado:** Esta caixa pode ser selecionada para descativar o Componente de Salário. Um componente desactivo não pode ser usado na Estrutura de Salário.

### 2.3 Beneficios Flexiveis

Esta secção é mostrada se o Componente de Salário é um Componente de Remuneração. O Beneficio Flexivel permite o funcionário de receber os beneficios que querem ou precisam de um pacote de programas oferecidos pelo patrão. Eslte podem incluir seguro de saúde, plano de pensão, despesas de telefone, etc. Para definir o Componente de Salário como Beneficio Flexivel, clique na caixa 'É um Beneficio Flexivel'.

<img class="screenshot" alt="Flexible Benefit" src="{{docs_base_url}}/assets/img/human-resources/flexible-ben.png">

Digite o valor anual maximo para o beneficio flexivel no campo 'Max Valor Beneficio (Anual)'. Alguns do atributos adicionais do Beneficio Flexivel que pode ser activos selecionando são:   

* **Pagar com Reivindicação de Beneficio:** Active esta caixa se voçê quer pagar este beneficio via [Reivindicação de Beneficio do Funcionário](/docs/user/manual/pt/recursos-humanos/reivindicação-beneficio-funcionário).
* **Impacto Somente em Imposto (Cannot Claim But Part of Taxable Income):** Se definido, o beneficion flexivel será parte do imposto dos rendimentos tributaveis.
* **Criar Registo de Pagamento Separado contra Reivindicação de Beneficio:** Se activo, irá deixar criar um pagamento separado contra a Reivindicação de Beneficio.

## 3. Topicos Relacionados

1. [Estrutura de Salário](/docs/user/manual/pt/recursos-humanos/estrutura-salário)
1. [Atribuição da Estrutura de Salário](/docs/user/manual/pt/recursos-humanos/atribuição-estrutura-salário)
1. [Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento)
1. [Periodo da Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/periodo-folha-de-pagamento)
