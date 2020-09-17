<!-- add-breadcrumbs -->
# Arranjando o Erro do Ano Fiscal

Ao criar um registo, o sistema valida se as datas (Data de Postagem, Data de Transação, etc) pertencem ao Ano Fiscal corrente. Caso não, o sistema mostra uma mensagem de erro:

`Data ##-##-#### não está no ano fiscal`

Voçê poderá receber esta mensagem se o seu Ano Fiscal mudou, e o novo Ano Fiscal ainda não esta por defeito. Para ter a certeza que o novo Ano Fiscal é atualizado nas transações, voçê deve configurar de acordo as instruções.

#### Criar uma Novo Ano Fiscal

Somente o Usuario com Papel atribuido de Gestor de Sistema tem permissão para criar um Novo Ano Fiscal. Para criar, vá para:

`Contabilidade > Configuração > Ano Fiscal`

Clique [aqui](/docs/user/manual/pt/contabilidad/ano-fiscal) para aprender mais sobre o Ano Fiscal.

#### Definir o Ano Fiscal como Padrão

Depois do Ano Fiscal ser salvo, voçê irá encontrar a opção para definir o Ano Fiscal como Padrão.

<img alt="Debit Credit Not Equal" class="screenshot" src="{{docs_base_url}}/assets/img/articles/fiscal-year-error-1.png">

Ano Fiscal Padrão será actualizado nas Configurações Gerais tambem. Voçê pode manualmente actulizar o Ano Fiscal Padrão aqui:

`Configurações > Configurações > Padrões Gerais`

<img alt="Debit Credit Not Equal" class="screenshot" src="{{docs_base_url}}/assets/img/articles/fiscal-year-error-2.png">

Salve os Padrões Gerais, e Recarregue o seu ERPNext. Depois, o Ano Fiscal padrão será auto-actualizado nas transações.

Nota: Nas transações, voçê pode manualmente selcionar o Ano Fiscal que precisa, apartir da secção Mais Info.

<!-- markdown -->

{next}
