<!-- add-breadcrumbs -->
<!-- title: HR Settings -->

# Configurações RH

**Configurações RH permitem configurações globlais para os documentos de RH.**

Para aceder as Configurações RH, Vá para:
> Home > Recursos Humanos > Configurações > Configurações RH

Existem varias configurações disponiveis nas Configurações RH.

## 1. Configurações de Funcionário

<img class="screenshot" alt="Previous Work Experience" src="{{docs_base_url}}/assets/img/human-resources/hr-settings1.png">

### 1.1. Idade de Aposentadoria:
Voçê pode digitar a Idade de Aposentaria (em anos) para os seus funcionários. 

### 1.2 Registo de Funcionários a serem criados
O nome das series dos documentos do funcionário são com base nos valores selecinados nestes campos.

* **Nome das Series**: Os documentos dos funcionários criados teram os nome das series usando o selecionado no campo 'Series'.
* **Numero do Funcionário**: O campo Numero do Funcionário fuca visivel ao selecionar este campo e o nome da serie é com base neste campo.
* **Nome Completo**: O documento do funcionário é criado usando o nome completo do funcionário.

### 1.3 Parar os Lembretes de Aniversário
Um email é enviado a todos os funcionários da empresa quando é o aniversario de um deles. Para parar este email de ser enviado voçê pode selecionar esta opção.

### 1.4 Aprovador de Despesas Obrigadoria na Reivindicação de Despesas
No Documento de Reivindicalão de Despesas o campo 'Aprovador de Despesas' é definido como obrigatorio ao selecionar esta opção.

## 2. Configurações de Folha de Pagamento

<img class="screenshot" alt="Previous Work Experience" src="{{docs_base_url}}/assets/img/human-resources/hr-settings2.png">

#### 2.1 Calcular Dias Trabalhado da Folha de Pagamento Com Base Em
Dias Trabalhados no Recibo de Salário pode ser calculado com base na Solicitação de Ferias ou nos registos de Assiduidade. Voçê pode selecionar a opção com base no quer para calcular os Dias Trabalhados.

#### 2.2 Maximo de Horas Trabalhadas contra o Timesheet
Para os Recibos de Salario com base em timesheet, voçe pode definir o maximo permitido de horas contra uma unica timesheet. Defina esta valor par zero para desactivar a validação.

### 2.3 Incluir Feriados no Total de Numero de Dias Trabalhados
Se selecionado, o numero total de dias trabalhados irá incluir feriados, e irá reduzir o valor do salario por dia.

### 2.4 Desactive o Total Arredondado
Voçê pode activar para desactivar o Arredondamento do Total nos Recebos de Salario.

### 2.5 Fração Diaria do Salario para Meio Dia
Com base nesta fração, o salario para Meio Dia será calculado. Por exemplo, o valor é definido para 0.75, o terceiro quarto do salario será entregue para a assiduidade de meio periodo.

### 2.6 Enviar Recibo de Salario por Email para os Funcionários
Um email com o Recibo de Salario é enviado para o resptivo email preferencial do funcionário ao submeter o Recibo de Salario.

### 2.7 Encriptar Recibo de Salario no envio de Emails
O Recibo de Salario em PDF enviado para o funcionário é encriptado usando uma Politica de Senha.

### 2.8 Politica de Senha
O campo fica visivel e obrigatório ao verificar a opção acima para encripar o Recibo de Salario no email.

Aqui esta um exemplo de como definir a Politica de Senha para o envio de PDF  do Recibo de Salarios.

**Exemplo:**

```
SAL-{first_name}-{date_of_birth.year}
```

Este irá gerar a senha tipo SAL-Jane-1972

## 3. Configurações de Ferias

<img class="screenshot" alt="Previous Work Experience" src="{{docs_base_url}}/assets/img/human-resources/hr-settings3.png">

### 3.1 Modelo de Notificação para Aprovação de Ferias
Ao criar ou actualizar a Solicitação de Ferias com o aprovador de ferias, um email é enviado para o aprovador de ferias notificando que uma nova Solicitação de ferias foi criada. O modelo de email para este proposito pode ser selecionado aqui.

### 3.2 Modelo de Notificação de Status de Ferias
Ao Submeter/Cancelar a solicitação de Ferias, o funcionario recebe um email com o status do seu pedido. O modelo de email utilizado para este proposito pode ser sleecionado aqui.

### 3.3 Aprovador de Licenças Obrigatorio para Solicitação de Ferias
No Documento de Solicitação de Ferias o campo 'Aprovador de Ferias' é definido para obrigatorio ao selecionar esta opção.

### 3.4 Mostrar Ferias de Todos os Membros do Departamento no Calendario
As ferias aprovadas para todos os funcionarios no mesmo departamento são mostrados no calendariio ao selecionar esta opção.

### 3.5 Auto Licença com Dinheiro (Encashment)
Se selecionado, o gera um rascunho do registo Licença de Ferias Encashment na data de expiração da alocação de ferias para todos tipo de Ferias com Dinheiro.

### 3.6 Restringir Solicitação de Ferias com Datas Anteriores
Se selecionado, o sistema não irá permitir criar Solicitação de Ferias com Datas Anteriores.

## 4. Configurações de Contractação

### 4.1 Verificar Vagas de Trabalho ao Criar Oferta de Trabalho
Ao criar uma Oferta de Trabalho para uma posicao em particular, as vagas disponiveis no Plano de Pessoal são verificadas para avisar o usuário de exceder o numero de Contractação para a posicao em particular.

{next}
