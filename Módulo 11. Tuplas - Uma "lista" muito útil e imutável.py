### Exemplo:
#Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.
#Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

#- Qual foi o faturamento de IPhone no dia 20/08/2020?
faturamento = 0
for item in vendas:   
    data, produto, cor, memoria, unidade, valor = item
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidade * valor    
print('O faturamento de Iphone X foi de: R$ {}'.format(faturamento))

#- Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?
produto_mais_vendido = ''
qnt_mais_vendida = 0
for item in vendas:   
    data, produto, cor, memoria, unidade, valor = item
    if data == '21/08/2020':
        if unidade > qnt_mais_vendida:
            produto_mais_vendido = produto
            qnt_mais_vendida = unidade
print('produto mais vendido em 21/08/2020 foi o {} com um total de unidades de {}'.format(produto_mais_vendido, qnt_mais_vendida))

# Exercícios
#São exercícios bem parecidos com os que fizemos com listas. Mas na tupla, podemos não só trabalhar com índices, mas fazer o "unpacking" das tuplas, o que pode facilitar nossos códigos.
## 1. Análise de Vendas
#Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
#Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]
for nome, unidades in vendas:
    if unidades >= meta: 
        print('O vendedore {} bateu a meta, com um total de {} unidades.'.format(nome, unidades))

## 2. Comparação com Ano Anterior
#Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.
#Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.
#Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)
#A lógica da tupla é: (produto, vendas2019, vendas2020)

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]
crescimento = 0
for produto, vendas2019, vendas2020 in vendas_produtos:
    if vendas2020 > vendas2019:
        crescimento = vendas2020 / vendas2019 - 1
        print('O produto {} vendeu em 2019: {} e em 2020: {}, tendo um crescimento de: {:.1%}'.format(produto, vendas2019, vendas2020, crescimento))
