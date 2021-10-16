def suma_listas(lista1, lista2):
    resultado = []
    acc = 0
    for i in range(len(lista1)):
        acc = lista1[i] + lista2[i]
        resultado.append(acc)
    return resultado

def resta_listas(lista1, lista2):
    resultado = []
    acc = 0
    for i in range(len(lista1)):
        acc = lista1[i] - lista2[i]
        resultado.append(acc)
    return resultado

def imprimir_matriz(matriz):
    for lista in matriz:
        print(lista)
