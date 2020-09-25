<!-- add-breadcrumbs -->
# Pedido de Licença

**Pedido de Licença é um documento formal criado por um Funcionario a pedir Ferias por um periodo determinado.**

O ERPNext permite que os seus funcionarios façam o pedido de ferias via Pedido de Ferias e ser aprovadas pelo Aprovador de Licenças.

Para aceder o Pedido de Licença, vá para:

> Home > Recursos Humanos > Sai > Pedido de Licença

## 1. Pre-requisitos

Antes de criar o Pedido de Licença, é aconselhavel ter os seguintes:

* [Departamento](/docs/user/manual/pt/recursos-humanos/departamento)
* [Periodo de Licença](/docs/user/manual/pt/recursos-humanos/periodo-ferias)
* [Lista de Feriados](/docs/user/manual/pt/recursos-humanos/lista-de-feriados)
* [Tipo de Licença](/docs/user/manual/pt/recursos-humanos/tipo-de-ferias)
* [Politica de Licença](/docs/user/manual/pt/recursos-humanos/politica-de-licença)
* [Alocação de Licença](/docs/user/manual/pt/recursos-humanos/alocação-ferias)

## 2. Como criar um Pedido de Licença

1. Vá para Pedido de Licença, clique em Novo.
1. A tabela de Licenças Alocadas será mostrada. Com base nas licenças tiradas, as licenças disponiveis são mostradas para cada Tipo de Licença.

     <img class="screenshot" alt="Leave Application" src="{{docs_base_url}}/assets/img/human-resources/leave-app.png">


1. Selecione o Nome do Funcionario e o Tipo de Licença.
1. Defina a duração da Licença usando a Data de Inicio e Fim. Com base nas datas selecionadas, o campo 'Total de Dias de Licença' e 'Balanço de Licença Antes do Pedido' serão mostrados.
1. Se as Licenças aplicadas são para meio-dia, selecione a caixa 'Meio Dia'.
1. Digite a Razão para a Licença.

    <img class="screenshot" alt="Leave Application" src="{{docs_base_url}}/assets/img/human-resources/leave-app1.png">


1. Selecione o Aprovador de Licença.
1. Selecione a Data de Postagem do Pedido de Licença.
1. Verifique a caixa 'Seguir por Email' para enviar a notificação do Pedido de Licença para o Aprovador.
1. Voce pode tambem ligar ao Recibo de Salario do Funcionario no registo do Pedido de Licença.

    <img class="screenshot" alt="Leave Application" src="{{docs_base_url}}/assets/img/human-resources/leave-app3.png">

1. Clique em Salvar. Um vez salvo o registo, o status do Pedido de Licença muda para 'Aberto', e um email é enviado para o Aprovador de Licença para aprovação. O Modelo de Notificação da Aprovação de Licença pode ser configurado em [Configurações RH](/docs/user/manual/pt/recursos-humanos/configuração-recursos-humanos) em baixo da secção Configurações de Licença.
1. Quando o Aprovador de Licença receber o email, ele pode Aprovar, Rejeitar ou Cancelar o Pedido de Licença. Uma vez feito, o Aprovador pode submeter o Pedido. Ao submeter, o status do documento muda de acordo e um email é enviado para o Funcionario notificando.


> **Nota:** Pedido de Licença não pode ser Submetido se o Salario já foi processado para o mesmo periodo.

O sumario do processo do Pedido de Licença:

- O funcionario aplica a licença pelo Pedido de Licença.
- Aprovador receber a notificação via email. Para isto, a caixa "Seguir por Email" deve estar activa.
- Aprovador revê o Pedido de Licença.
- Aprovador aprova/rejeita/cancela o Pedido de Licença
- O funcionario recebe a notificação do status do seu Pedido de Licença

## 3. Funcionalidades

### 3.1 Configurando Aprovador de Licença

Um aprovador de Licença é um usuario que pode aprovar o Pedido de Licença de um Funcionario. No ERPNext versão 12, Aprovadores de Licença pode ser definido em dois niveis:

* **Nivel de Departamento:** Aprovadores de Licença para cada departamento pode ser configurado na ficha [Departamento](/docs/user/manual/pt/recursos-humanos/departamento). Varios Aprovadores de Licença podem ser definidos num Departamento. O primeiro Aprovador na lista será considerado como o principal Aprovador de Licenças.


    <img class="screenshot" alt="Leave Application - Leave Approvers" src="{{docs_base_url}}/assets/img/human-resources/leave-app4.png">

    Quando um Funcionario pertencente a um departamento em particular aplica para licença, o Aprovador de Licença definido nesse departamento ir+a ser considerado como o seu Aprovador.


* **Nivel de Funcionario:**
Aprovadores de Licença podem tambem ser definidos na ficha do Funcionario para todos.


 <img class="screenshot" alt="Leave Application - Leave Approvers" src="{{docs_base_url}}/assets/img/human-resources/employee-level-approvers.png">


Se o Aprovador de Licença foi definido para ambos Nivel de Funcionario e Nivel de Departamento, o Aprovador Nivel de Funcionario será considerado o principal para Aprovação.

 **Dica:** Se voce quer que todos os usuarios criem o seu Pedido de Licença, voce pode definir os seus 
“ID de Funcionario" como o que deve ser igual nas Configurações de Permissões de Pedido de Licenças.
Verifique [Configurações de Permissão](/docs/user/manual/pt/configuração/usuarios-e-permissões/permissões-usuario.html)
para mais informações.

> **Notas Adicionais:**

>* O Periodo de Pedido de Licença deve ser dentro do period da Alocação de Licença. No caso, voce aplicar para licença entre o periodo de alocação, voce tem que criar dois registos de Pedido de Licença.
>* O Periodo Pedido de Liccença deve estar no ultimo periodo de Alocação de Licença.
>* O Funcionario não pode aplicar para licença nas data adicionadas na [Lista de Bloqueio de Licença](/docs/user/manual/pt/recursos-humanos/lista-de-bloqueio-licenças).

Para entender como o ERPNext permite voce configurar as licenças para funcionarios, verifique [Licenças](/docs/user/manual/pt/recursos-humanos/gestão-ferias/).


## 3. Topicos Relacionados

1. [Tipo de Licença](/docs/user/manual/pt/recursos-humanos/tipo-de-ferias)
1. [Periodo de Licença](/docs/user/manual/pt/recursos-humanos/periodo-ferias)
1. [Politica de Licença](/docs/user/manual/pt/recursos-humanos/politica-de-licença)
1. [Alocação de Licença](/docs/user/manual/pt/recursos-humanos/alocação-ferias)
1. [Lista de Bloqueio de Licença](/docs/user/manual/pt/recursos-humanos/lista-de-bloqueio-licenças)



<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/fc0p_AXebc8?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

{next}
