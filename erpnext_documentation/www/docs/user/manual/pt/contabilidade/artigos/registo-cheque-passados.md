<!-- add-breadcrumbs -->
# Registo de Cheques com Datas Anteriores

Cheque com Datas Anteriores são cheques datados em datas futuras. As Partes normalmente dão cheques com datas avançadas, como Adiantamento de Pagamento. Este cheque será liquidado somente na data do cheque.

No ERPNext, crie Registo de Pagamento para cheques com data anterior.

####Novo Registo de Pagamento

Para abrir um novo Lançamento Contabilisticos vá para

`Explorar > Contabilidade > Lançamento Contabilistico > Novo`

#### Defina a Data de Postagem

Assumindo que a Data do Cheque serja 31 de Dezembro, 2016 (ou qualquer data futura). Como resultado, este registo no seu razão do banco irá aparecer na Data de Postagem actualizada.

<img alt="JE Posting Date" class="screenshot" src="{{docs_base_url}}/assets/img/articles/post-dated-1.png">

Nota: Data de Referencia do Registo de Pagamento deve ser igual ou menor que a Data de Postagem.

####Step 3: Salvar e Submeter

Depois de digitar os detalhes necessários, Salve e Submete o Registo de Pagamento.

####Ajustar a Data de Postagem do Registo do Cheque

Voçê pode ajustar a Data de Postagem do Registo de Pagmento contra uma Factura [Ferramenta de Reconciliação de Pagamento](/docs/user/manual/pt/contabilidade/reconcialiação-pagamento).

Quando o cheque for liquidado, ex. na data actual do cheque, voçê pode actualizar a Data de Liquidação via [Ferramentoa de Reconciliação de Pagamento](/docs/user/manual/pt/contabilidade/reconciliação-pagamento).

No Plano de Contas, voçê pode encontrar o valor do Registo de Pagamento já a reflectir a Conta do Banco. Voçê deve verificar **Extracto de Reconciliaçáo Bancaria**, um relatorio no modulo de contas para verificar a diferença do balanço do banco e do sistema, e o balanço actual nos extractos do banco.
<!-- markdown -->

{next}
