sal_base= float(input('Informe o salário Base: R$'))
vant= float(input('Informe o total de Vantagens: R$'))
desc= float(input('Informe o total dos descontos: R$'))
#processamento
sal_liq= (sal_base + vant)- desc
#saída
print('O salário liquido calculado foi: R$', sal_liq)
