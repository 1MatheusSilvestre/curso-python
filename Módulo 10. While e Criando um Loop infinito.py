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

while salario > 0:
    print("O seu salário deve ser maior que 0")
    salario = float(input("Digite seu salário:"))

sexo = input("Digite seu sexo, F = Feminino ou M = Masculino:")

while not sexo in "f" or "m":
    print("Insira um gênero válido")
    sexo = input("Digite seu sexo, F = Feminino ou M = Masculino:")

EC = input("Digite seu Estado Civil 's', 'c', 'v' ou 'd' :")

while not EC in ["s", "c", "v", "d"]:
    print('Insira um estado civil válido')
    EC = input("Digite seu Estado Civil 's', 'c', 'v' ou 'd' :")
