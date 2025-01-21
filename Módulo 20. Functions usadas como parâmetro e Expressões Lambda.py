#Vamos criar uma função que me permita calcular o valor acrescido do imposto de diferentes categorias (produto, serviço, royalties, etc.)
def calcular_imposto(imposto):
    return lambda preco: preco * (1 + imposto)
  
#- Agora vamos definir as funções que calculam o imposto das 3 categorias (produto, serviço, royalties)
calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.25)

#Agora vamos aplicar com um valor de nota fiscal de 100 para ver o resultado
print(int(calcular_preco_produto(100)))
print(int(calcular_preco_servico(100)))
print(calcular_preco_royalties(100))

#Usar lambda como argumento de alguma outra função, como map e filter
preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

#Queremos saber o preço de cada produto adicionando o valor do imposto de 30% sobre o valor do produto
def calcular_preco(preco):
    return preco * 1.3
  
#Fazendo por function
preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values()))
print(preco_com_imposto)

#fazendo por lambda
preco_com_imposto2 = list(map(lambda preco: preco * 1.3 , preco_tecnologia.values()))
print(preco_com_imposto2)

#filter()
#Queremos apenas os produtos que custam acima de 2000
#fazendo por function
def ehmaior2000(item):
    return item[1] > 2000

produtos_acima2000 = dict(list(filter(ehmaior2000, preco_tecnologia.items())))
print(produtos_acima2000)

#fazendo por lambda
produtos2_acima2000 = dict(list(filter(lambda item: item[1] > 2000 , preco_tecnologia.items())))
print(produtos2_acima2000)
