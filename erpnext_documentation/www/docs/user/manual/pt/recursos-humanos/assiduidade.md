<!-- add-breadcrumbs -->
# Assiduidade

**Assiduidade é o registo que mostra se um Funcionário tem estado presente num dia em particular ou não.**

No ERPNext, voçẽ pode marcar o registo de Assiduidade para um Funcionário no dia a dia usando o doctype Assiduidade.

Para aceder Assiduidade, vá para:

> Home > Recursos Humanos > Assiduidade

## 1. Pre-requisitos

Antes de criar o registo da Assiduidade, é aconselhavel ter o seguinte:

* [Funcionário](/docs/user/manual/pt/recursos-humanos/funcionário)
* [Tipo de Turno](/docs/user/manual/pt/recursos-humanos/gestão-de-turnos)

## 2. Como criar uma Assiduidade

1. Vá para a lista de Assiduidade, clique em Novo.
1. Selecion o Funcionário.
1. Selecione a Data de Assiduidade.
1. Selecione o Turno (opcional).
1. Selecione o Status (Presente, Ausente, De Ferias, Meio Dia).
1. Salvar e Submeter.

    <img class="screenshot" alt="Attendance" src="{{docs_base_url}}/assets/img/human-resources/attendance.png">


> **Nota:** Assiduidade não pode ser marcada pra datas futuras.


Voçê pode ter um relatorio mensal das suas Assiduidade indo para o relatorio **Detalhes da Assiduidade Mensal**.

Voçê pode facilmente definir a Assiduidade dos Funcionários usando a [Ferramenta de Assiduidade do Funcionário](/docs/user/manual/pt/recursos-humanos/ferramente-assiduidade-funcionário).

Voçê pode tambel carregar assiduidade em massa usando o [Carregar Assiduidade](/docs/user/manual/pt/recursos-humanos/carregar-assiduidade).

## 3. Funcionalidades
### 3.1 Marcar Assiduidade não Marcada
No caso da assiduidade de alguns funcionários não ter sido marcada, voçê pode marcar as presenças, ausencias ou meio dia.

#### Como Marcar Assiduidade
1. Vá para a lista de Assiduidade.
1. Clique no botão  **Marcar Assiduidade**.
1. Uma caixa de dialogo irá aparecer.
1. Selecione o Funcionário e o Mês.
1. Selecione o Status se é Present, Ausente ou Meio Dia.
1. Selecion as datas que voçê quer marcar a assiduidade para o funcionário selecionado.
1. Clique no botão **Marcar Assiduidade** e clique em **Sim**.

    <img class="screenshot" alt="Attendance" src="{{docs_base_url}}/assets/img/human-resources/marking_unmarked_attendance.gif">

## 4. Topicos Relacionados

1. [Ferramenta de Assiduidade do Funcionário](/docs/user/manual/pt/recursos-humanos/ferramenta-assiduidade-funcionário)
1. [Gestão de Turnos](/docs/user/manual/pt/recursos-humanos/gestão-de-turnos)
1. [Auto Assiduidade](/docs/user/manual/pt/recursos-humanos/auto-assiduidade)
1. [Carregar Assiduidade](/docs/user/manual/pt/recursos-humanos/carregar-assiduidade)
1. [Solicitação de Assiduidade](/docs/user/manual/pt/recursos-humanos/solicitação-assiduidade)


É tambem, possivel definir a marcação da assiduidade automaticamente com base nos logs check-in/check-out logs dos Aparelhos Biometric/RFID (ou qualquer mecanismo similar que providencie logs de Entrada/SAIDAdo funcionário). Por favor refira a funcionalidade [Auto Assiduidade](/docs/user/manual/pt/recursos-humanos/auto-assiduidade) para mais informações.

{next}
