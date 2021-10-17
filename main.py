from modelo import Banquero
from vista import Ventana

def main():
    # # existentes = [6,3,4,2]
    # # asignados = [
    # #     [3,0,1,1],
    # #     [0,1,0,0],
    # #     [1,1,1,0],
    # #     [1,1,0,1],
    # #     [0,0,0,0]
    # # ]

    # # solicitados = [
    # #     [1,1,0,0],
    # #     [0,1,1,2],
    # #     [3,1,0,0],
    # #     [0,0,1,0],
    # #     [2,1,1,0]
    # # ]

    # existentes = [4,2,3,1]
    # asignados = [
    #     [0,0,1,0],
    #     [2,0,0,1],
    #     [0,1,2,0]
    # ]

    # solicitados = [
    #     [2,0,0,1],
    #     [1,0,1,0],
    #     [2,1,0,0]
    # ]


    # banquero = Banquero(existentes, asignados, solicitados)
    # print(banquero.correr_banquero())

    ventana = Ventana()
    ventana.mainloop()

if __name__ == '__main__':
    main()