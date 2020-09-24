<!-- add-breadcrumbs -->
# Gestão de Turnos

A secção de Gestão de Turnos no Recursos Humanos ajuda a gerir os turnos dos seus funcionarios.

Para usar a Gestão de Turnos no ERPNext,

  1. Defina o Tipo de Turno.
  2. Digite uma Solicitação de Turno.
  3. Visualize e Atribua a Gestão de Turnos.

## 1. Tipo de Turno

O Tipo de Turno permite criar diferentes tipos de turnos na sua empresa e definir a auto assiduidade para o turno. Auto assiduidade marca presença com base no 'Checkin do Funcionario' para o turno atribuído.

Para aceder o Tipo de Turno, vá para:
> Home > Recursos Humanos > Gestão de Turnos > Tipo de Turno

1. Vá para a lista de Tipo de Turno, Clique em Novo.
2. Digite no Nome, Data de Inicio e Fim
3. Salvar.
<img class="screenshot" alt="Shift Type" src="{{docs_base_url}}/assets/img/human-resources/new-shift-type.png">

## 2. Funcionalidades

Em adição a definir os diferentes turnos na sua empresa, o Tipo de Turno tem tambem a definição para a auto assiduidade. Auto assiduidad mar a presença do funcnionario atribuido a esse turno com base nos registos de 'Checkin do Funcionario'. Auto Assiduidade para todos os tipos de turno são agendados a marcar a cada hora. Voce pode activar o auto assiduidade manualmente para um unico tuno basta pressionar o botão 'Marcar Assiduidade' no Tipo de Turno.
<img class="screenshot" alt="Shift Type" src="{{docs_base_url}}/assets/img/human-resources/shift-type.png">

### 2.1 Hora de Inicio
A hora de inicio do dia em que o Turno começa. A hora é digitada no formato 24Hrs.

### 2.2 Hora de Termino
A hora do termino do dia em que o Turno termina. A hora é digitada no formato 24Hrs.

> Nota: Para casos em que o 'Hora de Termino' seja menor que a 'Hora de Inicio', o turno assume que foi um turno Noturno que começou num dia anterior e terminou no dia seguinte.

### 2.3 Lista de Feriados
Os Feriados Aplicaveis para este turno pode ser selecionados aqui. Se deixado em branco a lista de Feriados Padrão a partir da ficha Funcionario ou da ficha da Empresa será usando.

### 2.4 Activar Auto Assiduidade
Voce pode usar esta opção para activar marcação de assiduidade para funcionarios atribuidos este turno com base nos registo 'Checkin do Funcionario'.

### 2.5 Configurações do Auto Assiduidade
Voce pode usar as seguintes configurações do Auto Assiduidade de acordo as suas necessidades.

### Determinar o Check-in (entrada) e o Check-out (saida)
O Check-in do Funcionario pode nã ser sempre do tipo de log IN/OUT. Para, tais cenarios voce pode usar esta opção para obter os resultados de um sistema de auto assiduidade.

1. Registos Alternados como IN and OUT durante o mesmo turno:
	- A primeira entrada feita como IN seguindo da proximo registo como OUT e a seguinte como IN e assim sucessivamente.
2. Basicamente no Tipo de Log do Checkin do Funcionario:
	- O check-in é determinado como IN ou OU com base no 'Tipo de Log' no registo do Funcionario do Checkin.

### Calculo das Horas de Trabalho com Base em
Horas de Trabalho podem ser calculadas incluindo os intervalos entre o turno ou excluindo os intervalos

Isto pode ser configuradao usando as seguintes opções:

1. Primeiro Check-in e o ultimo Check-out:
	- Selecionando esta opção calcula as horas de trabalho considerando o primeiro IN e o ultimo OU do Funcionario durante o turno.
	- No caso do IN/OUT seja determinado por registos alternativos então o primeiro Checkin é considerado como IN e o ultimo Checkin é considerado como OUT para o propósito do calculo das horas.
2. Cada Check-in e Check-out valido:
	- Selecionando esta opções exclue a duração de tempo no qual o Funcionario fez o checked out.
	- i.e. Somente a hora durante o qual o funcionario fez o checked in é considerado como horas de trabalho.

### Inicia o check-in antes do inicio da hora de turno
Muitas vezes os funcionarios fazem o check-in minutos antes do turno começar. Para considerar este check-ins como parte do turno durante o calculo de assiduidade, voce pode definir esta valor.

### Permitir check-out depois da Hora do turno Terminar
Muitas vezes os funcionario fazem check-out depois da hora do turno terminar. Para considerar estes check-outs como parte do turno durante o calculo da assiduidade, voce pode configurar este valor.

### Limite de Horas de Trabalho para Meio Periodo
Se o numero actual de horas de trabalho for menos que o valor dado neste campo então o funcionario é marcado como 'Meio Periodo'. Se voce não quiser marcar Meio Periodo com base nas horas de trabalho, voce deve definir este valor para zero.

### Limite de Horas de Trabalho para Ausencia
Se o numero actual de horas de trabalho for menos que o valor dado neste campo então a assiduidade do funcionario é marcada como 'Ausente'. Se voce não quiser marca Ausencia com base nas horas de trabalho, voce deve definir esta valor para zero.

### Processar Assiduidade Depois
A data em que a 'Auto Assiduidade' deve iniciar a assiduidade. Voce deve definiar a data no qual tem Funcionarios com Registo de Checkin para este turno.

### Ultima Sincronização do Checkin
Este é o periodo em que as assiduidades são marcada com base nos registos do Checkin do funcionario. Voce deve definir a data e hora no qual o Checkin do Funcionario foi sincronizado. Caso contrario o funcionario pode ser marcado como ausente por falta de registos de check-in.

# Pedido de Turno


## 1. Pre-requisitos
Para criar um Pedido de Turno, estes devem ser criados primeiro:

* [Funcionario](/docs/user/manual/pt/recursos-humanos/funcionario)
* [Tipo de Turno](docs/user/manual/pt/recursos-humanos/gestão-de-turnos#1-tipo-de-turno)]

Pedido de Turno é usando pelo Funcionario para pedir um Tipo de Turno em particular.

Para criar um novo Pedido de Turno vá para:
> Recursos Humanos > Gestão de Turno > Pedido de Mudança


1. Vá para a Lista de Pedido de Turno, clique em Novo.
1. Selecione o Funcionario e o Tipo de Turno
1. Defina a duração do Turno usando das Datas de Inicio e Fim.
1. Selecione Aprovador
1. Salvar

	<img class="screenshot" alt="Shift Request" src="{{docs_base_url}}/assets/img/human-resources/shift-request.png">

# Atribuição de Turno

* Uma vez o Pedido de Turno aprovado e submetido irá automaticamente criar a Atribuição de Turno para o Funcionario.

	<img class="screenshot" alt="Shift Assignment" src="{{docs_base_url}}/assets/img/human-resources/shift-assignment.png">

> Nota: A Atribuição para tipo de turno activo irá ser para um periodo fixo ser houver uma data de fim, caso contrario, será tratado como um turno de continuação sem Data de Termino. Usuarios podem actualizar a Data de Termino e o status mesmo que já tenha submetido o documento.

### 3.1 Definindo Aprovador de Pedido de Turno

Um Aprovador de Pedido de Turno é um usario que pode aprovar o Pedido de Turno do Funcionario. No ERPNext vesão 13, o Aprovador de Pedido de Turno pode ser definido em dois niveis:

* **Nivel de Departamento:** Aprovadores de Pedido de Turno para cada departamento pode ser configurado na ficha do [Departamento](/docs/user/manual/pt/recursos-humanos/departamento). Varios Aprovadores de Pedido de Turno podem ser definidos nun Departamento.


    <img class="screenshot" alt="Shift Request Approvers" src="{{docs_base_url}}/assets/img/human-resources/shift-request-approvers.png">

    Quando um Funcionario que pertence a um departamento em particular faz o pedido de turno, o Aprovador de Pedido de Turno definido na ficha do Departamento do Funcionario irá ser considerado como seu Aprovador.


* **Nivel de Funcionario:**
Aprovador de Pedido de Turno pode tambem ser definido no formulario de Funcionario.


 <img class="screenshot" alt="Shift Request Approvers" src="{{docs_base_url}}/assets/img/human-resources/employee-level-approvers.png">


Se o Aprovador de Pedido de Turno esta definido em ambos Nivel de Funcionario e Departamento, o Nivel de Funcionario será considerado como padrão para este caso.

	{next}
