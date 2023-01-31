blocos = 0
numeroInicial1 = 0
numeroFinal1 = 0
numeroInicial2 = 4500
numeroFinal2 = 4500
listaBlocos1 = []
listaBlocos2 = []
while numeroFinal1 < 39999 and numeroFinal2 < 79999:
    arquivo = open("blocos.txt", "a")
    blocos += 1
    numeroInicial1 += 1
    numeroFinal1 += 20
    numeroInicial2 += 1
    numeroFinal2 += 20
    #print("Bloco ", str(blocos), "--- ", numeroInicial1, " até ", numeroFinal1, " e ", numeroInicial2, " até ", numeroFinal2, "\n")
    #arquivo.write("Bloco "+ str(blocos)+ "--- "+ str(numeroInicial1)+ " até "+ str(numeroFinal1)+ " e "+ str(numeroInicial2)+ " até "+ str(numeroFinal2)+ "\n")
    blocos = int(blocos)
    listaBlocos1.append(numeroInicial1)
    listaBlocos1.append(numeroFinal1)
    listaBlocos2.append(numeroInicial2)
    listaBlocos2.append(numeroFinal2)
    numeroInicial1 = numeroFinal1
    numeroInicial2 = numeroFinal2


vencedor = int(input("Qual numero: "))
blocoGanhador = 1
blocoRevisado = 0

while True:

    if vencedor >= listaBlocos1[blocoRevisado] and vencedor <= listaBlocos1[blocoRevisado + 1] or vencedor >= listaBlocos2[blocoRevisado] and vencedor <= listaBlocos2[blocoRevisado + 1]:
        print("O numero ganhador está no bloco: ", blocoGanhador)
        break
    else:
        blocoGanhador += 1
        blocoRevisado += 2





    



    
