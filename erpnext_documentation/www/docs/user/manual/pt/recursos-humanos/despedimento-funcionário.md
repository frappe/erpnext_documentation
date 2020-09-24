# Despedimento do Funcionário

**Despedimento do Funcionário é a situação em que o acordo de trabalho de um Funcionario para com a empresa termina e Funcionario deixa a Empresa.**

Despedimento do Funcionário é criado para um Funcionario que tenha sido despedido ou terminado com a Empresa.

**Caso pratico:** Vamos assumir que as seguntes actividade no qual precisam ser feitas o  mais rapido possivel assim que um Funcionario deixa a Empresa.

- Obter o Laptop
- Liquidar dividas 
- Apagar a Conta de Email do Funcionario
- Obter o Cartão de identidade


No ERPNext, estas atividades normais podem ser rastreadas no Modelo de Despedimento do Funcionario. Para aceder vá para: 

> Recursos Humanos > Ciclo de Vida do Funcionario > Separação do Funcionario

## 1.  Pre-requisitos

Antes de criar uma Separação de Funcionario, é aconselhavel criar os seguintes documentos:

* [Funcionario](/docs/user/manual/pt/recursos-humanos/funcionario)
* [Departamento](/docs/user/manual/pt/recursos-humanos/departamento)
* [Designação](/docs/user/manual/pt/recursos-humanos/designação)
* [Grau de Funcionario](/docs/user/manual/pt/recursos-humanos/employee-grade)

## 2. Como criar uma Separação de Funcionário

1. Vá para: Separação de Funcionario > Novo.
1. Selecione o Funcionario. Uma vez selecionado, a Informação do Funcionario correspondente tal como, Departamento, Designação e Grau de Funcionario serão inseridos.
1. Selecione o [Modelo de Separação de Funcionario](#31-modelo-de-separação-de-funcionário). Com base no modelo selecionado, informações como Departamento, Designação e Grau de Funcionario serão inseridos (se ja foi mencionado no Modelo de Separação).
1. Digite a Data da Carta de Despedimento.
1. Adicionalmente, voce pode tambem digitar o Sumario da Entrevista de Despedimento.
1. Salvar e Submeter.


  <img class="screenshot" alt="Separation Template" src="{{docs_base_url}}/assets/img/human-resources/employee-separation.png">



> Nota 1: Se um Modelo de Separação de Funcionario não foi criado, voce pode directamente preencher a informação no formulario de Separação..

> Nota 2: O 'Status' da Separação do Funcionario irá mudar para Completado uma vez todas as actividades associadas estiverem completas.


## 3. Funcionalidades

### 3.1 Modelo de Separação de Funcionario

O Modelo de Separação de Funcionario é um blueprint no qual contem uma lista de actividades pre-definidas para a Separação do Funcionario. Um Modelo de Separação de Funcionario pode ser cirado para um Departamento, Designação e Grau de Funcionario em Particular. 

Para criar um novo Modelo de Separação de Funcionario:

1. Vá para: Recursos Humanos > Ciclo de Vida do Funcionario > Modelo de Separação de Funcionario > Novo.
1. Digite o Departamento, Designação e Grau do Funcionario (opcional).
1. Mencione as Actividades para separação. Para cada Actividade, voce pode tambem mencionar o Usuario ou Papel, para quem as actividades serão atribuidas.
  
  <img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/employee-separation-template.png">


### 3.2 Tarefas e Atribuições

Ao submeter a Separação do Funcionario, um [Projecto](/docs/user/videos/learn/project-and-task) será criado. Dentro do Projecto, [Tarefas](/docs/user/videos/learn/project-and-task) tambem serão criadas para cada Actividade. 

Voce pode visualizar os Projectos e Tarefas criadas pelo Visão > Projetos / Tarefas.


Adicionalmente, cada Actividade pode ser atribuida pesos com base na sua importancia.

<img class="screenshot" alt="Tasks and Assignments" src="{{docs_base_url}}/assets/img/human-resources/employee-sep1.png">

Com base no progresso das Tarefas, progresso pode ser actualizado no processo de Separação do Funcionario.


### 3.3 Status Funcionario

Voce pode directamente visualizar os Funcionarios separadas pelo formulario Separação de Funcionarios indo em Visão > Funcionario uma vez o formulario submetido.


## 4. Topicos Relacionados

1. [Employee Onboarding](/docs/user/manual/pt/recursos-humanos/employee-onboarding)
1. [Promoção de Funcionario](/docs/user/manual/pt/recursos-humanos/promoção-funcionário)
1. [Separação de Funcionario](/docs/user/manual/pt/recursos-humanos/despedimento-funcionário)



