from vista import Ventana
from modelo import Banquero
from tkinter import INSERT, END

class ControladorBanquero:
    def __init__(self):
        self.ventana = Ventana(self)
        # self.banquero = Banquero()

    def main(self):
        self.ventana.correr_ventana()

    def presionando_boton(self):
        self.ventana.texto_resultado.delete(1.0, END)
        
        self.ventana.texto_resultado.insert(INSERT, self.ventana.cadena_existentes.get())
        
    





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

