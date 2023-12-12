#digitar o preço do produto e do percentual de acrécimo

prec_prod= float(input('Digite o preço do produto: R$'))
acrc_perc= float(input('Digite o acrécimo perncentual para o preço do produto: %'))

#Calcular o valor percentual

vlr_perc= (acrc_perc / 100) * prec_prod

print('O valor de venda do produto é de R$', format(vlr_perc + prec_prod, '.2f'))
