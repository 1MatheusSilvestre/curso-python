#Exercícios

##1. Criando um Registro de Hóspedes
#Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:
#1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
#2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
#3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa.
#seu código aqui
qtde_pessoas = int(input('Quantas pessoas terão no quarto?'))
quarto = []

for i in range(qtde_pessoas):
    nome = input('Qual o nome?')
    cpf = input('Qual o cpf?')
    hospede = [nome, 'cpf:{}'.format(cpf)]
    quarto.append(hospede)
    
print(quarto)

## 2. Análise de Vendas
#Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
#Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#seu código aqui
for item in vendas:
    if item[1] >= meta:
        print('Vendedor {} bateu a meta. Fez {} vendas'.format(item[0], item[1]))

## 3. Comparação com Ano Anterior
#Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.
#Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.
#Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)
#Dica: lembre do enumerate, ele pode facilitar seu "for"
produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
#seu código aqui

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print('{} vendeu R${:,} em 2019, R${:,} em 2020 e teve {:.1%} de crescimento'.format(produto, vendas2019[i], vendas2020[i], crescimento))

# Exercícios
##1. Calculando % de uma lista
#Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.
#Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.
#- Vamos resolver de 2 formas:
#1. Criando uma lista auxiliar apenas com os vendedores que bateram a meta
#2. Fazendo o cálculo diretamente na lista que já temos

acima_meta = []

for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)
        
print(acima_meta)
print('{:.1%} dos vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))
#----------------------------------------------------------------------------------
qtde_vendedores_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        qtde_vendedores_acima += 1
        
print('{:.1%} dos vendedores bateram a meta'.format(qtde_vendedores_acima / len(vendas)))

## Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?
melhor_vendedor = ''
maior_vendas = 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]
        
print('O melhor vendedor foi {} com {} vendas'.format(melhor_vendedor, maior_vendas))

#### 1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas. 
vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]

for i in range(len(vendas)):
    print(f"Vendedor: {vendedores[i]}, Vendas: {vendas[i]}")

media = sum(vendas)/len(vendas)

print('Média:', media)

#### 2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.
alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

medias = []
for i in range(len(notas)):
    media = sum(notas[i])/len(notas[i])
    medias.append(media)
    print(alunos[i], f"média: {media}")

contador = 0
for media in medias:
    if media >= 7:
        contador += 1
        
print(f'{contador} alunos tiveram nota maior ou igual a 7')

#### 3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funcionários com mais de 25 anos possuem salário inferior à média de todos os salários.
idades = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
salarios = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]

media = sum(salarios)/len(salarios)

contador = 0
for i, idade in enumerate(idades):
    if idade > 25 and salarios[i] < media:
        contador += 1

print(f'{contador} funcionários possuem mais de 25 anos e salário inferior à média.')

#### 4.Em quais meses a média de temperatura foi maior do que a média nacional?
meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]
media_nacional = sum(temperaturas)/len(temperaturas)

print('Média Nacional:', media_nacional)
for i, mes in enumerate(meses):
        if temperaturas[i] > media_nacional:
            print(f"{mes}: {temperaturas[i]} graus")

#### 5. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
#Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
lista_salarios = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
abonos = []
print('Salario - Abono')

conta_minimo = 0
for salario in lista_salarios:
    abono = salario * 0.2
    if abono < 100:
        abono = 100
    abonos.append(abono)
    if abono == 100:
        conta_minimo += 1
    print(f'R$ {salario} - R$ {abono}')
    
qtde = len(lista_salarios)
total = sum(abonos)
maximo = max(abonos)

print('Foram processados', qtde, 'colaboradores')
print(f'Total gasto com abonos: R$ {total:.2f}')
print('Valor mínimo pago a', conta_minimo, 'colaboradores')
print(f'Maior valor de abono pago: R$ {maximo:.2f}')

#### 6. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
#Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#a. O modelo do carro mais econômico;
#b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará,
#considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
#Os dados são fictícios e podem mudar a cada execução do programa.
#Comparativo de Consumo de Combustível
#Veículo 1
#Nome: fusca
#Km por litro: 7
#Veículo 2
#Nome: gol
#Km por litro: 10
#Veículo 3
#Nome: uno
#Km por litro: 12.5
#Veículo 4
#Nome: Vectra
#Km por litro: 9
#Veículo 5
#Nome: Peugeout
#Km por litro: 14.5
#Relatório Final
 #1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 #2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 #3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 #4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 #5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
#O menor consumo é do peugeout.
print('Comparativo de Consumo de Combustível')
veiculos = ['fusca',' gol', 'uno', 'vectra', 'peugeot']
autonomias = [7, 10, 12.5, 9, 14.5]
    
print('Relatório Final')
for i, autonomia in enumerate(autonomias):
    print(f' {i+1} - {veiculos[i]} - {autonomia:.1f} - {1000/autonomia:.2f} - R$ {1000/autonomia* 2.25:.2f}')
    
maior = max(autonomias)
i = autonomias.index(maior)
print('O menor consumo é do', veiculos[i])

#### 7. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe \\$200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
#Por exemplo, um vendedor que teve vendas brutas de \\$3000 em uma semana recebe \\$200 mais 9 por cento de \\$3000, ou seja, um total de \\$470. 
#Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante

vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]
faixas = []
menores_que_mil = 0
tamanho_faixas = 100
qtde_faixas = 9

for venda in vendas:
    bonus = venda * 0.09
    salario = 200 + bonus
    print(salario)
    faixa = int(bonus / tamanho_faixas) + 1
    faixas.append(faixa)
    
for i in range(qtde_faixas-1):
    print(f'Entre {i*100 + 200} e {i*100 + 299}:', faixas.count(i+1))
    menores_que_mil += faixas.count(i+1)
    
print('Mais que mil:', len(vendas) - menores_que_mil)
