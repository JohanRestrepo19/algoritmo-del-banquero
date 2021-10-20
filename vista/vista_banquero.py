import tkinter as tk

class Ventana(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.master.title('Ejemplo de ventana')
        # self.master.geometry("400x400")
        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta_exitentes = tk.Label(self, text='Rescursos existentes').grid(row=0, column=0, columnspan=2)
        self.entrada_exitentes = tk.Entry(self).grid(row=1, column=0, columnspan=2)

        self.etiqueta_asignados = tk.Label(self, text='Recursos asignados').grid(row=2, column=0)
        self.entrada_asignados = tk.Entry(self).grid(row=3, column=0)

        self.etiqueta_solicitados = tk.Label(self, text='Recursos solicitados').grid(row=2, column=1)
        self.entrada_solicitados = tk.Entry(self).grid(row=3, column=1)

        self.boton_correr = tk.Button(text='Correr').grid(row=4, column=0)
        self.boton_Ayuda = tk.Button(text='Ayuda').grid(row=4, column=1)

        self.texto_resultado = tk.Text(self, height=2, width=50).grid(row=5, columnspan=2)