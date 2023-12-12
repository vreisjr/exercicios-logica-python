#Apresentar um valor em Dólar, e o valor de cotação atual

vlr_dolar= float(input('Digite um valor em Dólar: U$'))
vlr_cot= float(input('Digite o valor da cotação atual do Dólar: R$'))

#Converter para Real

cov_real= vlr_dolar * vlr_cot

print('O valor em Real é: R$', format(cov_real, '.2f'))
