# receber 20 iadades diferentes, e calcular a média aritimética deles

soma= 0
for n in range (20):
    idade= int(input('Informe a idade:'))
    soma= soma + idade

media= soma / 20
print ('A média aritmética das idades é:', media)
