Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Rateio
>>> #Recebe os valores das variáveis de Entrada
>>> qtd_apto = int(input('Qtd de Apartamentos:'))
Qtd de Apartamentos:16
>>> vlr_agua = float(input('Valor da água:'))
Valor da água:86.5
>>> vlr_luz = float(input('Valor da Luz:'))
Valor da Luz:118.6
>>> #Calcula o Valor a Pagar
>>> vlr_a_pagar = (vlr_agua + vlr_luz)/ qtd_apto
>>> print('O Valor do Rateio foi:', vlr_a_pagar)