letras= 'abcdefghijklmnopqrstuvwxyz'
nome_criptografado= ''
nome= input('Informe um nome:')
nome= nome.lower()
for i in range(len(nome)):
    if nome[i] == 'a':
        nome_criptografado = nome_criptografado + 'z'
    elif nome[i] == ' ':
        nome_criptografado = nome_criptografado + ' '
    else:
        posicao= letras.find(nome[i])
        nome_criptografado= nome_criptografado + letras[posicao -1]

print (nome, nome_criptografado)