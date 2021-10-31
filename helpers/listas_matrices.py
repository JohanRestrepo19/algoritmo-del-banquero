def suma_listas(lista1: list, lista2: list) -> list:
    resultado = []
    acc = 0
    for i, _ in enumerate(lista1):
        acc = lista1[i] + lista2[i]
        resultado.append(acc)
    return resultado


def resta_listas(lista1: list, lista2: list) -> list:
    resultado = []
    acc = 0
    for i, _ in enumerate(lista1):
        acc = lista1[i] - lista2[i]
        resultado.append(acc)
    return resultado


def imprimir_matriz(matriz: list) -> None:
    for lista in matriz:
        print(lista)


def lista_cadenas_lista_enteros(lista_cadenas: list) -> list:
    lista_enteros = []
    for cadena in lista_cadenas:
        lista_enteros.append(int(cadena))
    return lista_enteros


def convertir_str_lista(cadena_cruda: str) -> list:
    lista_cadenas = cadena_cruda.split()
    return lista_cadenas_lista_enteros(lista_cadenas)


def convertir_str_matriz(cadena_cruda: str, tam_fila: int) -> list:
    lista_cadenas = cadena_cruda.split()
    lst_cadena_aux = []
    matriz_enteros = []
    for i, cadena in enumerate(lista_cadenas):
        lst_cadena_aux.append(cadena)
        if (i % tam_fila) == (tam_fila - 1):
            matriz_enteros.append(lista_cadenas_lista_enteros(lst_cadena_aux))
            lst_cadena_aux = []

    return matriz_enteros
