custo = float(input('Informe o custo de fábrica R$'))
imposto = custo * 0.45
distribuicao = (custo +imposto) * 0.28
venda = custo + imposto + distribuicao
print('Preço de venda R$',format(venda,".2f"))