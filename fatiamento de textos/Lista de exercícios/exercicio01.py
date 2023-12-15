soma_a= 0

for i in range (5):
    frase= input('Informe a frase:')
    a_minsc= (frase.lower())
    conta_a= (a_minsc.count('a'))
    soma_a= soma_a + conta_a

print ('O total de letras A contidas nas 5 frases são de:', soma_a)

#faltei substituir os 'A' acentuados por 'a'