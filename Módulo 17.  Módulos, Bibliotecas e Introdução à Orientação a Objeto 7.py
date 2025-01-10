#Contagem regressiva - Um evento especial está programado para começar em 10 segundos. Crie uma contagem regressiva que começa em 10 e vai até 0, com uma pausa de um segundo entre cada número.
import time

for numero in range(10, 0, -1):
    time.sleep(1)

print (numero, end = '...\t')

#Formatação de tempo - Uma empresa quer exibir a data e a hora atual em seu site no formato "Dia da semana, dia do mês de mês de ano, horas:minutos". Crie um script Python que mostra a data e a hora atuais neste formato.
import locale
import time

# Definir a localização para português.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime('%A, %d de %B de %Y, %H:%M', tempo_em_struct)

print(f'Data e hora atuais: {tempo_formatado}')

#Tempo até o próximo ano - Crie um script Python que calcula quantos dias, horas, minutos e segundos faltam até o próximo Ano Novo.
import time

agora = time.localtime()
proximo_ano = (agora.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)

segundos_restantes = int(time.mktime(proximo_ano) - time.mktime(agora))

dias, resto_segundos = divmod(segundos_restantes, segundos_por_dia)
horas, resto_segundos = divmod(resto_segundos, segundos_por_hora)
minutos, segundos = divmod(resto_segundos, segundos_por_minuto)

print(f'Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para o próximo Ano Novo.') 

## Oferecendo desconto para cliente com base na última compra
#Suponha que você está trabalhando para uma empresa que deseja rastrear a atividade do cliente. 
#Uma métrica que eles estão interessados é o tempo que passou desde a última transação do cliente. Se for muito tempo, eles podem oferecer um desconto para o cliente. 
#Crie um script Python que mostra quanto tempo se passou desde a última compra do cliente. Se faz mais de 30 dias, mostre uma mensagem oferecendo um desconto para o cliente.
from datetime import datetime

ultima_compra = datetime(2023, 5, 10)
data_atual = datetime.now()
diferenca_dias = data_atual - ultima_compra

if diferenca_dias.days > 30:
    print('Você recebeu um desconto especial! Apareça em nossa loja!')

##Data e hora em diferentes fusos horários
#Uma empresa tem escritórios em São Paulo, Nova York e Tóquio. Crie um script Python que mostra a data e hora atuais nesses três fusos horários. Exiba, também, se estes escritórios estão abertos ou fechados (9h às 17h).
from datetime import datetime
import pytz

escritorios = []
data_hora_atual = datetime.now(pytz.utc)

data_hora_sp = pytz.timezone('America/Sao_Paulo')
escritorios.append(('São Paulo', data_hora_sp))
data_hora_ny = pytz.timezone('America/New_York')
escritorios.append(('Nova Iorque', data_hora_ny))
data_hora_toquio = pytz.timezone('Asia/Tokyo')
escritorios.append(('Tóquio', data_hora_toquio))

for escritorio in escritorios:
    data_hora_local = data_hora_atual.astimezone(escritorio[1])
    if 9 <= data_hora_local.hour < 17:
        print (f'O escritorio de {escritorio[0]} está aberto!')
    else:
        print(f'O escritório de {escritorio[0]} está fechado!')

#Calculando a Idade
#Um usuário fornece sua data de nascimento no formato 'dd/mm/aaaa'. Crie um script em Python que calcula a idade do usuário.
from datetime import datetime

nascimento_user = input('digite sua data de nascimento (dd/mm/aaaa):  ')
nascimento_user = datetime.strptime(nascimento_user, '%d/%m/%Y')

data_atual = datatime.now()
mes_atual = datatime.month
ano_atual = datatime.year
idade = data_atual.year - nascimento_user.year

mes_nasc = nascimento_user.month
dia_nasc = nascimento_user.day

if mes_atual >= mes_nasc:
    idade -= 1
    print(idade)
elif mes_atual == mes_nasc < idade:
    idade -= 1
    print(idade)

print(f'Você tem: {idade} anos.')
