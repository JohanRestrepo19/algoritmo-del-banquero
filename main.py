from controlador import ControladorBanquero
from helpers import convertir_str_lista, convertir_str_matriz, imprimir_matriz



def main() -> None:
    controlador = ControladorBanquero()
    controlador.main()
    # str = '3 0 1 1 0 1 0 0 1 1 1 0 1 1 0 1 0 0 0 0'
    # try:
    #     imprimir_matriz(convertir_str_matriz(str, 4))
    # except ValueError as e:
    #     print(f'Hubo un error: {e}')
    # finally:
    #     print(str)
        


if __name__ == '__main__':
    main()