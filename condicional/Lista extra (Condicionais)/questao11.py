# definir como entrada a preço de etiqueta e a condição de pagamento

preco= float(input('Insira o preço de etiqueta: R$'))
condicao= int(input('Insira o código da condição:'))

#para código da condição usar: 1- à vista, 20% desconto; 2 - à vista no cartão, 15%; 3 - em duas vezes, preço de etiqeta; 4 - em quatro vezes, juros de 10%

if condicao == 1:
    novo_preco= preco - (preco * 0.20)

if condicao == 2:
    novo_preco= preco - (preco * 0.15)

if condicao == 3:
    novo_preco= preco

if condicao == 4:
    novo_preco= preco + (preco * 0.10)

print ('A condição foi', condicao, ', e preço vai ficar: R$', novo_preco)
