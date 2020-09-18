<!-- add-breadcrumbs -->
# Razão Imudavel no ERPNext

> Introduzido na Versão 13

Um mudança grande foi feita no ERPNext apartir da vesão 13. Isto muda a forma como as Contas do Razão (Razão Geral) e Razão do Stcok funcionam no ERPNext. Existem varias razões do porquê que os razões devem ser imudaveis. Para lista algumas:

* Registo de Futuras reposições são computacionamente despendiosas. Para postar datas anteriores em transações, todas os fututos registo tem de ser re-feitos.
* No Razão do Stock, aonde as avaliações são com base no metodo First-in-first-out (FIFO), a sequencia inteira pode ser refeita de forma a afectar as avaliações e lucros em transações futuras.
* Impostos pagos por um periodo tambem podem ter de ser alterados.

## De seguida são os impactos no dia a dia de transações

### 1. Voltar Registos ao cancelar transações

<img alt="General Ledger" class="screenshot" src="{{docs_base_url}}/assets/img/articles/general-ledger.png">

Ao cancelar qualquer transação em vez de apagar o Registo do GL para aquela transação, registos reversos serão feitos para cancelar o efeito dessa transação no dia de cancelamento.

<img alt="Document Delete" class="screenshot" src="{{docs_base_url}}/assets/img/articles/document-delete.png">

Vendo que os Registo de GL estão ligados a uma transação nunca serão apagados o que significa que a transação cancelada e seus documentos não podem ser apagados.

### 2. Restrições ao postar datas anteriores em transações de stock

Vendo que os razões são imudaveis agora significa que as futuras transações não podem ser actualizadas ou re-feitas.
Portanto os usuarios não irão poder inserir transações de stock com datas anteriores.

<img alt="Back Dated Entry" class="screenshot" src="{{docs_base_url}}/assets/img/articles/backdated-entry.png">

Por ex. Suponhamos que a Transação do Stock foi feita para o **Item A** como a data de postagem `19-06-2020 23:00:10` depois desta transação voçê não pode postar uma transação para o **Item A** como uma data de postagem anterior a primeira.
