frase= input('Informe uma frase:')

#os primeiros 5 caracteres da frase

print ('Os 5 primeros caracteres são:', (frase[0:6]))
#os últimos 5 caracteres da frase

print ('Os 5 últimos caracteres são:', (frase[0:6][::-1]))
#Os primeiros 5 caracteres invertidos 

print ('Os 5 caracteres invertidos são:', (frase[::-1][0:6]))
#a quantidade de caracteres da frase

print ('São', len(frase), 'caracteres na frase')