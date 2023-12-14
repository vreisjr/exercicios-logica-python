boi_gordo= -1
boi_magro= 999999999999999999

for i in range (90):
    numero= int(input('Informe o número do boi:'))
    peso= float(input('Informe o peso do boi:'))

    if peso > boi_gordo:
        boi_gordo= peso
        cod_gordo= numero
    
    if peso < boi_magro:
        boi_magro= peso
        cod_magro= numero

print (cod_gordo, boi_gordo)
print (cod_magro, boi_magro)