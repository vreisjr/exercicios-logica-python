#Receber 5 placas de automóveis no formato 'LLLNLNN', onde N são números, e L são letras 

soma_palca= 0

for i in range (5):
    placa= input('Informe a placa do carro em formato LLLNLNN (onde L são letras, e N são números):')

    n3= int(placa[3])
    n5= int(placa[5])
    n6= int(placa[6])
    soma_palca= n3 + n5 + n6
    print ('A soma dos números é de:', soma_palca)