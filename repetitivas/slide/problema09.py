#elaborar um sitema de entradas que peça pesos aleatórios. Assim que receber um valor acima de 200kg, deve se encerrar. Ao final, exibir o menor peso recebido.

menor_peso= 99999999999999999999999

peso= float(input('Informe o peso (Kg):'))

while peso < 200:
    peso= float(input('Informe o peso (Kg):'))

    if peso < menor_peso:
        menor_peso= peso

print ('O menor peso digitado foi (Kg):', menor_peso)