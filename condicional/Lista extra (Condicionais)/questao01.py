#Informar o valor de A, B e C

vlr_a= float(input('Informe o valor de A:'))
vlr_b= float(input('Informe o valor de B:'))
vlr_c= float(input('Informe o valor de C:'))

#Informar na tela se a soma de A e B é menor que C

soma_ab= vlr_a + vlr_b

if soma_ab < vlr_c:
    print ('O valor somado de A e B e menor que C')

else:
    print ('O valor somado de A e B é maior que C')