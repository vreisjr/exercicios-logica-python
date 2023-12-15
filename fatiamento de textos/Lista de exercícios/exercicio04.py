#Informar três telfones com o DDD de São Paulo, e acrescentar o 9 em cada número

for i in range (3):
    telefone= input('Informe o telefone: (011)')
    n_DDD= str('0119') + telefone
    print ('O novo número com a adição do 9 fica:', n_DDD)

# Na entrada, a questão exige que seja inserido o 011 tbm