#inserir o peso do peixe
peso_peixe= float(input('Digite o peso do peixe:'))

#se exceder o peso de 50kg, exibir o excesso de peso e o valor de multa. se não, exibir a menssagem 'peso ok!'

if peso_peixe >= 50:
    excesso= peso_peixe - 50
    multa= excesso * 4
    print ('Excesso:', excesso, ', a multa vai ser de: R$', multa)

else:
    print('Peso ok!')