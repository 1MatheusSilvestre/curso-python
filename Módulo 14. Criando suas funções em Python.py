## 1. Function para Cálculo de Carga Tributária
#(Lembrando, não se atente ao funcionamento real da carga tributária, é apenas um exemplo imaginário para treinarmos as functions com algo mais prático)
#Imagine que você trabalha no setor contábil de uma grande empresa de Varejo. 
#Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.
def carga_tributaria(preco, custo, lucro): 
    lucro_real = preco - custo 
    diferenca = lucro_real - lucro
    porcentagem = diferenca / preco
    return porcentagem 

print('a porcegentem de imposto foi de {}%'.format(carga_tributaria(1500, 400, 800)))
