soma= 0
nome_prod= str(input('Informe o nome do produto:'))
while nome_prod != ' ':
    preco_prod= float(input('Informe o preço do produto: R$'))
    qtd_prod= int(input('Informe a quantidade do produto:'))
    vlr_venda= preco_prod * qtd_prod
    print (nome_prod, '- preço unitário: R$', preco_prod, '- quantidade:', qtd_prod, '- valor: R$', vlr_venda)
    soma= soma + vlr_venda
    nome_prod= str(input('Informe o nome do produto:'))

dinheiro= float(input('Informe o número do dinheiro que vai pagar: R$'))

troco= dinheiro - soma

print ('O total deu R$', format(soma, '2f'), ', a quantia de dinheiro é de R$', dinheiro, ', Logo, o troco vai ser de R$', format(troco, '2f'))