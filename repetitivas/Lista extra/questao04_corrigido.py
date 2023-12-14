ordenado= True
anterior= int(input('Informe um número:'))
for i in range (4):
    numero= int(input('Informe um número:'))
    if numero >= anterior and ordenado:
        ordenado= True
    else:
        ordenado= False
    anterior= numero
if ordenado:
    print ('Ordenado')
else:
    print ('Fora da ordem')