posicao_alcance= 0
nome= input('Informe um nome:')
conta_nome= len(nome)

for i in range (conta_nome + 1):
    print (nome[0:posicao_alcance])
    posicao_alcance= posicao_alcance + 1