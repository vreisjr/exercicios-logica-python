#Informe o peso e a altura

peso= float(input('informe o peso:'))
altura= float(input('informe a altura:'))

#calcular o IMC, e classificar

imc= peso / (altura ** 2)

if imc > 30:
    print ('Obeso')
elif imc > 25:
    print ('Acima do peso')
elif imc > 18.5:
    print ('Peso normal')
elif imc < 18.5:
    print ('Abaixo do peso')
