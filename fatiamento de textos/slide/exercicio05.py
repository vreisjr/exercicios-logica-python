maiorfrase=''
maiortamanho= 0
for i in range (5):
    frase= input('Digite uma frase:')

    if len(frase) > maiortamanho:
        maiorfrase= frase
        maiortamanho= len(frase)

print (maiorfrase)