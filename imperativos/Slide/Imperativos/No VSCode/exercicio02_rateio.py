#Rateio
#Recebe os valores das variáveis de entrada
qtd_apto= int(input('Quantidade de apartamentos:'))
vlr_agua= float(input('Valor da Água: R$'))
vlr_luz= float(input('Valor da luz: R$'))
#Calcula o Valor a Pagar
vlr_a_pagar= (vlr_agua + vlr_luz)/ qtd_apto
print('O valor do Rateio vai ser de: R$', vlr_a_pagar)
 