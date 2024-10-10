## 1. Cálculo de Bônus

#Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

#A meta é 1000 vendas.<br> 
#Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.<br>
#Caso contrário o valor de bônus do funcionário é 0.<br>
#Print o bônus dos 3 funcionários

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

#crie seu código aqui
if vendas_funcionario1 >= 1000:
    print('O funcionário 1 ganhou {} de bônus'.format(vendas_funcionario1 * 0.1))

if vendas_funcionario2 >= 1000:
    bonus = vendas_funcionario2 * 0.1
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus'.format(bonus))

if vendas_funcionario3 >= 1000:
    bonus = vendas_funcionario3 * 0.1
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus'.format(bonus))


## 2. Cálculo de bônus com uma nova regra

#Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

#A meta é 1000 vendas<br>
#Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:<br>

#Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
#Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
#Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

#Use as mesmas variáveis de vendas_funcionários


#crie seu código aqui
#obs: há 2 formas de fazer, com if dentro de if ou então com if e elif. Escolha a que você preferir

if vendas_funcionario1 >= 1000:
    if vendas_funcionario1 >= 2000:
        bonus = 0.15 * vendas_funcionario1
    else:
        bonus = 0.1 * vendas_funcionario1
else:
    bonus = 0
print('O funcionário 1 ganhou {} de bônus'.format(bonus))

#2 Maneira- 

if vendas_funcionario2 >= 2000:
    bonus = 0.15 * vendas_funcionario2
elif vendas_funcionario2 >= 1000:
    bonus = 0.1 * vendas_funcionario2
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus'.format(bonus))

######
if vendas_funcionario3 >= 1000:
    if vendas_funcionario3 >= 2000:
        bonus = 0.15 * vendas_funcionario3
    else:
        bonus = 0.1 * vendas_funcionario3
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus'.format(bonus))

#Exercícios If - Parte 2

#1. Criando um mini sistema de controle de estoque

#- Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
#- Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
#- Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:

#- alimentos -> Estoque mínimo: 50
#- bebidas -> Estoque mínimo: 75
#- limpeza -> Estoque mínimo: 30

#Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.

#Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

#Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.<br>
#Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

#Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.<br>
#Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.


#seu código aqui
produto = input('Qual o produto?')
categoria = input('Qual a categoria do produto?')
qtde = input('Qual a quantidade atual do produto?')

if produto and categoria and qtde:
    qtde = int(qtde)
    if categoria == 'bebidas':
        if qtde < 75:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
    elif categoria == 'limpeza':
        if qtde < 30:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
    else:
        if qtde < 50:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
else:
    print('Preencha todas as informações')

#Lista de Exercícios - Estruturas de Decisão


