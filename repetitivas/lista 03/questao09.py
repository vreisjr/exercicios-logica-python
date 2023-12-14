cont_par= 0 
conta_impar= 0

numero= int(input('Informe um número:'))

while numero != 99:
    if numero % 2 == 0:
        cont_par= cont_par + 1
    
    else:
        conta_impar= conta_impar + 1
    
    numero= int(input('Informe um número:'))

perc_par= cont_par / (cont_par + conta_impar) * 100
perc_impar= 100 - perc_par

print (perc_par)
print (perc_impar)
