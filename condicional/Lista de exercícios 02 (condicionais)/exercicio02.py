#informar duas notas de um aluno

nota1= float(input('Digite a primeira nota:'))
nota2= float(input('Digite a segunda nota:'))

#calcular a média das notas, se a média for igual ou maior que 7, exibir a mensagem "Aprovado"; se for inferior a 7, exibir a mensagem "Reprovado"; e so for igual a 10, exibir "Aprovado com Distinção"

media= (nota1 + nota2) / 2

if media == 10 :
    print ('Aprovado com Distinção')
elif media >= 7:
    print ('Aprovado')
else:
    print ('Reprovado')
