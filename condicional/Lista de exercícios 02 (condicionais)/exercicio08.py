#informar o peso e a altura do indivíduo

peso= float(input('Informe o peso: Kg'))
altura= float(input('Informe a altura: M'))

#calcular o IMC

imc= peso / (altura ** 2)

# classificar o IMC

if imc >= 40:
    print ('Obeso Mórbido')
elif imc >= 30:
    print ('Obeso')
elif imc >= 25:
    print ('Sobre peso')
elif imc >= 20:
    print ('Peso normal')
else:
    print ('Abaixo do peso')
