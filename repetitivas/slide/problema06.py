#receber a quantidade de gols feitos em cada 3 jogos realizados em um campeonato de futebol

conta_gol= 0
qtd_jogo= 1

for i in range (3):
    gol= int(input('Informe o número de gols do ' +str(qtd_jogo)+ 'º jogo:'))
    qtd_jogo= qtd_jogo + 1
    conta_gol= conta_gol + gol

print ('O número total de gols feito a cada três jogos do campeonato foi de:', conta_gol)