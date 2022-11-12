from time import sleep
morango1 = 2.50 #! SE O CLIENTE PEGAR MENOS DE 5KG É ESSE VALOR DE $2.50
morango2 = 2.20 #! SE O CLIENTE PEGAR MAIS DE 5KG É ESSE VALOR DE $2.20
maca1 = 1.80 #! SE O CLIENTE PEGAR MENOS DE 5KG É ESSE VALOR DE $1.80
maca2 = 1.50 #! SE O CLIENTE PEGAR MAIS DE 5KG É ESSE VALOR DE $1.50
kg = 50
print("-"*57)
# print("| PREZADO CLIENTE O PESO APROXIMADO DAS FRUTAS É DE 100g |")
print("-"*57)
print("|      NOMES   |   ATE 5KG        |  ACIMA DE 5KG       |")
print("|      MORANGO | R$ 2.50 por KG   | R$ 2.20 por KG      |")
print("|      MAÇA    | R$ 1.80 por KG   | R$ 1.50 por KG      |")
print("-"*57)
user = float(input('Quantos KG voce gostaria de adicionar no Carrinho:')) #! O CLIENTE VAI ADICIONAR QUANTOS KILOS QUE ELE QUER!!!!!
maca_menor = maca1 * user #! CALCULANDO SE O CLIENTE PEGAR MENOS DE 5KG
morango_menor = morango1 * user #! CALCULANDO SE O CLIENTE PEGAR MENOS DE 5KG
maca_maior = maca2 * user  #! CALCULANDO SE O CLIENTE PEGAR MAIS DE 5KG É ESSE
morango_maior = morango2 * user #! CALCULANDO SE O CLIENTE PEGAR MAIS DE 5KG
# -------------------------------------------------------------------------- #
maca_preco_desconto = 0.07 * 1.50
maca_valor = maca_preco_desconto - 1.50
maca_x = int(user) * 1000
maca_y = maca_x * maca_valor
# -------------------------------------------------------------------------- #
morango_preco_desconto = 0.07 * 2.20
morango_valor = morango_preco_desconto - 2.20
morango_x = int(user) * 1000
morango_y = morango_x * morango_valor
if user<5: #! VERIFICANDO A RESPOSTA....
    print("-" * 58)
    print("|      NOMES   | VALORES ATE 5KG  | VALORES ACIMA 5KG    |")
    print("|      MORANGO | R$ ",int(morango_menor)," por KG   | R$ ",int(morango_maior)," por KG     |")
    print("|      MAÇA    | R$ ",int(maca_menor)," por KG   | R$ ",int(maca_maior)," por KG     |")
    print("-" * 58)
    user2= str(input("Gostaria de adicionar qual fruta no carrinho:"))
    if user2.lower()=="Morango".lower() or  user2.lower() == "MAÇA".lower():  #! VERIFICANDO A RESPOSTA....
        print("-" * 58)
        print(" <<<<<<< SEU PEDIDO FOI REALIZADO COM SUCESSO >>>>>>>")
        print("-" * 58)
elif user>5: #! VERIFICANDO A RESPOSTA....
    if user >= 10:
        print("-" * 58)
        print("|      NOMES   | VALORES ATE 5KG  | VALORES ACIMA 5KG    |")
        print("|      MORANGO | R$ ", int(morango_menor), " por KG   | R$ ", int(morango_y), " por KG     |")
        print("|      MAÇA    | R$ ", int(maca_menor), " por KG   | R$ ", int(maca_y), " por KG     |")
        print("-" * 58)
        user2 = str(input("Gostaria de adicionar qual fruta no carrinho:"))
        if user2.lower() == "Morango".lower() or user2.lower() == "MAÇA".lower():
            print("-" * 58)
            print(" <<<<<<< SEU PEDIDO FOI REALIZADO COM SUCESSO >>>>>>>")
            print("-" * 58)
            exit()
    elif user >= 5:
        print("-" * 58)
        print("|      NOMES   | VALORES ATE 5KG  | VALORES ACIMA 5KG    |")
        print("|      MORANGO | R$ ", int(morango_menor), " por KG   | R$ ", int(morango_menor), " por KG     |")
        print("|      MAÇA    | R$ ", int(maca_menor), " por KG   | R$ ", int(maca_menor), " por KG     |")
        print("-" * 58)
        user2 = str(input("Gostaria de adicionar qual fruta no carrinho:"))
        if user2.lower() == "Morango".lower() or user2.lower() == "MAÇA".lower():
            print("-" * 58)
            print(" <<<<<<< SEU PEDIDO FOI REALIZADO COM SUCESSO >>>>>>>")
            print("-" * 58)
