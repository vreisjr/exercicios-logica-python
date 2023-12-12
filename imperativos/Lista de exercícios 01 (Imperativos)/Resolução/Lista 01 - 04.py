cotacao = float(input('Digite a taxa de câmbio: '))
qtd = float(input('Informe a qauntidade monetária: '))
real = cotacao * qtd
print('Valor em Real R$',format(real,".2f"))