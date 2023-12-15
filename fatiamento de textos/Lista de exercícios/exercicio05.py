frase= input('Informe a palavra ou frase:')
frase_minsc= (frase.lower())
frase_junta= (frase_minsc.replace(' ', ''))
frase_inver= (frase_junta[::-1])

if frase_inver == frase_junta:
    print ('É um palímdromo')

else:
    print ('Não é um palímdromo')