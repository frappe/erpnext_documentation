# Tipo de Licença

**Tipo de Licença refere-se a tipo de Licenças atribuidasa a um Funcionario no qual eles podem usar para a Solicitação de Licença.** 


Voce pode criar qualquer quantidade de Tipo de Licença com base nas necessidades da sua Empresa.

Para aceder Tipo de Licença, vá para:

> Home > Recursos Humanos > Licenças > Tipo de Licença

## 1. Como criar Tipo de Licença

1. Vá para Tipo de Licença, clique em Novo.
1. Digite o Nome do Tipo de Licença.
1. Digite o Maximo de Licenças Permitidas, Aplicadas Depois (Dias de Trabalho), Maximo de Dias Continuos Aplicaveis (opcional).
1. Salvar.

    <img class="screenshot" alt="New Leave Type"
    src="{{docs_base_url}}/assets/img/human-resources/new-leave-type.png">

Em baixo uma explanação detalhada de todos os campos e caixa no Tipo de Licença.

* **Max de Licenças Permitidas:** Este campo permite definir o numero maximo de alocações anuais para o Tipo de Licença ao criar a Politica de Licença. 

* **Aplicavel Depois (Dias de Trabalho):** Digite o numero minimo de dias de trabalho aqui. Somente os funcionarios que trabalharam para este numero de dias ou mais são permitidos aplicar este Tipo de Licença. Qualquer outra licença (como Licença Casual, Doença, etc.) atribuida aos Funcionarios depois da sua data de admissão serão tambem consideradas ao calcular os dias de trabalho para o Funcionario.

* **Maximo de Dias Continuos Aplicavel:** Refere-se ao numero maximo de dias este Tipo de Licença em particular pode ser atribuida ao maximo. Se o funcionario passar o numero maximo de dias, a licença estendida será considerada como ‘Licença Sem Pagamento'.

* **É para Continuar:** Se selecionada, o balanço de licenças para este Tipo de Licença será transportado para o proximo periodo de alocação.    

* **É Licença Sem Pagamento:** Este da a certeza que o Tipo de Licença será tratado como licença sem pagamento e o salario será deduzido para este Tipo de Licença.

* **É Opcional:** Licenças Opcionais são os feriados que os Funcionarios escolhem ter de uma lista de Feriados publicados pela Empresa. A Lista de Feriados para Licenças Opcionais podem ter uma numero de feriados, mas voce pode restringir o numero de tais licenças definindo o Maximo de Dias de Licença Permitida no campo.

* **Permitir Balanço Negativo:** Se selecionado, o sistema irá sempre permitir aplicar e selecionar [Pedido de Licença](/docs/user/manual/pt/recursos-humanos/pedido-licença) para este Tipo de Licença, mesmo se não tenha balanço positivo.


* **Incluir feriados dentro das Licenças como Licenças:** Assinale esta opção se voce quer contar os feriados dentro das licenças como ‘licença’. Por exemplo, se um Funcionario aplicou para uma licença na Sexta para Segunda, e Sabado para Domingo são dias de descanso, se a caixa 'Incluir feriados dentro das licenças como licenças' para este Tipo de Licença estiver selecionado, o sistema irá considerar Sabado e Domingo como Licenças tambem. Tais feriados serão deduzidos do numero total de licenças.


* **É Compensatoria:** Licenças Compensatorias são as licenças dadas por trabalhar hora extras ou em feriados, normalmente compensadas como licenças pagas. Voce pode assinalar esta opção para marcar o Tipo de Licença como compensatoria. Um Funcionario pode pedir para licenças compensatorias usando [Solicitação de Licença Compensatoria](/docs/user/manual/pt/recursos-humanos/solicitação-licenças-compensatoria).



## 2. Funcionalidades

### 2.1 Licença Paga

É possivel que funcionarios recebam dinheiro dos Empregadores para licenças não usadas num Periodo de Folha de Pagamento. Nem todos os Tipos de Licença precisam ser pagas, portanto, deve definir "Permitir Pagamento" somente para o Tipo de Licenças que são ou devem ser pagas. 

> **Nota:** Licença Paga é permitida somente no ultimo mes do Periodo da Folha de Pagamento.

<img class="screenshot" alt="Leave Encashment"
        src="{{docs_base_url}}/assets/img/human-resources/leave-encashment.png">

**Dias de Limite de Pagamento:** Este campo indica o numero de dias de licença o Funcionario não será possivel ser pago. Acima dos dias mencionados, o Funcionario pode receber o pagamento das licenças. 

Por exemplo, se tem 10 licenças para um Tipo de Licenças em particular que é paga, e o Funcionario tem 8 dias. Se os Dias de Limite de Pagamento = 5, o Funcionario é dado pagamento somente para 8 - 5 = 3 licenças.

**Componente de Remuneração:** Este campo permite voce especificar o Componente de Salario que será paga aos Funcionarios como parte do seu Salario no Recibo de Salario.

> **Nota:** Ao submeter uma [Licença Paga](/docs/user/manual/pt/recursos-humanos/leave-encashment) para um Funcionario, o ERPNext automaticamente cria um [Salario Adicional](/docs/user/manual/pt/recursos-humanos/salário-adicional) que será adicionado ao Recibo de Salario do Funcionario ao processar a proxima Folha de Pagamento.

### 2.2 Licença Ganha

Licenças Ganhas são as licenças ganhas por um Funcionario depois de trabalhar com a empresa por um certo periodo d tempo. Assinalando "É Licença Ganha" irá alocar licenças pro-rata automaticamente atualizando a Alocação de Licença para as licenças deste tipo em intervalos definidos 'Frequencia das Licenças Ganhas'. 


Por exemplo, um Funcionario é alocado 24 Licenças de Privilegio num ano, aonde a Licença de Privilegio esta definida como Licença Ganha com Alocação Mensal. Neste caso, o Funcionario ganha 2 (24 licenças/12 meses) Licenças Privilegiadas no fim de cada mês. O processo de alocação da licença somente irá alocar licenças considerando o maximo de licenças para o tipo de licença e arredondar para frações.

<img class="screenshot" alt="Earned Leave"
        src="{{docs_base_url}}/assets/img/human-resources/earned-leave.png">

> **Nota:** A alocação inicial para este Tipo de Licença será 0. Licenças serã atualizados no fim do Mes (ou pela definição 'Frequencia de Licença Ganha'). 

### 2.3 Tipo de Licenças Padrão

Tem alguns Tipos de Licença pre-carregadas no sistema, como pode ver em baixo:

- **Licença Sem Pagamento:** Voce pode atribuir esta licenças para varias razões, como assuntos de saude, educação ou razões não evitaveis. A caixa 'Licença Sem Pagamento' para este Tipo de Licença é selecionado por Padrão. O funcionario não é pago por tais licenças.
- **Licença de Privilegio:** Estas são tipo licenças ganhas que podem ser atribuidas por viagens, ferias de familia, etc.
- **Licença por Doença:** Voce pode atribuir este tipo de licenças de não estiver bem de saude.
- **Compensatoria off:** Estas são as licenças compensatorias alocadas a funcionarios por hora extra. A caixa 'É Compensatoria' para este Tipo de Licença esta activa por defeito.
- **Licença Casual:** Pode atribuir esta licença para tratar de assuntos urgentes.

## 3. Topicos Relacionados

1. [Periodo de Licença](/docs/user/manual/pt/recursos-humanos/periodo-ferias)
1. [Politica de Licença](/docs/user/manual/pt/recursos-humanos/politica-de-licença)
1. [Alocação de Licença](/docs/user/manual/pt/recursos-humanos/alocação-ferias)
1. [Pedido de Licença](/docs/user/manual/pt/recursos-humanos/pedido-licença)
1. [Solicitação de Licença Compensatoria](/docs/user/manual/pt/recursos-humanos/solicitação-licenças-compensatoria)
1. [Licença Paga](/docs/user/manual/pt/recursos-humanos/leave-encashment)

