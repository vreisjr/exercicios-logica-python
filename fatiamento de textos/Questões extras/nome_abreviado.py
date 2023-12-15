nome= input('informe um nome:')
p1= nome[0:nome.find(' ')]
p2= nome[nome.find(' ')+1]
p3= nome[::-1]
p3= p3[0:p3.find(' ')]
p3= p3[::-1]
print (str(p1 + ' ' + p2 + ' ' + p3).title())