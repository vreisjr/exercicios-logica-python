
matricula= int(input('Informe o número da matrícula:'))

while matricula != 99:
    salario= float(input('Informe o salário:'))
    vendas= float(input('Informe o total de vendas:'))

    if vendas <= 1000:
        comis= vendas * 0.03
    else:
        comis= 1000 * 0.03 + (vendas - 1000) * 0.05
    print (matricula)
    print (vendas)
    print (salario + comis)

    matricula= int(input('Informe o número da matrícula:'))
