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
