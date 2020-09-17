<!-- add-breadcrumbs -->
# Ordens e Facturas Recorrentes

Se voçẽ tiver um contracto com um **Cliente** aonde voçê cobra o Cliente mensalmente, trimestral ou anual, voçẽ pode usar esta funcionalidade de Ordens e Facturas Recorrentes.

## 1. Considere o cenario

Subscrição para o seu ERPNext requer uma renovação anual. Nós geramos uma Ordem de Venda para criar uma Proforma. Para automatizar a renovação da proforma, nós definimos a Ordem de Venda original como recorrente. Ordens e Facturas Recorrentes são criados automaticamente antes da conta do cliente expirar, que precisa renovar. Estas Ordens e Facturas Recorrentes são tambem enviadas por email automaticamente para o Cliente.

Funcionalidade para definir o documento como Recorrente está disponivel em Ordens de Venda, Factura de Vendas, Ordens de Compra e Facturas de Compra.

## 2. Como criar Ordens e Facturas Recorrentes
Opção para definir o documento recorrente fica visivel somente depois de submeter. Está é a opção **Auto Repetir**.

1. Clique no botão + proximo ao Auto Repetir.
1. Selecione a Referencia do Doctype.
1. Selecione o Documento.
1. Defina a Data de Inicio e Data de Fim(opcional).
1. Selecione a frequencia diaria, semanal, etc,.
1. Salvar.

Aqui esta a explicação dos campos:

* **Da Data e Até a Data:** Este define o periodo do contracto com o cliente.
* **Repetir no Dia do Mês:** Se este tipo de recorrencia for Mensal, então será num dia do Mês no qual a factura recorrente será gerada.
* **Repetir no Ultimo dia do Mês:** Factura Recorrentes serâo criadas no ultimo dia de cada Mẽs.
* **Notificar por Email:** Endereço de Emails (separados por virgula) no qual as factura recorrentes serão enviadas depois de serem auto-geradas.

Para mais detalhes sobre Auto Repetir [Clique aqui](/docs/user/manual/pt/automação/repetição-automatica)

## 3. Gerindo Excepções

Numa situação aonde facturas recorrentes não são criadas como sucesso, o usuario com Papel Gestor de Sitema é notificado via email. Falha ao criar a factura de recorrencia pode ter varios motivos como Email errado etc.

Ao receber a notificação, se a causa da falha for fixa (como email errado) dentro de 24 horas, então as factura recorrentes serão geradas automaticamente. Se o problema não foi arranjada dentro deste periodo, o documento dever ser criado manualmente.

### 4. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Facturas de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
1. [Ordens de Venda](/docs/user/manual/pt/vendas/ordem-vendas)
1. [Ordens de Compra](/docs/user/manual/pt/compras/ordem-de-compra)
