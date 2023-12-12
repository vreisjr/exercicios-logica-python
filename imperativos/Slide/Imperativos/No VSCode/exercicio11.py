#digitar o tempo em segundos
seg= int(input('Digite os segundos:'))

#converter para horas, minutos e segundos

horas= seg // 3600
minutos= seg % 3600 // 60
segundos= seg % 3600 % 60

print ('são', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos')
