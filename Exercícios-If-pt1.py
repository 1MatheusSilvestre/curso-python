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
