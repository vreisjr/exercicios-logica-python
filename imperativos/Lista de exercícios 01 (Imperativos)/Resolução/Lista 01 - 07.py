custo = float(input('Informe o valor de custo R$'))
aumento = float(input('Informe margem % '))
venda = custo * (1 + aumento / 100)
print("Valor venda R$", format(venda,'.2f'))