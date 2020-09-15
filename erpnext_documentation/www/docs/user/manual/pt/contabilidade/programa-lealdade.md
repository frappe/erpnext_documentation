<!-- add-breadcrumbs -->
# Programa de Lealdade

**Um Programa de Lealdade permite os Clientes ganharem pontos ao gastar um certo valor e deixa eles reclamar os pontos em futuras compras.**

Um Programa de Lealdade é um esforço de marketing estruturado de longo termo que dá incentivos ao Cliente para voltarem. Programas com sucesso são desenhados para motivar os Clientes num mercado de negocio para gerar retornos, fazem compras constantes, e ganhar os competidores.

Para aceder a lista do Programa de Lealdade, vá para:
> Home > Retalho > Operações de Retalho > Programa de Lealdade

## 1. Pre-requisitos
Antes de criar ou usar o Programa de Lealdade, é aconselhavel criar os seguintes:

1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)

## 2. Como Criar um Programa de Lealdade
1. Vá para a lista de Programa de Lealdade e clique em Novo.
1. Digite o Nome do Programa de Lealdade.
1. Selecione se o programa é de Camada Unica ou Multiplas Camadas (ouro, prata, etc).
1. Defina a data de inicio e fim do programa.
1. Selcione o Grupo de Cliente e o Territorio par ao qual o programa será aplicado, por defeito será para todos.
1. Para optar por todos os Clientes por defeito, selecione 'Auto Opt In (Para todos os clientes)'. Caso contrario, o programa precisa ser atribuido pelo [Ficha de Cliente](/docs/user/manual/pt/contabilidade/programa-lealdade#22-pontos-de-lealdade-no-cliente).
1. Na tabela, digite:
 2. **Nome do Nivel**: Para ser atribuido ao Cliente baseado na sua elegibilidade.
 2. **Fator de Coleta**: Quanto é necessário gastar para ganhar 1 Ponto de Lealdade no ERPNext.
 2. **Valor Minimo**: Valor minimo a ser gasto para se qualificar ao Programa/Nivel.
1. Defina o fator de Conversão, ex: 10 USD = 1 ponto.
1. Salvar.

 <img class="screenshot" alt="Loyalty Program" src="{{docs_base_url}}/assets/img/accounts/loyalty-program.png">

### 2.1 Secção de Redenção

* **Fator de Conversão**: Ao redimir os pontos de lealdade, este fator decide quanto dinheiro equivale 1 Ponto de Lealdade. Por exemplo, se o Cliente tem 100 Pontos de Lealdade, e 1 Ponto de Lealdade = 1 USD, então o Cliente soma mais Itens para 100 USD  com os Pontos de Lealdade para futuras compras.

* **Conta de Despesa**: Defina a Conta de Despesa apartir do qual serão ofertados os beneficios. Este é util para rastrear os beneficios oferecidos separadamente. 

* **Duração de Expiração (em Dias)**: Os Pontos de Lealdade colecionados irão expirar depois do numero de dias definidos aqui neste campo.

### 2.2 Pontos de Lealdade no Cliente

Defina uma Secção do Programa de Lealdade na ficha do Cliente para atribuir um Programa ao Cliente.

<img class="screenshot" alt="Loyalty Program 1" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-1.png">

**Pontos de Lealdade** ganhos podem ser vistos no dashboard dos Clientes.

<img class="screenshot" alt="Loyalty Program 2" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-2.png">

### 2.3 Entrada dos Pontos de Lealdade
Vá para: **Contabilidade > Operações de Retalho > Entrada do Ponto de Lealdade**.
Este age como um log para dar uma visão de qual Cliente ganhou pontos, quantos em que Factura de Vendas. Guarda os dados da Factura e Cliente.

<img class="screenshot" alt="Loyalty Program 3" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-3.png">

## 3. Como funciona o Programa de Lealdade?

### 3.1 Ganhar Pontos

*  Primeiro, um **Programa de Lealdade** precisa ser criado como explicado na primeira secção.
* Atribuir este **Programa de Lealdade** a um **Cliente**.
* Criar uma nova Factura de Vendas para o **Cliente** no qual voçê atribuiu o **Programa de Lealdade**.
* Por exemplo, uma factura foi criada como total geral de 3,000 INR e de acordo o **Programa de Lealdade** para o minimo gasto de 2,000 INR, o fator da coleção da Camada de Prata será calculada e para cada 300 INR gastos, o **Cliente** irá receber 1 ponto (daí o total de pontos ganhos nesta transação ser de 15).
* Após submissão da factura, o **Registo de Pontos de Lealdade** serem criados para esta factura (como mostra em baixo na secção do Registo de Programa de Lealdade).
* No nosso **Programa de Lealdade** após um minimo gasto de 6,000, seria elegivel para a Camada Prata. Então, quando outra factura for submetida com o mesmo valor, o total das vendas para este Cliente será de 6,000. Então agora, o **Cliente** será automaticamente actualizado para a Camada Ouro.

> Nota: O minimo gasto no Programa de Lealdade não significa um valor minimo para uma unica factura. Mas sim a soma do total das Factura do Cliente num esquema particular do Programa de Lealdade.

### 3.2 Redimir os Pontos

* Vamos continuar com o exemplo acima aonde nós criamos 1 factura e ganhou 15 pontos. Ao criar outra factura para o mesmo Cliente, vá para a secção de Lealdade de Pontos e active a caixa para 'Redimir Pontos da Lealdade'.
 ![Factura Programa de Lealdade](/docs/assets/img/accounts/loyalty-program-inv.png)
* Os campos para 'Pontos de Lealdade', 'Conta de Redenção' e 'Centro de Custo de Redenção' será visivel nesta secção. A conta e Centro de Custo será procurado apartir do **Programa de Lealdade** atribuido ao **Cliente**.
*  Vendo que o Cliente ganhou 15 pontos, nós podemos usar tudo até expirar. Se nós tentarmos usar mais que tem um erro irá ser mostrado.
* Para este exemplo, nós vamos usar todos os 15 pontos para ser redimido. Fazendo isto irá activar outro campo que irá mostrar o valor calculado usando (Pontos de Lealdade * Fator de Conversão). Portanto, '150' INR será deduzido apartir do valor vendo que o 'Fator de Conversão' foi '10'.
 ![Factura de Lealdade](/docs/assets/img/accounts/loyalty-program-inv2.png)
* Ao submeter, 2 **Registos de Pontos de Lealdade** será criado. Um para redimir, que será um valor negativo e o outro para a factura corrente (vendo que o valor ainda está elegivel por uma das Camadas). O Cliente foi tambem actualizar para Ouro vendo que o valor minino para gastar foi de 6,000.
 ![Pontos de Lealdade](/docs/assets/img/accounts/loyalty-point-2.png)

> Nota: Para uma factura no qual os pontos foram ganhos, se uma factura de devolução for criada, será apagado o Registo de Lealdade de Pontos original e criado uma nova depois de subtrair o valor devolvido do valor original. Tambem, ao cancelar uma factura, os Registos de Lealdade de Pontos subsequentes serão apagados.

### 4. Topicos Relacionados
1. [Centro de Custo](/docs/user/manual/pt/contabilidade/centro-custo)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Grupo de Cliente](/docs/user/manual/pt/CRM/grupo-cliente)

