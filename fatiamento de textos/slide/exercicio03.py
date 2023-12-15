nome= input('Informe um nome com no mínimo 10 caracteres:')
nome= nome.replace(' ', '')

while len(nome) < 10:
    print ('Nome inválido')
    nome= input('Informe um nome com no mínimo 10 caracteres:')
    nome= nome.replace(' ', '')

metade= len(nome) // 2

parte1= nome[0:metade]
parte2= nome[metade:]

senha= parte2[0:2] + '%%' + parte1[-3:]

print (parte1, parte2, senha)