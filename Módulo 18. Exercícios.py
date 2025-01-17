#1- Imposto a pagar no Lucro Presumido
#5% sobre faturamento de ISS (mensal)
#0,65% de PIS sobre faturamento, (mensal)
#3% de COFINS sobre faturmaneto, (mensal)
#4.8% de IR (trimestral)
#10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
#CSLL: 2,88% sobre faturamento (trimestral)
faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# você precisa inserir no sistema um dicionário no formato:

# resultado = {
#     'mes': (faturamento, imposto_mensal, imposto_trimestral),
# }

#cada mês
    #transformar fat de string para int
    #calcular imposto men e tri,
    #add fat, imposto men e tri no dict resultado

def transformar_numero(numero):
    #utilizar funçaõ replace para alterar os valores
    numero = numero.replace('R$', '')
    numero = numero.replace('.', '')
    numero = numero.replace(',', '.')
    valor = float(numero)
    return valor


def calcular_mensal(valor_fat):
    iss = valor_fat * 0.05
    pis = valor_fat * 0.065
    cofins = valor_fat * 0.03
    imposto_mensal = iss + pis + cofins
    return imposto_mensal


def calcular_tri(valor_fat):
    ir = valor_fat * 0.048
    ir_adicional = 0
    if valor_fat > 20000:
        ir_adicional = (valor_fat - 20000) * 0.1
    csll = valor_fat * 0.028
    imposto_tri = ir + ir_adicional + csll
    return imposto_tri

resultado = {}

for mes in faturamento:
    valor_fat = transformar_numero(faturamento[mes])
    imposto_mensal = calcular_mensal(valor_fat)
    imposto_tri = calcular_tri(valor_fat)
    #add no dicionário vai passar no mês do for e adicionar como valor a tupla contendo os valores de fat
    resultado[mes] = (valor_fat, imposto_mensal, imposto_tri)

print(resultado)


# puxando informações SQL de um banco de dados
informacoes = [(1, 'NATHANIEL FORD', 'GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY', 167411.18, 0.0, 400184.25, None, 567595.43, 567595.43, 2011, '', 'San Francisco', ''), (2, 'GARY JIMENEZ', 'CAPTAIN III (POLICE DEPARTMENT)', 155966.02, 245131.88, 137811.38, None, 538909.28, 538909.28, 2011, '', 'San Francisco', ''), (3, 'ALBERT PARDINI', 'CAPTAIN III (POLICE DEPARTMENT)', 212739.13, 106088.18, 16452.6, None, 335279.91, 335279.91, 2011, '', 'San Francisco', ''), (4, 'CHRISTOPHER CHONG', 'WIRE ROPE CABLE MAINTENANCE MECHANIC', 77916.0, 56120.71, 198306.9, None, 332343.61, 332343.61, 2011, '', 'San Francisco', ''), (5, 'PATRICK GARDNER', 'DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)', 134401.6, 9737.0, 182234.59, None, 326373.19, 326373.19, 2011, '', 'San Francisco', ''), (6, 'DAVID SULLIVAN', 'ASSISTANT DEPUTY CHIEF II', 118602.0, 8601.0, 189082.74, None, 316285.74, 316285.74, 2011, '', 'San Francisco', ''), (7, 'ALSON LEE', 'BATTALION CHIEF, (FIRE DEPARTMENT)', 92492.01, 89062.9, 134426.14, None, 315981.05, 315981.05, 2011, '', 'San Francisco', ''), (8, 'DAVID KUSHNER', 'DEPUTY DIRECTOR OF INVESTMENTS', 256576.96, 0.0, 51322.5, None, 307899.46, 307899.46, 2011, '', 'San Francisco', ''), (9, 'MICHAEL MORRIS', 'BATTALION CHIEF, (FIRE DEPARTMENT)', 176932.64, 86362.68, 40132.23, None, 303427.55, 303427.55, 2011, '', 'San Francisco', ''), (10, 'JOANNE HAYES-WHITE', 'CHIEF OF DEPARTMENT, (FIRE DEPARTMENT)', 285262.0, 0.0, 17115.73, None, 302377.73, 302377.73, 2011, '', 'San Francisco', '')]
descricao = (('Id', "<class 'int'>", None, 10, 10, 0, True), ('EmployeeName', "<class 'str'>", None, 65536, 65536, 0, True), ('JobTitle', "<class 'str'>", None, 65536, 65536, 0, True), ('BasePay', "<class 'float'>", None, 54, 54, 0, True), ('OvertimePay', "<class 'float'>", None, 54, 54, 0, True), ('OtherPay', "<class 'float'>", None, 54, 54, 0, True), ('Benefits', "<class 'float'>", None, 54, 54, 0, True), ('TotalPay', "<class 'float'>", None, 54, 54, 0, True), ('TotalPayBenefits', "<class 'float'>", None, 54, 54, 0, True), ('Year', "<class 'int'>", None, 10, 10, 0, True), ('Notes', "<class 'str'>", None, 65536, 65536, 0, True), ('Agency', "<class 'str'>", None, 65536, 65536, 0, True), ('Status', "<class 'str'>", None, 65536, 65536, 0, True))

# precisamos 1º de uma lista com o nome das colunas para poder organizar as colunas da nossa tabela:
# o nome das colunas está na variável descrição, dê uma olhada.

import pandas as pd

colunas = (tupla[0] for tupla in descricao)

# tabela = pd.DataFrame.from_records(informacoes)
# para acertar nossa tabela, vamos precisar fazer:
tabela = pd.DataFrame.from_records(informacoes, columns = colunas) # onde colunas é uma lista com o nome das colunas
display(tabela)


# além disso, precisamos enviar por e-mail para o RH uma lista com o nome e o cargo de cada pessoa da tabela
# então você precisa construir o texto do corpo desse email do tipo:

# texto = """
# RH, segue a lista dos funcionários:
# Fulano, Cargo: tal
# Beltrano, Cargo: isso
# """

texto = 'RH, segue a lista dos funcionários:\n'

for item in informacoes:
    nome = item[1]
    cargo = item[2]
    texto += f'{nome}, Cargo: {cargo}\n'

print(texto)


# para pegar o dicionario do vimeo, use:
from dic import dicionario_vimeo

import pprint

informacoes = dicionario_vimeo["data"]
videos = []
for item in informacoes:
    video_uri = item["uri"]
    nome = item["name"]
    duracao = item["duration"]


    link_540p = ""
    link_720p = ""
    link_1080p = ""
    lista_downloads = item["download"]
    for dicionario_download in lista_downloads:
        if dicionario_download["rendition"] == "540p":
            link_540p = dicionario_download["link"]
        if dicionario_download["rendition"] == "720p":
            link_720p = dicionario_download["link"]
        if dicionario_download["rendition"] == "1080p":
            link_1080p = dicionario_download["link"]
    
    dic_item = {'uri': video_uri, 'nome': nome, 'duracao': duracao, 'link540p': link_540p, 'link720p': link_720p, 'link1080p': link_1080p}
    videos.append(dic_item)
pprint.pprint(videos)

# você precisa chegar em:
# videos = [
#     {'uri': video_uri, 'nome': nome_video, 'duracao': duracao, 'link540p': link540p, 'link720p': link720p, 'link1080p': link1080p},
