vlr_dentro= 0
vlr_fora=0
for i in range (10):
    vlr= int(input('Insira um número inteiro:'))

    if vlr >= 10 and vlr <= 20:
        vlr_dentro= vlr_dentro + 1
    
    else:
        vlr_fora= vlr_fora + 1
    
print ('são', vlr_dentro, 'valores dentro de 10 e 20')
print ('são', vlr_fora, 'valores fora de 10 e 20')