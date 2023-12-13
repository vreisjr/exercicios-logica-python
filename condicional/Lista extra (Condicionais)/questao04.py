# informar o valor de A e de B

vlr_a= float(input('Qual o valor de A:'))
vlr_b= float(input('Qual o valor de B:'))

# se os valores forem iguais, deveram ser somados, do contrário, deveram ser multiplicados. Ao final de qualquer uma das operações, o resultado deverá ser denominada a variável C

if vlr_a == vlr_b:
    vlr_c= vlr_a + vlr_b

else:
    vlr_c= vlr_a * vlr_b

print('O valor de C é:', vlr_c)
