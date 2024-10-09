#### 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.
print('Alô mundo!')

#### 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."
numero = input('Informe um número: ')
print(f'O número informado foi {numero}.')

#### 3. Faça um Programa que peça dois números e imprima a soma.
x = float(input('Informe o primeiro número: '))
y = float(input('Informe o segundo número: '))

print('A soma dos dois números é:', x + y)

#### 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
nota3 = float(input('Informe a 3ª nota: '))
nota4 = float(input('Informe a 4ª nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('A média é:', media)

#### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).
comprimento_m = float(input('Informe um comprimento em metros: '))
comprimento_cm = comprimento_m * 100
print('Este comprimento em centímetros é:', comprimento_cm, 'cm')

#### 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.
largura = float(input('Informe a largura da sala em metros: '))
comprimento = float(input('Informe o comprimento da sala em metros: '))
area = largura * comprimento
print('A área da sala é:', area, 'm²')

#### 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input('Informe o valor ganho por hora em R$/h: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '))
total = valor_hora * horas_trabalhadas
print('O salário do mês foi: R$', total)

#### 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#$C = \frac{5}{9}(F-32)$
temperatura_f = float(input('Informe a temperatura em Fahrenheit: '))
temperatura_c = (5/9) * (temperatura_f - 32)
print('A temperatura é:', temperatura_c, '°C')

#### 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#$F = \frac{9}{5}C + 32$
temperatura_c = float(input('Informe a temperatura em Celsius: '))
temperatura_f = 9/5 * temperatura_c + 32
print('A temperatura é:', temperatura_f, '°F')

#### 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
#$P = 72,7h - 58$

#Lembrando que "algoritmo" nada mais é do que um programa, como todos os outros que você vem fazendo
altura = float(input('Informe a altura em metros: '))
peso_ideal = 72.7 * altura - 58
print('O peso ideal é:', peso_ideal, 'kg')

#### 11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
##### a. Para homens: $P = 72,7h - 58$
##### b. Para mulheres: $P = 62,1h - 44,7$
altura = float(input('Informe a altura em metros: '))
peso_ideal_homens = 72.7 * altura - 58
peso_ideal_mulheres = 62.1 * altura - 44.7

print('O peso ideal com essa altura para homens é:', peso_ideal_homens, 'kg')
print('O peso ideal com essa altura para mulheres é:', peso_ideal_mulheres, 'kg')

#### 12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
remuneracao = float(input('Informe a remuneração em R$ por hora: '))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas: '))

#### 13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
# que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (para simplificação nesse momento,
# não se preocupe em arredondar a quantidade de latas a serem compradas - vamos trabalhar isso em breve)
area = float(input('Informe o tamanho da área a ser pintada em m²: '))

litros_tinta = area / 3 

latas = litros_tinta / 18
preco = latas * 80
print(f'Serão necessárias {latas} latas, custando R$ {preco} no total')

#### 14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link 
# (em minutos).

#Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 
tamanho = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade da conexão em Mbps: '))

tamanho_megabits = tamanho * 8

tempo = tamanho_megabits / velocidade

tempo_minutos = tempo / 60
print(f'O tempo de download é de {tempo_minutos} minutos')

















