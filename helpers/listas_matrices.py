def suma_listas(lista1:list, lista2:list) -> list:
    resultado = []
    acc = 0
    for i in range(len(lista1)):
        acc = lista1[i] + lista2[i]
        resultado.append(acc)
    return resultado

def resta_listas(lista1:list, lista2:list) -> list:
    resultado = []
    acc = 0
    for i in range(len(lista1)):
        acc = lista1[i] - lista2[i]
        resultado.append(acc)
    return resultado

def imprimir_matriz(matriz: list) -> None:
    for lista in matriz:
        print(lista)
