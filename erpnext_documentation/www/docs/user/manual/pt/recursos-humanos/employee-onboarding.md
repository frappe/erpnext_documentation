# Employee Onboarding 

**No processo de contractar um Funcionario, existem definições como actividades normais que precisam ser feitas. Esta funcionalidade ajuda voce a manter a lista destas actividades, e criar um conjunto de tarefas na altura da contratação.**

Employee Onboarding é criado para um Candidado a Trabalho, que foi aprovado para contratar.

**Caso prático:** Vamos assumir que as seguintes actividades que precisam ser feias o mais rapido assim que o Candidato for aprovado para ser contratado.

- Fazer uma verificação legal e professional
- Criar uma ficha do Funcionario
- Criar uma Conta de Email
- Criar um Cartão de Identidade
- Alocar as Ferias


No ERPNext, estas activadades normais podem ser rastreadas no Modelo Employee Onboarding Template. Para aceder ao Employee Onboarding, vá para: 

> Recursos Humanos > Ciclo de Vida do Funcionario > Employee Onboarding

## 1.  Pre-requisitos

Antes de criar Employee Onboarding, é aconselhavel que voce crie os seguintes documentos:

* [Candidato a Trabalho](/docs/user/manual/pt/recursos-humanos/candidato-emprego)
* [Funcionario](/docs/user/manual/pt/recursos-humanos/funcionario)
* [Departamento](/docs/user/manual/pt/recursos-humanos/departamento)
* [Designação](/docs/user/manual/pt/recursos-humanos/designação)
* [Grau de Funcionario](/docs/user/manual/pt/recursos-humanos/grau-funcionario)

## 2. Como criar Employee Onboarding

1. Vá para: Employee Onboarding > Novo.
1. Selecione o Candidado a Emprego. Uma vez criado, o Funcionario correspondente será automaticamente inserido.
1. Selecion o [Modelo Employee Onboarding](#31-employee-onboarding-template). Com base no modelo selecionado, informação como Departamento, Designação e Grau de Funcionario será automaticamente inserido (se ja foi mencionado no Modelo Onboarding).
1. Digite a Data de Admissão.
1. Salvar e Submeter.


  <img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/employee-onboarding1.png">



> Nota 1: Se o Modelo Employee Onboarding  não foi criado, voce pode preencher directamente a informação no formulario Employee Onboarding.

> Nota 2: O 'Status' do Employee Onboarding irá mudar para Completado uma vez todas actividade associadas estiverem completas.


## 3. Funcionalidades

### 3.1 Modelo Employee Onboarding 

O Modelo Employee Onboarding é um blueprint que contem uma lista de Atividades pre-definidas para Employee Onboarding. Um Modelo Employee Onboarding pode ser criado para um Departamento, Designação e Grau de Funcionario em particular. 

Para criar um novo Modelo Employee Onboarding:

1. Vá para: Recursos Humanos > Ciclo de Vida do Funcionario > Modelo Onboarding Template > Novo.
1. Digite o Departamento, Designação e Grau de Funcionario (opcional).
1. Mencione as Actividades para onboarding. Para cada Atividade, voce pode mencionar o Usuario ou Papel, para quem será atribuida a tarefa.
  
  <img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding-template.png">


### 3.2 Tarefas e Atribuições

Ao submeter o Employee Onboarding, um [Projecto](/docs/user/manual/pt/projectos/projecto) será criado. Dentro do Projeto,[Tarefas](/docs/user/manual/pt/projectos/tarefas) serão criadas para cada Actividade. 

Voce pode visualizar os Projectos e Tarefas criadas como mostram em baixo:

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/project-task.png">

Adicionalmente, cada Actividade pode ser atribuida pesos com base na sua importancia.

<img class="screenshot" alt="Tasks and Assignments" src="{{docs_base_url}}/assets/img/human-resources/employee-onboarding3.png">

Com base no progresso das Tarefas, progresso pode ser atualizado no processo Employee Onboarding.


### 3.3 Criação de Funcionario

Voce pode criar Funcionarios pelo Employee Onboarding (se ainda não existe o funcionario) uma vez todas as tarefas obrigatorias concluidas.

<img class="screenshot" alt="Onboarding Template" src="{{docs_base_url}}/assets/img/human-resources/onboarding-employee.png">


## 4. Topicos Relacionados

1. [Promoção de Funcionario](/docs/user/manual/pt/recursos-humanos/promoção-funcionário)
1. [Separação de Funcionario](/docs/user/manual/pt/recursos-humanos/despedimento-funcionário)
1. [Transferencia de Funcionario](/docs/user/manual/pt/recursos-humanos/transferencia-funcionários)


