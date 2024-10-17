## 1. Identificando Locais de Risco
#(Não conhecemos muito dos números e indicadores reais, esse é um exercício imaginário para treinarmos com um cenário mais prático)\n",
#"Digamos que você está construindo um programa para identificar níveis de CO2 (gás carbônico) em determinados locais para evitar potenciais acidentes. Em cada um desses locais a sua empresa tem 5 sensores que captam o nível de CO2 do local.\n",
#"Os níveis normais de CO2 são em média 350. O nível de CO2 de um local é dado pela média captada pelos 5 sensores.\n",
#Isso significa que se tivermos os 5 sensores do Rio de Janeiro marcando: 350, 400, 450, 350, 300, o nível de CO2 do Rio de Janeiro será dado por: (350 + 400 + 450 + 350 + 300) / 5 = 370.\n",
#Caso o nível seja maior do que 450, um aviso deve ser exibido pelo seu programa dizendo, por exemplo: Rio de Janeiro está com níveis altíssimos de CO2 (490), chamar equipe especializada para verificar a região.\n",
#Os resultados dos sensores são monitorados frequentemente e são dados para o sistema em forma de dicionário:"

niveis_co2 = {
    'AC': [325,405,429,486,402],
    'AL': [492,495,310,407,388],
    'AP': [507,503,368,338,400],
    'AM': [429,456,352,377,363],
    'BA': [321,508,372,490,412],
    'CE': [424,328,425,516,480],
    'ES': [449,506,461,337,336],
    'GO': [425,460,385,485,460],
    'MA': [361,310,344,425,490],
    'MT': [358,402,425,386,379],
    'MS': [324,357,441,405,427],
    'MG': [345,367,391,427,516],
    'PA': [479,514,392,493,329],
    'PB': [418,499,317,302,476],
    'PR': [420,508,419,396,327],
    'PE': [404,444,495,320,343],
    'PI': [513,513,304,377,475],
    'RJ': [502,481,492,502,506],
    'RN': [446,437,519,356,317],
    'RS': [427,518,459,317,321],
    'RO': [517,466,512,326,458],
    'RR': [466,495,469,495,310],
    'SC': [495,436,382,483,479],
    'SP': [495,407,362,389,317],
    'SE': [508,351,334,389,418],
    'TO': [339,490,304,488,419],
    'DF': [376,516,320,310,518],
    }

for item in (niveis_co2):
    qtde_co2 = len(niveis_co2[item])
    soma_co2 = sum(niveis_co2[item])
    media = soma_co2 / 5
    if media  > 450:
        print('{} está com níveis altíssimos de CO2 ({}), chamar equipe especializada para verificar a região'.format(item, media))
    else:
        print('{} está na média'.format(item))

## 1. Exercício \"menos prático\" para treinar manipulação de dicionário\n",
#Dessa vez, vamos apenas treinar a manipulação de dicionário. Transforme as listas abaixo em 1 único dicionário no formato:
#produto: [vendas2019, vendas2020]
#produto2: [vendas2019, vendas2020]
#produto3: [vendas2019, vendas2020]
produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

lista = list(zip(vendas2019, vendas2020))
dicionario = dict(zip(produtos, lista))
print(dicionario)

# Exercício 1
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}
produto = input('Informe um produto:')

if produto in precos:
    preco = precos[produto]
    print('produto {}: R$ {}'.format(produto, preco))
else:
    print('produto não existe, por favor tente novamente')

# Exercício 2
# Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
# Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
# Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

produto = input('Informe um produto:')
if produto in precos:
    preco = precos[produto]
    print('produto {}: R$ {}'.format(produto, preco))
else:
    cadastro = input('produto não existe, quer registra-lo? s/n: ')
    if 's' in cadastro:
        produto_lista = produto
        valor = input('Informe o preço do produto:')
        precos.update({produto_lista: valor})
        print('Cadastro bem sucedido, agora a nossa lista está assim: {}'.format(precos))
    else:
        print('Produto não existe, por favor tente novamente')
# Exercício 3
# Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos. 
# calcule o novo valor dos produtos com base nas seguintes regras:
# Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
# Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
# Preços acima de 2.000 vão ter reajuste de 20%
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
precos_atual = {}

for produto in precos:
    preco_produto = precos[produto]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    print(f"Produto {produto}, Novo Preço: R${novo_preco}")
    precos_atual[produto] = novo_preco
# Exercício 4
# Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços
# Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final
for produto in precos:
    preco_produto = precos[produto]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    print(f"Produto {produto}, Novo Preço: R${novo_preco}")
    precos_atual[produto] = novo_preco
total_antigo = sum(precos.values())
total_novo = sum(precos_atual.values())
reajuste = total_novo - total_antigo
print(f"O reajuste total foi de R${reajuste}")

# Exercício 5
# Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
# Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
# Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022
vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    percentual = valor_23 / valor_22 - 1
    print(f"Em {mes}, a variação percentual foi de: {percentual:.1%}")

total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())
crescimento = total_23 / total_22 - 1
print(f"Crescimento Real: {crescimento:.1%}")

