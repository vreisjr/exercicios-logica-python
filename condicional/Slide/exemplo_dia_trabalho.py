#Informe o salário

vlr_salario= float(input('Digite o salário: R$'))

#com salário inferior a R$1100, aumento de 10%; inferior a R$2000, aumento de 7%; os demais terão 5%

if vlr_salario < 1100:
    vlr_novo_slr= vlr_salario * 1.1

elif vlr_salario <= 2000:
    vlr_novo_slr= vlr_salario * 1.7

else:
    vlr_novo_slr= vlr_salario * 1.05

print ('O novo salário vai ser de: R$', vlr_novo_slr)
