from tkinter import INSERT, END
from vista import Ventana
from modelo import Banquero
from helpers import convertir_str_lista, convertir_str_matriz


class ControladorBanquero:
    def __init__(self):
        self.ventana = Ventana(self)
        # self.banquero = Banquero()

    def main(self):
        self.ventana.correr_ventana()

    def presionando_boton(self):
        resultado = None
        cadena_resultado = ''
        cadena_existentes = self.ventana.entrada_exitentes.get()
        cadena_solicitados = self.ventana.entrada_solicitados.get(1.0, END)
        cadena_asignados = self.ventana.entrada_asignados.get(1.0, END)

        try:
            existentes = convertir_str_lista(cadena_existentes)
            solicitados = convertir_str_matriz(
                cadena_solicitados, len(existentes))
            asignados = convertir_str_matriz(cadena_asignados, len(existentes))
            banquero = Banquero(existentes, asignados, solicitados)
            resultado = banquero.correr_banquero()

            for cadena in resultado:
                cadena_resultado += cadena
                

        except ValueError as e:
            cadena_resultado = f'Los valores de entrada deben ser enteros. Error: {e}'
            print(resultado)
        except Exception as e:
            cadena_resultado = f'Hubo un error, por favor verifique las entradas. Error {e}'
            print(resultado)
        finally:
            self.ventana.texto_resultado.delete(1.0, END)
            self.ventana.texto_resultado.insert(INSERT, cadena_resultado)


            print('/////////////////////')
            print(cadena_resultado)
