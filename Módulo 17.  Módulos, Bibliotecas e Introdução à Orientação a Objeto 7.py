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
