#Insira a idade de uma pessoa em anos, meses e dias

anos= int(input('Digite a idade em anos:'))
meses= int(input('e meses:'))
dias=int(input('e dias:'))

#converte a variavel anos e meses para dias

cov_m_d= meses * 30
cov_a_d= anos * 360
dias_vida= dias + cov_m_d + cov_a_d

#somar dias com o resultado das duas conversões

print ('São', format(dias_vida, '.2f'), 'dias de vida')
