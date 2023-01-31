
vencedor = int(input("Qual numero: "))


if vencedor < 19999:
    blocos = 0
    numeroInicial1 = 0
    numeroFinal1 = 0
    listaBlocos1 = []
    while numeroFinal1 < 19999:
        blocos += 1
        numeroInicial1 += 1
        numeroFinal1 += 20
        blocos = int(blocos)
        listaBlocos1.append(numeroInicial1)
        listaBlocos1.append(numeroFinal1)
        numeroInicial1 = numeroFinal1
    blocoGanhador = 1
    blocoRevisado = 0
    while True:
        if vencedor >= listaBlocos1[blocoRevisado] and vencedor <= listaBlocos1[blocoRevisado + 1]:
            print("O numero ganhador está no bloco: ", blocoGanhador)
            break
        else:
            blocoGanhador += 1
            blocoRevisado += 2



elif vencedor > 20000 and vencedor < 39999:
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
    blocoGanhador = 1
    blocoRevisado = 0
    while True:
        if vencedor >= listaBlocos1[blocoRevisado] and vencedor <= listaBlocos1[blocoRevisado + 1]:
            print("O numero ganhador está no bloco: ", blocoGanhador - 1001)
            break
        else:
            blocoGanhador += 1
            blocoRevisado += 2
    

elif vencedor > 60000 and vencedor < 79999:
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
    blocoGanhador = 1
    blocoRevisado = 0
    while True:
        if vencedor >= listaBlocos1[blocoRevisado] and vencedor <= listaBlocos1[blocoRevisado + 1]:
            print("O numero ganhador está no bloco: ", blocoGanhador)
            break
        else:
            blocoGanhador += 1
            blocoRevisado += 2
    


elif vencedor < 59999 and vencedor > 40000:
    blocos = 0
    numeroInicial1 = 40000
    numeroFinal1 = 40000
    listaBlocos1 = []
    while numeroFinal1 < 59999:
        blocos += 1
        numeroInicial1 += 1
        numeroFinal1 += 20
        blocos = int(blocos)
        listaBlocos1.append(numeroInicial1)
        listaBlocos1.append(numeroFinal1)
        numeroInicial1 = numeroFinal1
    blocoGanhador = 1
    blocoRevisado = 0
    while True:
        if vencedor >= listaBlocos1[blocoRevisado] and vencedor <= listaBlocos1[blocoRevisado + 1]:
            print("O numero ganhador está no bloco: ", blocoGanhador - 1001)
            break
        else:
            blocoGanhador += 1
            blocoRevisado += 2
