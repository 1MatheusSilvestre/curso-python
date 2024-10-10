# Exercícios

## 1. Cadastro de CPF

#Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.

#Ex: 'Insira seu CPF (digite apenas números)'

#Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"

cpf = input('Insira seu CPF')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente e digite apenas números')


## 2. Melhorando nosso Cadastro de CPF

#Agora, além das validações anteriores, vamos criar um input que permita que o usuário insira pontos, traços e inclusive espaços vazios.

#Nosso programa deve "tratar" o que o usuário inserir para padronizar o CPF dele em apenas números.

#A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.

#No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.

cpf = input('Insira seu CPF')
cpf = cpf.strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente e digite apenas números')

## 3. Cadastro de e-mails

#A Hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido, verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:

#liragmail.com NÃO é um e-mail válido
#lira@gmail NÃO é um e-mail válido
#lira@gmail.com é um e-mail válido

#Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
#1. Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
#2. Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido

#Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string

nome = input('Digite seu nome')
email = input('Digite seu e-mail')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluído')
    else:
        print('Email inválido')
else:
    print('Digite seu nome e e-mail corretamente')

#Lista de Exercício 

#### 1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#<pre>
#Compara duas strings
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.
#</pre>
print('Compara duas strings')

s1 = input('String 1: ')
s2 = input('String 2: ')
print(f'Tamanho de "{s1}": {len(s1)} caracteres')
print(f'Tamanho de "{s2}": {len(s2)} caracteres')

if len(s1) == len(s2):
    print('As strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')
    
if s1 == s2:
    print('As strings possuem conteúdos iguais.')
else:
    print('As duas strings possuem conteúdo diferente.')

#### 2. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
#<pre>
#Valida e corrige número de telefone
#Telefone: 461-0133
#Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 3461-0133
#</pre>
print('Valida e corrige número de telefone')

tel = input('Telefone: ')
tel = tel.replace('-', '')
if len(tel) == 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    tel = '3' + tel
    print(f'Telefone corrigido sem formatação: {tel}')
    print(f'Telefone corrigido com formatação: {tel[:4]}-{tel[4:]}')
else:
    print('O telefone não tem 7 dígitos.')
