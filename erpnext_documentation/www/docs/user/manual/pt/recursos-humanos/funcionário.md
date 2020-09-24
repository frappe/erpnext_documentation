<!-- add-breadcrumbs -->
# Funcionário

**Um individuo que trabalha meio-periodo ou tempo inteiro sobre um contracto de trabalho, e tem os seu direitos e deveres reconhecidos da sua empresa é seu Funcionário.**

No ERPNext, voce pode gerir a ficha Funcionários. Captura a demografia, detalhes pessoais e profissionais, detalhes de admissão de demissão, etc. do Funcionário.


Para aceder a ficha do Funcionário, vá para:

> Home > Recursos Humanos > Funcionário

## 1. Pre-requisitos

Antes de criar o Funcionário, é aconselhavel criar o seguinte:

* [Tipo de Contrato](/docs/user/manual/pt/recursos-humanos/tipo-de-contracto)
* [Candidato a Emprego](/docs/user/manual/pt/recursos-humanos/candidato-emprego) 
* [Departamento](/docs/user/manual/pt/recursos-humanos/departamento)
* [Grau do Funcionario](/docs/user/manual/pt/recursos-humanos/grau-funcionario)
* [Filial](/docs/user/manual/pt/recursos-humanos/filial)
* [Designação do Funcionario](/docs/user/manual/pt/recursos-humanos/designação)
* [Politica de Licença](/docs/user/manual/pt/recursos-humanos/politica-de-licença)
* [Lista de Feriados](/docs/user/manual/pt/recursos-humanos/lista-de-feriados)
* [Leave Encashment](/docs/user/manual/pt/recursos-humanos/leave-encashment)
* [Tipo de Turno](/docs/user/manual/pt/recursos-humanos/gestão-de-turnos)
* [Seguro de Saude do Funcionário](/docs/user/manual/pt/recursos-humanos/seguro-saúde)

## 2. Como criar um Funcionário
  
1. Vá pra a lista de Funcionário, clique em Novo.
1. Digite os dados pessoais do Funcionário como Nome, Genero, Data de Nascimento e Data de Admissão.
1. Salvar.

Como mostra em baixao, todos os campos obrigatorios estão carregados.


## 3. Funcionalidades

Para alem dos campos obrigatorios, alguns dados adicionais que podem ser capturados na ficha do Funcionário são:

### 3.1 Tipo de Contrato

Voce pode definir um [Tipo de Contrato](/docs/user/manual/pt/recursos-humanos/tipo-de-contracto) como Interno, Contracto, Tempo Inteiro, Meio-Periodo, Testes, etc.


### 3.2 Criar um Usuario ERPNext

O ID do Usuario pode ser ligado ao Funcionario. No cao do ID do Usuario não tenha sido criado, pode fazer o clique no 'Criar Novo Usuario' para criar um. 
 
Ao fazer o clique na caixa 'Criar Permissão do Usuario', o acesso do Funcionario a outros registos pode ser restrito. Verifique [Adicionando Usuarios](/docs/user/manual/pt/configuração/usuarios-e-permissões/adicionar-usuarios) para aprender como criar usuarios e adicionar permissões.


### 3.3 Detalhes de Adesão

Os Detalhes de Adesão do Funcionario como Data de Oferta, Data de Confirmação, Fim de Contracto, Dias de Notificação (Dias), e Data de Aposentadoria podem ser capturados. 


### 3.4 Departamento e Grau

Num empresa, os Funcionarios são agrupados com base em [Departamentos](/docs/user/manual/pt/recursos-humanos/departamento), [Gray](/docs/user/manual/pt/recursos-humanos/grau-funcionario), [Designação](/docs/user/manual/pt/recursos-humanos/designação), e [Filial](/docs/user/manual/pt/recursos-humanos/filial). 

Na secção do Departamento e Grau, estes detalhes do Funcionario podem ser salvos. No campo 'Reporta a', a pessoa para quem o Funcionario tem que reportar as suas tarefas pode ser capturado.


### 3.5 Detalhes de Licença

Nos Detalhes de Licença, voce pode salvar a [Politica de Licença](/docs/user/manual/pt/recursos-humanos/politica-de-licença) e [Lista de Feriados](/docs/user/manual/pt/recursos-humanos/lista-de-feriados. Politica de Licença especifica o tipo e numero de ferias um Funcionario pode ter, e Lista de Feriados é a lista que contem as datas de Feriados e Fins de semana.


### 3.6 Detalhes de Salario

Aqui, o modo de pagamento do salario, i.e. pelo Banco, Cheque ou Dinheiro pode ser selecionado.


### 3.7 Detalhes de Contacto

Informação de Contacto do Funcionario tais como Numero de Telefone, Endereço Corrente e Permanente, Email Pessoal e da Empresa podem ser guardados aqui. No campo Email Preferencial, ou o Email da Empresa, Email Pessoal ou ID do Usuario podem ser escolhidos de acordo a preferencia do funcionario.
 

### 3.8 Detalhes Pessoais

Detalhes Pessoais de um Funcionario como Detalhes da Familia como nome ocupação dos parentes, mulher e filhos, detalhes de passporte, etc, pode ser salvos. 

### 3.9 Qualificação Educacional

Aqui, os Detalhes de Qualificação Educacional como as Escolas/Universidades, Qualificação, Nivel e Ano que passou do Funcionario pode ser salvo como mostra em baixo:

<img class="screenshot" alt="Educational Qualification" src="{{docs_base_url}}/assets/img/human-resources/educational-qualification.png">

Adicionalmente, detalhes como Classe/Percentagem e Disciplinas podem tambem ser incluidas ao fazer a seta para baixo na tabela de Educação.

### 3.10 Experiência Laboral Anterior

Como na Qualificação Educacional, Experiência Laboral Anterior de um Funcionario pode tambem ser capturada na tabela Historico de Trabalho Externo como mostra:

<img class="screenshot" alt="Previous Work Experience" src="{{docs_base_url}}/assets/img/human-resources/previous-work-experience.png">

Adicionalmente, detalhes como Contacto da empresa anterior e o Total de Experiencia no Ano pode ser salvo tambem.

### 3.11 Saida

Detalhes da Saída do funcionario como Demissão, Entrevista de Saida e detalhes do [Subsidio de Ferias](/docs/user/manual/pt/recursos-humanos/leave-encashment) podem ser incluidos. Quano status do Funcionario é 'Despedido', é obrigatorio preencher a Data de Demissão. 

> **Nota:** Uma vez o status do Funcionario 'Despedido', esta ficha do Funcionario não estará disponivel para futuras transações.

### 3.12 Funcionalidades Adicionais
Alguma funcionalidades adicionais incluidas na ficha do Funcionario são:

* Contacto de Emergencia
* Seguro de Saude
* Biografia Pessoal
* Historico na Empresa

## 3. Topicos Relacionados

1. [Gestão de Licenças](/docs/user/manual/pt/recursos-humanos/gestão-ferias)
1. [Gestão de Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento) 



<hr>

<div class="embed-container">    
    <iframe src="https://www.youtube.com/embed/kkwOzeU4wFU?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>


