#inserir um número indeterminado de idades, se encerra quando for digitado uma idade igual a 0. Calcular a média das idades

idade_soma= 0
idade_conta= 0
idade= int(input('Informe a idade:'))

while idade != 0:
    idade_conta= idade_conta + 1
    idade_soma= idade + idade_soma
    idade= int(input('Informe a idade:'))

idade_media= idade_soma / idade_conta

print ('A média das idades é:', idade_media)