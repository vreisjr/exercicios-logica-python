

divida= float(input('Informe o valor da dívida: R$'))

while divida != 0:
    parcela= int(input('Informe a quantidade de parcelas (1, 6, 9, 12):'))
    

    if parcela == 1:
        juros= divida * 0.10
        soma= divida + juros
        print ('O valor da dívida é de R$', divida, ', o valor do juros de', juros, ', em 1 parcelas com o valor de R$', soma)
    
    elif parcela == 6:
        juros= divida * 0.15
        soma= divida + juros
        valor_parcela= soma / 6
        print ('O valor da dívida é de R$', divida, ', o valor do juros de', juros, ', em 6 parcelas de R$', valor_parcela)
    
    elif parcela == 9:
        juros= divida * 0.20
        soma= divida + juros
        valor_parcela= soma / 9
        print ('O valor da dívida é de R$', divida, ', o valor do juros de', juros, ', em 9 parcelas de R$', valor_parcela)
    
    elif parcela == 12:
        juros= divida * 0.25
        soma= divida + juros
        valor_parcela= soma / 12
        print ('O valor da dívida é de R$', divida, ', o valor do juros de', juros, ', em 12 parcelas de R$', valor_parcela)
    
    else:
        print ('Parcela inválida')
    
    divida= float(input('Informe o valor da dívida: R$'))