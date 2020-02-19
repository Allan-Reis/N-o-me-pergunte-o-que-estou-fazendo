#agenda de contatos
def frank (n,tel):
agenda[n]=tel
def dinossauro (nome):
print('----consultando os contatos------')
consulta=input('digite o nome da pessoa que deseja consultar: ')
if consulta in agenda.keys():
  print('{0}: {1}'.format(consulta,agenda[consulta]))
else:
  print('Você não possui esse contato!!')
def transformes (nome):
z='sim'
print('----alterando os nnumeros do contato------')
print(agenda)
while z == 'sim':
  x = input('Você deseja alterar, adicionar ou remover um numero do seu contato?')
  if x == 'alterar':
    nome = input('digite o nome da pessoa que deseja fazer as alteraçoes: ')
    print('{0}: {1}'.format(nome,agenda[nome]))
    numero_antigo=str(input('digite o numero que deseja alterar: '))
    if numero_antigo in agenda[nome]:
      agenda[nome].remove(numero_antigo)
      agenda[nome].append(str(input('digite o numero novo: ')))
      print(agenda[nome])       
    #agenda[nome].pop(agenda[nome].index(numero_antigo))     
    else:
      print('numero digitado não existe no contato')
  if x == 'adicionar':
    nome = input('digite o nome da pessoa que deseja adicionar o numero: ')
    agenda[nome].append(input('digite o numero desejado para adicionar ao seu contato'))
    print('{0}: {1} , numero adicionado com sucesso !!'.format(nome,agenda[nome]))
  if x == 'remover':
    nome = input('digite o nome da pessoa que deseja remover algum numero do contato: ')
    print('{0}: {1}'.format(nome,agenda[nome]))
    numero = input('digite o numero a ser removido: ')
    agenda[nome].remove(numero)
    print('nome:{0}'.format(nome),'\n','numero(s) para contato {1}'.format(nome,agenda[nome]))
  z = input('se quer continuar a fazer alterações digite (sim) caso não digite (não): ')
def tyranossauro (nome):
print('---remover contatos da sua agenda----')
nome = input('digite o nome do contato que deseja remover: ')
if nome in agenda.keys():
  x = input('Tem certeza que deseja contato esse numero da sua agenda? s/n: ')
  if x == 's':
    del (agenda[nome])
    print(agenda)
  else:
    print('-----operação cancelada-----')
z='sim'
while z == 'sim':
 print('----Menu de seleção-----')
 print('digite (1): Para criar ou adicionar um contato a sua agenda','\n','digite (2): Para a consulta de um contato','\n', 'digite (3): Para remover um contato da sua agenda','\n', 'digite (4): Para alterar os dados de um contato da sua agenda')
 x = str(input('Digite a opção desejada: '))
 if x == '1':
   quant_pessoas = int(input('digite quantas pessoas deseja adicionar a sua agenda de contatos: '))
   agenda={}
   for i in range(quant_pessoas):
     nome = input('digite o nome da pessoa: ')
     quant_numeros = int(input('Quantos numeros essa pessoa tem?: '))
     telefones=[]
     for i in range(quant_numeros):
       tel = input('digite o numero: ')
       telefones.append(tel)
       frank(nome,telefones)
   print('contato cadastrado com sucesso!!')
   z = str(input('se deseja continuar digite (sim), caso não, digite (não): '))
   z = z.lower()
 if x == '2':
   dinossauro(nome)
   z = str(input('se deseja continuar digite (sim), cso não, digite (não): '))
   z = z.lower()
 if x == '4':
   transformes(nome)
   z = str(input('se deseja continuar digite (sim), cso não, digite (não): '))
   z = z.lower()
 if x == '3':
   tyranossauro(nome)
   z = str(input('se deseja continuar digite (sim), cso não, digite (não): '))
   z = z.lower()
