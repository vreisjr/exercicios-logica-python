#Entrar com um valor de depósito

vlr_deps= float(input('Qual valor você deseja depositar: R$'))

#fazer o cálculo com o valor depositado, quanto ele ficaria depois de um mês, com juros de 0,50% 

aplic_a_m= vlr_deps * (0.50 / 100)

print('O valor de juros seria de: R$', aplic_a_m, ', logo, esse valor ficaria: R$', aplic_a_m + vlr_deps, 'com aplicação de a.m 0,50%')
