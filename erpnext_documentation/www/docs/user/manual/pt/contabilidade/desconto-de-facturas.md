<!-- add-breadcrumbs -->
# Desconto de Facturas

**Desconto de Facturas é a practica em usar uma factura de vendas não paga da empresa para um emprestimo a curto prazo, na qual é issued por um banco ou empresa financeira.**

Para aceder a lista de Decontando Facturas, deve ir:
> Home > Contabilidade > Banco e Pagamentos > Desconto de Facturas

## 1. Pre-requisitos

Voçê precisa criar os seguintes ledgers para poder ter transações de Desconto de Facturas.

* **Emprestimo a Curto Prazo:** Um ledger em baixo de ´Responsabilidade Currentes' > Grupo 'Emprestimos (Responsabilidades)' para Emprestimo.
* **Taxas Conta Bancária:** Uma despesa ledger para as taxa feitas pelo banco.
* **Contas de Recebimentos de Credito:** Uma conta de control do tipo Recebimento.
* **Contas de Recebimentos De Desconto:** Uma conta de recebimento para facturas que foram descontadas.
* **Contas de Recebimentos não Pagos:** Uma conta de recebimento para factura que fora descontadas e continuam não pagas mesmo depois do periodo do emprestimo ter terminado.

## 2. Como Criar uma Transação de Descont de Facturas

1. Vá para a lista de Desconto de Facturas, click em Novo.
1. Digite a Data de Postagem e a Data de Inicio do Emprestimo. Digita o Periodo de Dias do Emprestimo.
1. Selecione factura manual na tabela ou fazendo um click no botão 'Obter Facturas' em cima a direita.
1. Selecione a Conta de Termo para Emprestimo Curto, Conta Bancária e a Conta de Taxas de Banco.
1. Selecione as Contas de Recebimento de Credito, Contas de Recebimento de Desconto e as Contas de Recebimento não pagas.
1. Click em Salvar e Submeter.
1. Depois de Submeter o Formulario Descontos de Factura, click em **Valor Disburse**.
  <img class="screenshot" alt="Lead" src="{{docs_base_url}}/assets/img/accounts/invoice_discounting.png">
1. Voçê irá para o ecrãn [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico). Salve e Submeta o Lançamento Contabilistico.
  ![Lançamento Contabilistico](/docs/assets/img/accounts/invoice-discounting-je.png)
  
## 2. Funcionalidades

### 2.1 Importar Facturas
Click no botão 'Obter Facturas' para importar facturas. Voçê pode importar facturas fazendo o filtro com alguns criterios.

* Facturas criadas para um Cliente especifico.
* Filtro de Datas entre as facturas criadas.
* Valor Maximo e Minimo.

Voçê pode tambem especificar valores multiplos dos filtros acima citados.

### 2.2 Terminar o Emprestimo
Quando voçê termina de pagar o emprestimo no fim do periodo ou antes, voçê pode actualizar o mesmo fazendo o click no botão 'Terminar Emprestimo'.
  ![Lançamento Contabilistico](/docs/assets/img/accounts/invoice-discounting-disbursed.png)
O sistema irá preparar o Lançamento Contabilistico. Faça uma Revisão e Submeta.

### 2.3 Auto Actualização do Razão no fim do Period de Emprestimo
Caso o emprestimo não foi pago no fim do periodo do mesmo, o sistema irá criar um Lançamento Contabilistico atravez de um trabalho programado para mudar o valor da ´Conta de Recebimento Descontado' para 'Conta de Recebimento não Pago'. Desta forma será facil rastrear as facturas que forma descontadas e não pagas no fim do periodo do emprestimo.
