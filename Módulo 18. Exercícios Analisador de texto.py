#Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras (independentemente se há repetição ou não), a quantidade de cada palavra e a quantidade de cada letra. 
#Ignore maiúsculas e minúsculas ao contar letras (ou seja, transforme tudo para minúsculas). Faça o devido tratamento para pontuação e espaços ao contar palavras.  
#O programa deve conter uma função chamada analisar_texto que recebe o texto como parâmetro e retorna a contagem de palavras, a frequência de palavras e a frequência de letras. A função deve ser devidamente documentada.

#Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve imprimir:

#Contagem de palavras: 8
#Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
#Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2, 'd': 1, 'é': 1, 'v': 1, 'a': 1})
#Dica: use o módulo string para obter uma lista de caracteres de pontuação. Exemplo:

#import string
#print(string.punctuation)
#Dica: use o módulo collections para obter um contador de palavras e letras. Exemplo:

#from collections import Counter
#print(Counter(['a', 'b', 'a', 'c', 'b', 'a']))
#print(Counter('abacba'))

def analisar_texto(texto):
    """
    Analisa um texto fornecido e retorna a contagem de palavras, a frequência de palavras e a frequência de letras.

    Parameters
    ---------
    texto : str
        O texto a ser analisado.

    Returns
    --------
    Tuple
        uma tupla contendo a contagem de palavras, a frequência de palavras e a frequência de letras.
    """
    #remove a pontuação
    tratamento = str.maketrans('', '', string.punctuation)
    #aplica o metódo anterior para deixar sem pontuação
    texto_tratado = texto.translate(tratamento)
    #divide em palavras, criando uma lista de palavras 
    palavras = texto_tratado.split()
    #conta o total de palavras 
    contagem = len(palavras)
    #cria um contador de cada palavra
    frequencia_palavras = Counter(palavras)
    #cria um contador de cada letra  e deixa tudo minusculo 
    frequencia_letras = Counter(texto_tratado.lower())

    return contagem, frequencia_palavras, frequencia_letras


texto = "Olá mundo! Este é um teste. Olá novamente."
contagem, frequencia_palavras, frequencia_letras = analisar_texto(texto)

print(f"Contagem de palavras: {contagem}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")
