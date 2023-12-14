#informar cinco notas e definir a média aritimética

soma= 0
n= 1
while (n <= 5):
    nota= float(input('Informe a '+ str(n)+'º nota:'))
    soma = soma + nota
    n = n + 1
media= soma / 5
print('A média calculada foi:', media)
