from controlador import ControladorBanquero


def main() -> None:
    controlador = ControladorBanquero()
    controlador.main()
    # ls_estados = []
    # recursos_existentes = [6,3,4,2]
    # recursos_poseidos = [4,2,2,1]
    # recursos_disponibles = [2,1,2,1]
    # procesos_terminados = [False,False,False,True,False]

    # msg = (
    #     f'recursos existentes: {recursos_existentes}\n'
    #     f'recursos poseidos:   {recursos_poseidos}\n'
    #     f'recursos disponibles:{recursos_disponibles}\n'
    #     f'procesos terminados: {procesos_terminados}\n'
    #     f'---------------------------------------------'
    # )

    # ls_estados.append(msg)

    # recursos_existentes = [5,1,1,1]
    # recursos_poseidos = [1,1,1,1]
    # recursos_disponibles = [1,1,1,1]
    # procesos_terminados = [True,True,True,True,True]

    # msg = (
    #     f'recursos existentes: {recursos_existentes}\n'
    #     f'recursos poseidos:   {recursos_poseidos}\n'
    #     f'recursos disponibles:{recursos_disponibles}\n'
    #     f'procesos terminados: {procesos_terminados}\n'
    #     f'---------------------------------------------\n'
    # )

    # ls_estados.append(msg)

    # cadena = ''

    # for msg in ls_estados:
    #     cadena += msg
    
    # print(cadena)



'''
registro_estados
'''

if __name__ == '__main__':
    main()
