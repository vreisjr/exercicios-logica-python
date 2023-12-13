#informe um valor de três dígitos

vlr= int(input('informe um número de três dígitos:'))

#informar a centena, dezena e unidade, e somar entre eles

centena = vlr // 100
dezena = vlr % 100 // 10
unidade = vlr % 100 % 10

soma= centena + dezena + unidade

print ('A soma entre', centena, ',', dezena, 'e', unidade, 'é de', soma)
