""" 
    #! EMPRESA FUTURA SISTEMA !#

 1- Exercio do a Sequencia Fibonacci LOOP (1,2,3,5,8....)

"""
from time import sleep #! É UMA BICLIOTECA QUE DA UM TEMPO DE ESPERA PARA O SISTEMA SER INICILIZADO...
x = int("0") #! Adicionei um String pelo motivo de Usar um conversor de INT sabendo que valor 0.
y = int("1") #! Adicionei um String pelo motivo de Usar um conversor de INT sabendo que valor 1.
dados = list() # Adicionamos uma Lista para salvar todas Vareaveis.
dados.append(x) # Aqui foi adiciona uma vareavel que tem o valor 0.
dados.append(y) # Aqui foi adiciona uma vareavel que tem o valor 1.
v1 = int(input("Quantas vez voce quer LOOP RODANDO:")) #! Quando o Usuario for digitar um valor que for igual a quantas vez rodada, o LOOP Terminar!!! 
print("MAQUINA EM PROCESSO, AGUARDE O VALOR ESPERADO...") #! Adicionei uma mensagem para notificar o usuario que esta em PROCESSO o Sistema...
sleep(1.5) # Adionei um Tempo de Espera para o Usuario aguarda em torno de 1.5 Segundo
while v1: # Aqui nos adicinamos um LOOP INIFITO, QUE APOS QUE ELE SER TORNA TRUE COMECA A INICIAR O LOOP!!!!
    x = x+1 # Adicionamos um Somador para ele ficar somando 1+1 ate que verifique o que o usuario digito se estiver igual, ele apos encerra o LOOP....
    v = dados[-1]+dados[-2] # A VAREAVEL DADOS[-1] VERIFICA QUAL è O PENUTIMO NUMERO, A VAREAVEL DADOS[-2] VERIFICA QUAL è O ANTIPENUTIMO NUMERO e APOS FAZ A SOMA!!!!!
    sleep(0.5) # TEMPO DE ESPERA 0.5 SEGUNDO.
    dados.append(v) # ESSA VAREAVEL ELA ADICIONA NA LISTA TODOS OS DADOS QUE FORAM CALCULADO....
    if x==v1: # VEREFICA QUANTAS VEZ O LOOP RODOU PARA VERIFICAR QUAL E MOMENTO CERTO DE PARAR...
        dados.pop(1) # ESSA VAREAVEL ELA EXCLUIR O NUMERO, POR QUE ELE SAO DUPLICADO, PARA A LISTA NAO TER NENHUM NUMERO DUPLICADO...
        print(dados) # ESSA VAREAVEL VAI MOSTRA PRO USUARIO A LISTA DE DADOS DO EXERCICIO FIBOONACCI...
        break # APOS QUE IF SER VERDADEIRO ESSA VAREAVEL ELA QUEBRA O LOOP...
"""
    MENSAGEM: EXERCICIO TERMINADO EM 25 MINUTOS 11|11|2022...
    DEVELOPER: @fehoffcial
    GITHUB: https://github.com/fehoffcial
"""
