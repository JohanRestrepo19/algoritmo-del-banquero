import tkinter as tk
from tkinter import ttk

class Ventana(tk.Tk):
    def __init__(self, controlador, master=None):
        tk.Tk.__init__(self, master)
        self.controlador = controlador
        self.title('Ejemplo de ventana')
        self.resizable(False, False)
        self.__crear_marco_principal()
        self.__crear_widgets()

    def correr_ventana(self):
        self.mainloop()

    def __crear_marco_principal(self):
        self.marco_principal = ttk.Frame(self)
        self.marco_principal.pack(padx=10, pady=10)

    def __crear_widgets(self):
        self.__crear_widgets_existentes()
        self.__crar_widgets_matrices()
        self.__crear_widgets_botones()
        self.__crear_widgets_resultado()

    def __crear_widgets_existentes(self):
        marco_existentes = ttk.LabelFrame(self.marco_principal)
        marco_existentes.pack(padx=5, pady=5)

        etiqueta_exitentes = ttk.Label(marco_existentes, text='Rescursos existentes')
        etiqueta_exitentes.grid(row=0, column=0)
        self.entrada_exitentes = ttk.Entry(marco_existentes)
        self.entrada_exitentes.grid(row=1, column=0)

    def __crar_widgets_matrices(self):
        marco_matrices = ttk.LabelFrame(self.marco_principal)
        marco_matrices.pack(padx=5, pady=5)

        etiqueta_asignados = ttk.Label(marco_matrices, text='Recursos asignados')
        etiqueta_asignados.grid(row=0, column=0)
        self.entrada_asignados = tk.Text(
            marco_matrices, 
            height=4,
            width=20,
            )
        self.entrada_asignados.grid(row=1, column=0)

        etiqueta_solicitados = ttk.Label(marco_matrices, text='Recursos solicitados')
        etiqueta_solicitados.grid(row=0, column=1)
        self.entrada_solicitados = tk.Text(
            marco_matrices, 
            height=4,
            width=20,
            )
        self.entrada_solicitados.grid(row=1, column=1)

    def __crear_widgets_botones(self):
        marco_botones = ttk.LabelFrame(self.marco_principal)
        marco_botones.pack(padx=5, pady=5)
        boton_correr = ttk.Button(
            marco_botones, 
            text='Correr',
            command = self.controlador.presionando_boton
            )
        boton_correr.grid(row=0, column=0)

    def __crear_widgets_resultado(self):
        marco_resultado = ttk.LabelFrame(self.marco_principal)
        marco_resultado.pack(padx=5, pady=5)

        self.texto_resultado = tk.Text(
            marco_resultado,
            height=10,
            width=70,
            # state='disabled'
            )

        self.texto_resultado.grid(row=0, column=0)

