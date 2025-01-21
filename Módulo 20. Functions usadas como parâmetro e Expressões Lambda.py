#Exemplo: digamos que eu tenha uma function que corrige um código de um produto (semelhante ao que fizemos na seção de function aqui do curso)
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

#Agora queremos padronizar uma lista de códigos:
produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']

#Usando o for, temos que percorrer a lista toda e para cada item executar a function
for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
print(produtos)

#Usando o map, apenas chamamos a função e ela já faz isso para a gente
produtos = list(map(padronizar_texto, produtos))
print(produtos)

-----------------------------------------------------

#Como ordenar um dicionário de acordo com o valor
vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

#Queremos listar da maior quantidade de vendas para a menor, para enviar como report para o diretor, por exemplo
def segundo_item(tupla):
    return tupla[1]
lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(dict(lista_vendas))

-----------------------------------------------------

#Exemplo mais simples de Lambda
def minha_funcao(num):
    return num * 2
print(minha_funcao(5))

minha_funcao2 = lambda num: num * 2
print(minha_funcao2(5))

#Exemplo útil: Vamos usar lambda expressions para criar uma função que calcula o preço dos produtos acrescido do imposto
imposto = 0.3
def preco_imposto(preco):
    return preco * (1 + 0.3)

preco_imposto2 = lambda preco: preco * (1.0 + imposto)

print(preco_imposto2(100))

-----------------------------------------------------

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

-----------------------------------------------------

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
