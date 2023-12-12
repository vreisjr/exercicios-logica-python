#Entrar com uma variável denominada salário bruto

sal_bruto= float(input('Informe o valor do Salário Bruto: R$'))

#Após o recebimento do salario bruto, calcule o valor do imposto de renda, o do INSS e o salário líquido

vlr_ir= sal_bruto * (5 / 100)
vlr_inss= sal_bruto * (11 / 100)
sal_liquido= sal_bruto - (vlr_ir + vlr_inss)

print('O Valor do Imposto de renda é de: R$', vlr_ir, ', o valor do INSS é de: R$', vlr_inss, ', logo, o salário liquido é de: R$', sal_liquido)
