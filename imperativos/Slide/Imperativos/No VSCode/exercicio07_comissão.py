#Digite o salário fixo do vendedor, e o total de vendas efetuadas no mês (em R$)

sal_fixo= float(input('Digite o salário fixo do vendedor: R$'))
vend_mes= float(input('Digite o quanto ele vendeu no mês: R$'))

#calcular 15% em cima das vendas do mês, e somar ao salário fixo

comis= vend_mes * (15 / 100)

print ('A comissão de vendas do funcionário foi de: R$', comis, ', logo, seu salário vai ser de: R$', sal_fixo + comis)
