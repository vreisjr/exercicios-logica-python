#Iserir o nome de um vendedor de loja, seu salário fixo e o numero de suas vendas

vendedor= str(input('Digite o nome do vendedor:'))
salario= float(input('Digite o seu salário fixo: R$'))
n_vendas= float(input('Digite o valor total de vendas realizadas no mês: R$'))

#calcular a cmissão que ele ganha em cima do valor de suas vendas e somar ao seu salário fixo

comis_vendas= n_vendas * (15 / 100)
sal_final= salario + comis_vendas

print ('A comissão de vendas de', vendedor, 'foi de R$', comis_vendas, 'e o salário fixo é de R$', salario, ',logo, seu pagamento final do mês vai ser R$', sal_final)
