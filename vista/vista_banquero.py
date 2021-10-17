import tkinter as tk

class Ventana(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.master.title('Ejemplo de ventana')
        self.crear_widgets()

    def crear_widgets(self):
        self.boton_salida = tk.Button(self, text='Quit', command=self.quit).grid(row=0, column=1)
        self.lbl_existentes = tk.Label(self, text='Rescursos existentes').grid(row=0, column=0)