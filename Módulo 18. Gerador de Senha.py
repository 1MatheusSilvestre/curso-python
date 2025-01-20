def gerar_senha(tamanho):
    #caso seja menor que 4 digítos
    if tamanho < 4:
        print("O comprimento da senha deve ser maior que 4")
    else:
        senha = [
            #letra
            random.choice(string.ascii_letters),
            #digito
            random.choice(string.digits),
            #caracter especial 
            random.choice(string.punctuation)
        ]

        #juntando todas as possibilidades
        possibilidades = "".join([string.ascii_letters + string.digits + string.punctuation])

        #extendendo a lista e escolhendo mais de um elemento de possibilidades, -3 pois já tem na senha 
        senha.extend(random.choices(possibilidades, k = tamanho - 3))
        #embaralhar os carecteres 
        random.shuffle(senha)

        #junta os carecteres 
        return "".join(senha)

tamanho = int(input("Digite o comprimento da senha: "))
print(gerar_senha(tamanho))
