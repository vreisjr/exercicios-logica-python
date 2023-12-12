# Entrar com a distância percorrida de um automóvel (Km), e o gasto de combustível (L)

tot_km= float(input('Digite a distância percorrida pelo automóvel: Km'))
tot_litros= float(input('Digite o total de combustível gasto: L'))

#calcular a razão entre a distância percorrida, e o total de combustível gasto, para obter o consumo médio

consumo= tot_km / tot_litros
consumo_arredontado= round(consumo, 3)

print ('O total de consumo é:', consumo_arredontado, 'km/l')
