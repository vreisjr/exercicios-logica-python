#Inserir um número inteiro menor que 1000

n_int= int(input('Digite um número inteiro menor que 1000:'))

#e mostrar a centena, dezena e unidade desse número

unidade= n_int % 10

dezena= (n_int - unidade) / 10

centena= dezena - (dezena % 10)

print ('A centena do número é:', centena / 10, ', a dezena é:', dezena % 10, ',e a unidade é:', unidade)
