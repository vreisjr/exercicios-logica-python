#Inserir um custo de fábrica de um carro

cust_carro_fab= float(input('Digite o preço de fábrica do carro: R$'))

#calcular os imposto sobre o custo de fábrica e a prcentagem do distribuidor

impostos= cust_carro_fab * (45 / 100)
porc_distr= impostos * (28 / 100)
cust_consumidor= cust_carro_fab + impostos + porc_distr

print ('O custo ao consumidor vai ser de R$', format(cust_consumidor, '.2f'))
