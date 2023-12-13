#Responder cinco persguntas

p1= str(input('Telefonou para a vítima?'))
p2= str(input('Esteve no local do crime?'))
p3= str(input('Mora perto da vítima?'))
p4= str(input('Devia para a vítima?'))
p5= str(input('Já trabalhou com a vítima?'))

#emitir uma classificação sobre o interrogado, se sim para 2 questões, "suspeita"; entre 3 e 4, "cúmplice"; e 5, "assasino". Caso contrário, será "Inocente"

if p1 == 'sim':
    r1= 1
if p1 == 'não':
    r1= 0

if p2 == 'sim':
    r2= 1
if p2 == 'não':
    r2= 0

if p3 == 'sim':
    r3= 1
if p3 == 'não':
    r3= 0

if p4 == 'sim':
    r4= 1
if p4 == 'não':
    r4= 0

if p5 == 'sim':
    r5= 1
if p5 == 'não':
    r5= 0

total= r1 + r2 + r3 + r4 + r5

if total == 5:
    print ('Assassino')
elif total == 4:
    print ('Cúmplice')
elif total == 3:
    print ('Cúmplice')
elif total == 2:
    print ('Suspeito')
elif total == 1:
    print ('Inocente')
elif total == 0:
    print ('Inocente')