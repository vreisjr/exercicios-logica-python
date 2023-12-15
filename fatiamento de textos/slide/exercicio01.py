data= str(input('Informe uma data DD/MM/AAAA:'))

dia= int(data[0:2])
mes= int(data[3:5])
ano= int(data[6:])

soma= dia + mes + ano

print ('A soma calculada foi:', soma)