<!-- add-breadcrumbs -->
# Entradas de Contabilidade

O conceito de contabilidade é explicado com o seguinte exemplo: Nós vamos por a 
"Tea Stall" como uma empresa e ver como criar as entradas de contabilidade para o negocio.

Mama (The Tea-stall dono) investiu Rs. 25000 par acomeçar o negocio.
![JE](/docs/assets/img/accounts/je-1.png)

## 1. Investimento
Mama investiu Rs. 25000 na Empresa, esperando ter algum lucro. Em outras palavras,
a empresa é obrigada a pagar Rs. 25000 a Mama no futuro. Portanto, a conta
"Mama" é uma conta de responsabilidade e a credito. Balanço de dinheiro da Empresa será
aumentado devido o investimento feito. "Dinheiro" é um activo para a empresa e será debitado.

  A empresa precisa de equipamento (fogão, Chaleira, chavenas, etc.) e material crú (chá, açucar, leite, etc.) de imediato. Eles decidem comprar numa loja proxima, "Super Bazaar" cujo o dono é um amigo, pelo que obtem um credito. Custo do Equipamento ficou em Rs. 2800 e material crús Rs. 2200. Ele pagou Rs. 2000 fora do custo total que é Rs. 5000. Isto pode ser guardado no ERPNext usando [Payment Entry](/docs/user/manual/pt/contabilidade/entrada-pagamento).

![JE](/docs/assets/img/accounts/je-2.png)

## 2. Activos
Equipamentos são "Activos Fixos" (porque eles tem uma vida longa) e o material crú são "Activos Currentes" (vendo que são usados no dia a dia), 
da empresa. Então "Equipamentos" são contas de "Stock em Mão" que foram debitadas para aumentar o valor. Ele paga 2000, portanto conta "Dinheiro" será reduzida este valor,
e creditado aonde tem obrigação de pagar Rs. 3000 a "Super
Bazaar" depois, então Super Bazaar será creditado Rs. 3000.

  Mama (Que faz todas as entradas) decide fazer o registo de vendas no fim do dia, para que ele possa analizar as vendas diarias. Ao fim do periodo do primeiro dia, a tea stall vende 325 chavenas de chá, que dá um lucro de Rs. 1625. O dono regista a sua primeira venda do dia.

![JE](/docs/assets/img/accounts/si-1.png)

## 3. Recebimentos
Recebimento foi alocado na conta "Sales of Tea" que foi creditado para aumentar
o valor e o mesmo valor será debitado para conta "Dinheiro". Vamos dizer, para fazer 325 chavenas de chá,
custa Rs. 800, portanto "Stock em Mão" será reduzido (Cr) por Rs. 800 e a despesa será alocada na conta "Custo de Venda de Bens" pelo mesmo valor.

No fim do mês, a empresa pagou a rende de (Rs. 5000) e
o salário de um funcionário (Rs. 8000), que entrou no primeiro dia.

![JE](/docs/assets/img/accounts/je-3.png)

## 4. Alocar Lucros

Ao passo que o mês avança, a empresa comprou mais material para o negocio.
Após um mẽs alocou lucro para a "Folha de Balanço" e "Lucros e Percas". Lucros pertencem a Mama e não a ha empresa sendo 
ser uma responsabilidade para a empresa (tem que pagar a Mama). quando a Folha de Balanço não está balanceada
i.e. Debito não é igual ao Credito, o lucro nã pode ser alocado. Para alocar o lucro, as contas de lucro e percas tem que zerar. O lucro/perca é transferido para a conta de Responsabilidade e começa do zero. Isto é feito usando [Voucher de Término de Período](/docs/user/manual/pt/contabilidade/voucher-termino-periodo).

**Explicação**: Valor liquido das vendas e despesas da Empresa são Rs. 40000 e Rs. 20000
respectivamente. Então, a empresa teve um lucro de Rs. 20000. Para alocar a entrada de lucro,
da conta "Lucro e Perca" foi debitada e "Conta Capital" foi creditada. O balanço liquido é Rs. 44000 e ha algum material
disponivel no valor de Rs. 1000.

### Topicos Relacionados
1. [Entrada de Pagamento](/docs/user/manual/pt/contabilidade/entrada-pagamento)
1. [Adiantamento de Pagamento](/docs/user/manual/pt/contabilidade/adiantamento-pagamento)
1. [Congelar Entradas de Contabilidade](/docs/user/manual/pt/contabilidade/articles/freeze-accounting-entries)
1. [Post Dated Cheque Entry](/docs/user/manual/pt/contabilidade/articles/post-dated-cheque-entry)
1. [Ajustar Valor Retido de Pagamento](/docs/user/manual/pt/contabilidade/articles/adjust-withhold-amount-payment-entry)
1. [Bulk Entrada de Pagamento](/docs/user/manual/pt/contabilidade/articles/bulk-payment-entry)
1. [Botão de Registo de Diferença](/docs/user/manual/pt/contabilidade/articles/difference-entry-button)
