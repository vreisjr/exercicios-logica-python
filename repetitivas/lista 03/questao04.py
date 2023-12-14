#Ler a idade de 15 pessoas e apresentar: maior idade, nome da pessoa mais nova e a média das idades

soma= 0 
maior_i= -1
menor_i= 999999999999999999999

for i in range (15):
    nome = input ('Informe o nome:')
    idade= int (input('Informe a idade:'))

    if idade < menor_i :
        menor_i= idade
        nome_novo= nome
    
    if idade > maior_i:
        maior_i= idade
    
    soma= soma + idade

media= soma / 15
print (maior_i)
print (nome_novo)
print (media)
