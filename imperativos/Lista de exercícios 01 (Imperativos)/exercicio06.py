#Apresentar o valor de um produto da loja

vlr_produto= float(input('Qual é o valor do produto: R$'))

#dividir esse valor em conco prestações sem juros

vlr_dividido= vlr_produto / 5
print('Esse valor vai ficar dividido em cinco prestações de R$', format(vlr_dividido, '.2f'), 'sem juros')
