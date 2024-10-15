# Exercícios
# 1. Input até o usuário parar
#Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.
#O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.
#Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.
#Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha.
#Sugestão para sua lista de produtos vendidos:
vendas = []
while True:
    prod = input("Digite um Produto")
    if not prod:
        break
    qntd = int(input("Digite uma quantidade"))
    vendas.append([prod, qntd])
print(vendas)

#### 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = float(input("Digite uma nota de 0 a 10"))
while not(0 <= nota <= 10):
    print("nota inválida")
    nota = float(input("Digite uma nota de 0 a 10"))

#### 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
login = input("digite seu login")
senha = input("digite sua senha")
while login == senha:
    print ("Não é aceito a senha igual ao nome de usuário")
    login = input("digite seu login")
    senha = input("digite sua senha")

#### 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
##### Nome: maior que 3 caracteres;
##### Idade: entre 0 e 150;
##### Salário: maior que zero;
##### Sexo: 'f' ou 'm';
##### Estado Civil: 's', 'c', 'v', 'd';
nome = input("Digite seu nome:")
while len(nome) < 4:
    print("insira um nome maior que 3 caracteres")
    nome = input("Digite seu nome:")

idade = int(input("Digite sua idade:"))
while not (0 <= idade <= 150):
    print("A sua idade deve ter entre 0 a 150")
    idade = int(input("Digite sua idade:"))

salario = float(input("Digite seu salário:")) 
while salario <= 0:
    print("O seu salário deve ser maior que 0")
    salario = float(input("Digite seu salário:"))

sexo = input("Digite seu sexo, f = Feminino ou m = Masculino:")
while not sexo in ['f', 'm']:
    print("Insira um gênero válido")
    sexo = input("Digite seu sexo, f = Feminino ou m = Masculino:")
    
EC = input("Digite seu Estado Civil 's', 'c', 'v' ou 'd' :")
while not EC in ['s', 'c', 'v', 'd']:
    print('Insira um estado civil válido')
    EC = input("Digite seu Estado Civil 's', 'c', 'v' ou 'd' :")

#### 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
#com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
#ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
paisA = 80000
paisB = 200000
tempo = 0
while paisA <= paisB:
    paisA *= 1.03
    paisB *= 1.015
    tempo += 1
print("Foram necessários {} anoss para que o País A ultrapassasse o País B".format(tempo))

#### 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
repete = 's'
while repete == 's':
    populacao_A = int(input('Informe a população A: '))
    populacao_B = int(input('Informe a população B: '))
    while populacao_A <= 0 or populacao_B <= 0:
        print('As populações precisam ser maiores que zero')
        populacao_A = int(input('Informe a população A: '))
        populacao_B = int(input('Informe a população B: '))
    taxa_A = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
    taxa_B = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
    while taxa_A <= 0 or taxa_B <= 0:
        print('As taxas precisam ser maiores que zero')
        taxa_A = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
        taxa_B = float(input('Informe a taxa de crescimento da população A em porcentagem (exemplo: entre 3 para 3%): '))
    taxa_A = taxa_A / 100 + 1
    taxa_B = taxa_B / 100 + 1
    tempo = 0
    while populacao_A < populacao_B:
        populacao_A *= taxa_A
        populacao_B *= taxa_B
        tempo += 1
    print('São necessários', tempo, 'anos para a população A igualar ou superar a população B')
    repete = input('Deseja repetir a operação? Tecle "s" para sim, qualquer outra tecla para não.')

#### 6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento
for i in range (5):
    fat = int(input("Informe o Faturamento"))
    if i == 0:
        maior = fat
    else:
        if fat > maior:
            maior = fat
print(maior, "foi o maior faturamento." )
#### 8. Faça um programa que consiga categorizar a idade das equipes de uma empresa. 
#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da equipe varia entre 0 e 25 (jovem) ,
#26 e 60 (sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.
n = int(input("Informe quantas pessoas serão"))
total = 0
for i in range(n):
    idade = int(input(f"Por gentileza, informe a {i+1}ª idade:"))
    total += idade
media = total/n
if 0 <= media <= 25:
    print("A idade média da equipe é {}, e ela é jovem".format(media))
if 25 < media <= 60:
    print("A idade média da equipe é {}, e ela é sênior".format(media))
if media > 60:
     print("A idade média da equipe é {}, e ela é idosa".format(media))  
#### 9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
qtde = int(input(f"Informe a quantidade de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
for i in range(qtde):
    candidato = int(input(f"Informe o voto do primeiro eleitor {i+1}. O eleitor pode votar nos candidatos 1, 2 ou 3: "))
    if candidato == 1:
        candidato1 += 1
    elif candidato == 2:
        candidato2 += 1
    elif candidato == 3:
        candidato3 += 1      
print("Votos do candidato 1:", candidato1)
print("Votos do candidato 2:", candidato2)
print("Votos do candidato 3:", candidato3)
#### 10. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.
qtde = int(input(f"Informe a quatidade de CDs: "))
total = 0
for i in range(qtde):
    valor = int(input(f"Informe o preço do {i+1}º CD: "))
    total += valor
print(f"A média é de R$ {total/qtde} por CD")
#### 11. O Sr. Manoel Joaquim possui uma grande loja de artigos de R\\$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
#Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50
print("Lojas Quase Dois - Tabela de preços")
for i in range(50):
    print(f"{i+1} - R$ {(i+1)*1.99:.2f}")

#### 12. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
#Faça um programa que determine o salário desse funcionário em 2003. 
salario = 1000 * 1.015
porcentagem = 0.015
for i in range(1997, 2004):
    porcentagem *= 2
    salario *= (1 + porcentagem)
print("O salário em 2003 era R$ {:.2f}".format(salario))

#### 13. O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o 
#total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
total = 0
codigo = input('Informe o código do produto, caso deseje encerrar digite "encerrar": ')
while codigo != 'encerrar':
    qtde = int(input('Informe a quantidade: '))
    if codigo == '100':
        total += 1.2 * qtde
    elif codigo == '101':
        total += 1.3 * qtde
    elif codigo == '102':
        total += 1.5 * qtde
    elif codigo == '103':
        total += 1.2 * qtde
    elif codigo == '104':
        total += 1.3 * qtde
    elif codigo == '105':
        total += 1 * qtde   
    codigo = input('Informe o código do produto, caso deseje encerrar digite "encerrar": ')
print('O total a ser pago é: R$ ', total)
