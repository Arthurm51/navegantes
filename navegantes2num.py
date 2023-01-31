


blocos = 0
numeroInicial1 = 20000
numeroFinal1 = 20000
listaBlocos1 = []
while numeroFinal1 < 39999:
    
    blocos += 1
    numeroInicial1 += 1
    numeroFinal1 += 20

    blocos = int(blocos)
    listaBlocos1.append(numeroInicial1)
    listaBlocos1.append(numeroFinal1)
    numeroInicial1 = numeroFinal1
vencedor = int(input("Qual numero: "))
blocoGanhador = 1
blocoRevisado = 0

while True:

    if vencedor >= listaBlocos1[blocoRevisado] and vencedor <= listaBlocos1[blocoRevisado + 1]:
        print("O numero ganhador está no bloco: ", blocoGanhador - 1001)
        print("\n\n\n")
        print("################## VALORES ENTRE 20 MIL E 40 MIL ##################")
        print("################## VALORES ENTRE 20 MIL E 40 MIL ##################")
        print("################## VALORES ENTRE 20 MIL E 40 MIL ##################")
        print("################## VALORES ENTRE 20 MIL E 40 MIL ##################")
        print("################## VALORES ENTRE 20 MIL E 40 MIL ##################")
        print("################## VALORES ENTRE 20 MIL E 40 MIL ##################")
        print("################## VALORES ENTRE 20 MIL E 40 MIL ##################")
        break
    elif vencedor == 20000:
        print("O numero ganhador está no bloco: 1000")
        break
    else:
        blocoGanhador += 1
        blocoRevisado += 2





    



    
