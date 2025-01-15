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
