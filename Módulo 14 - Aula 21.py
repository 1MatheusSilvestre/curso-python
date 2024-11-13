#23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.

# 1. Comprar apenas latas de 18 litros: (apenas latas inteiras)
def area_pintada():
    area = int(input('Defina a área a ser pintada:'))
    return area 


def litros_tinta(area):
    litros = area / 6
    return litros


def calcular_latas(litros):
    latas = litros / 18
    if latas > int(latas):
        latas = int(latas) + 1
    return latas


def custo_latas(latas):
    custo = latas * 80
    return custo


area = area_pintada()
litros = litros_tinta(area)
latas = calcular_latas(litros)
custo = custo_latas(latas)

print('Latas', latas, 'Valor R$',custo)

#2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)
def area_pintada():
    area = int(input('Defina a área a ser pintada:'))
    return area 


def litros_tinta(area):
    litros = area / 6
    return litros


def calcular_galao(litros):
    galao = litros / 3.6
    if galao > int(galao):
        galao = int(galao) + 1
    return galao


def custo_galao(galao):
    custo = galao * 25
    return custo


area = area_pintada()
litros = litros_tinta(area)
galao = calcular_galao(litros)
custo = custo_galao(galao)

print('Galões', galao, 'Valor R$',custo)

#3. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Sempre arredonde os valores para cima, isto é, considere latas cheias.
# Pegar a área a ser pintada
def area_a_ser_pintada():
    area = int(input("Escreva qual a área a ser pintada (m²):"))
    return area


# Pegar quantos litros eu vou precisar de tinta
def calcular_litros_tinta(area):
    litros = area / 6
    return litros


# Calcular quantas latas e quantos galões eu vou precisar
    # Calcular quantas latas inteiras eu vou precisar
    # Calcular quantos litros ainda faltam comprar
    # Calcular quanto custa preencher esses litros que faltam com galao
    # Calcular quanto custa preencher esses litros que faltam com latas
    # Escolher a opção mais barata
def calcular_qtde_latas_galoes(litros):
    latas = 0
    galoes = 0

    latas_inteiras = int(litros / 18)

    litros_faltam = litros % 18
    # se for preencher com latas
    custo_latas_extras = 1 * 80

    # se for preencher com galoes
    galoes = litros_faltam / 3.6 # 2
    if galoes > int(galoes):
        galoes = int(galoes) + 1
    custo_galoes_extras = galoes * 25

    if custo_latas_extras < custo_galoes_extras:
        latas = latas_inteiras + 1
        galoes = 0
    else:
        latas = latas_inteiras
    return latas, galoes


# Calcular o custo total
def calcular_custo(latas, galoes):
    custo_latas = latas * 80
    custo_galoes = galoes * 25
    custo = custo_latas + custo_galoes
    return custo


area = area_a_ser_pintada()
litros = calcular_litros_tinta(area)
latas, galoes = calcular_qtde_latas_galoes(litros)
custo = calcular_custo(latas, galoes)
print("Litros", litros)
print("Latas", latas)
print("Galoes", galoes)
print("Custo", custo)
