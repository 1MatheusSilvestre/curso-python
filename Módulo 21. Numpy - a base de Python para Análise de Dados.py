#Exercícios Arrays:
#Exercício 1
#Você é um gerente de vendas e tem os dados de vendas de um produto para os últimos 7 dias em uma lista: [127, 90, 201, 150, 210, 220, 115]. Calcule a média de vendas durante a semana.
import numpy as np

dados = [127, 90, 201, 150, 210, 220, 115]

media_semana = np.mean(dados)
print(media_semana)

#Exercício 2
#Você é um analista financeiro e tem os preços de fechamento diário de uma ação para a última semana em um array NumPy: precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50]). Calcule o preço máximo, mínimo e a variação de preço durante a semana.
precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])

preco_max = np.max(precos)
preco_min = np.min(precos)
variacao_semana = preco_max - preco_min

print(preco_max)
print(preco_min)
print(f'{variacao_semana :.2}')

#Exercício 3
#Sua loja vendeu em um dia 5 unidades do Produto A, 3 unidades do Produto B e 2 unidades do Produto C. Os preços dos produtos são, respectivamente, 100, 200 e 50 reais. Calcule o total de vendas do dia.
quantidades = np.array([5, 3, 2])
precos = np.array([100, 200, 50])

print(np.dot(quantidades, precos))

#Exercício 4
#Você é um analista de RH e tem os salários de todos os funcionários da sua empresa em um array NumPy. 
#Seu trabalho é identificar quantos funcionários ganham acima da média. Use o seguinte array para sua análise: salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800]).
salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])

media = np.mean(salarios)
#print(media)

acima_media = np.where(salarios[salarios > media])

print(f'Existem {len(salarios[salarios > media])} funcionários que ganham acima da média. Sendo a média: R$ {media:.1f} e seus respectivos salários: {acima_media}')

#Exercício 5 
#Você é um engenheiro de produção e tem os tempos de ciclo (em minutos) de uma linha de produção em um array NumPy. Seu trabalho é identificar quaisquer tempos de ciclo que estão dois desvios padrão acima ou abaixo da média. 
#Use o seguinte array para sua análise: tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8]).

tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])
media = np.mean(tempos_ciclo) 

desvio_padrao = np.std(tempos_ciclo) 

limite_superior = media + 2 * desvio_padrao
limite_inferior = media - 2 * desvio_padrao

anomalias = [x for x in tempos_ciclo if (x > limite_superior or x < limite_inferior)]

print(anomalias)

#Exercicio 6
#Você é um gerente de vendas e tem os dados de vendas de três produtos diferentes (Produto A, Produto B, Produto C) para os últimos 5 dias em um array 2D NumPy. Cada linha do array representa um produto e cada coluna representa um dia. 
#Seu trabalho é calcular as vendas totais para cada produto e para cada dia.
#Use o seguinte array para sua análise:

vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])

produtoA = np.sum(vendas[0])
produtoB = np.sum(vendas[1])
produtoC = np.sum(vendas[2])

vendas_dia = np.sum(vendas, axis=0)

for i in range(5):
    print(f'Vendas do dia {i+1}: {vendas_dia[i]}')

print(f'Vendas do produto A: {produtoA}')
print(f'Vendas do produto B: {produtoB}')
print(f'Vendas do produto C: {produtoC}')
