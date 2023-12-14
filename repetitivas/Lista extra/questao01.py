soma_cd= 0
qtd_cd= int(input('Informe a quantidade de cds:'))

for i in range (qtd_cd):
    valor_cd= float(input('Informe o o preço do cd: R$'))
    soma_cd= soma_cd + valor_cd

media_cd= soma_cd / qtd_cd

print ('O valor da coleção é de: R$', soma_cd)
print ('O preço médio da coleção é de: R$', media_cd)