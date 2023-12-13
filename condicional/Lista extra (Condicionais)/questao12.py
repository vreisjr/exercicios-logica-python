id_aluno= int(input('insira a identificação do aluno:'))
nota_1= float(input('Insira a nota 1:'))
nota_2= float(input('Insira a nota 2:'))
nota_3= float(input('Insira a nota 3:'))

media= (nota_1 + nota_2 + nota_3) / 3
ma= (nota_1 + nota_2 * 2 + nota_3 * 3 + media) / 7

if ma >= 90:
    print ('A aprovado')

elif ma >= 75:
    print ('B aprovado')

elif ma >= 60:
    print ('C aprovado')

elif ma >= 40:
    print ('D reprovado')

else:
    print ('E reprovado')

print ('O aluno de número:', id_aluno, ', teve as notas:', nota_1, ',', nota_2, 'e', nota_3,'. Sua média de atividades foi de', media, 'e a média de aproveitamento foi de', ma)