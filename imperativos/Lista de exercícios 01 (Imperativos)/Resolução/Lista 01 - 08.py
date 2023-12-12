nome = input('Informe o nome do vendedor: ')
fixo = float(input('Informe o salário fixo R$'))
vendas = float(input('Informe o total de vendas do mês R$'))
comissao = 0.15 * vendas
final = fixo + comissao
print('Nome do vendedor',nome,' seu salário fixo é R$', fixo, 'O salário final ficou R$', format(final,".2f"))