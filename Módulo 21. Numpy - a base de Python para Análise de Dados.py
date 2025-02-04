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

#Exercício
#Você é um analista de RH e tem os salários de todos os funcionários da sua empresa em um array NumPy. 
#Seu trabalho é identificar quantos funcionários ganham acima da média. Use o seguinte array para sua análise: salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800]).
salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])

media = np.mean(salarios)
#print(media)

acima_media = np.where(salarios[salarios > media])

print(f'Existem {len(salarios[salarios > media])} funcionários que ganham acima da média. Sendo a média: R$ {media:.1f} e seus respectivos salários: {acima_media}')
