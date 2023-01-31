
blocos = 0
numeroInicial1 = 60000
numeroFinal1 = 60000
listaBlocos1 = []
while numeroFinal1 < 79999:
   
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
        print("O numero ganhador está no bloco: ", blocoGanhador)
        print("\n\n\n")
        print("################## VALORES ACIMA DE 60 MIL ##################")
        print("################## VALORES ACIMA DE 60 MIL ##################")
        print("################## VALORES ACIMA DE 60 MIL ##################")
        print("################## VALORES ACIMA DE 60 MIL ##################")
        print("################## VALORES ACIMA DE 60 MIL ##################")
        print("################## VALORES ACIMA DE 60 MIL ##################")
        print("################## VALORES ACIMA DE 60 MIL ##################")
        break
    else:
        blocoGanhador += 1
        blocoRevisado += 2

