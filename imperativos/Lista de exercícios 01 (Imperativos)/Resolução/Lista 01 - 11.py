numero = int(input('Informe o número: '))
centena = numero // 100
dezena = numero % 100 // 10
unidade = numero % 100 % 10
print( 'O numero',numero,'tem',centena,'centenas',dezena,'dezenas e ',unidade,'unidades')