import tkinter as tk
from tkinter import ttk

class Ventana(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.title('Ejemplo de ventana')
        self.resizable(False, False)
        self.cadena_existentes = tk.StringVar()
        self.cadena_asignados = tk.StringVar()
        self.cadena_solicitados = tk.StringVar()
        self.__crear_marco_principal()
        self.__crear_widgets()
        self.mainloop()

    def __crear_marco_principal(self):
        self.marco_principal = ttk.Frame(self)
        self.marco_principal.pack(padx=10, pady=10)

    def __crear_widgets_existentes(self):
        marco_existentes = ttk.LabelFrame(self.marco_principal)
        marco_existentes.pack(padx=5, pady=5)

        etiqueta_exitentes = ttk.Label(marco_existentes, text='Rescursos existentes')
        etiqueta_exitentes.grid(row=0, column=0)
        entrada_exitentes = ttk.Entry(marco_existentes, textvariable=self.cadena_existentes)
        entrada_exitentes.grid(row=1, column=0)

    def __crar_widgets_matrices(self):
        marco_matrices = ttk.LabelFrame(self.marco_principal)
        marco_matrices.pack(padx=5, pady=5)

        etiqueta_asignados = ttk.Label(marco_matrices, text='Recursos asignados')
        etiqueta_asignados.grid(row=0, column=0)
        entrada_asignados = ttk.Entry(marco_matrices, textvariable=self.cadena_asignados)
        entrada_asignados.grid(row=1, column=0)

        etiqueta_solicitados = ttk.Label(marco_matrices, text='Recursos solicitados')
        etiqueta_solicitados.grid(row=0, column=1)
        entrada_solicitados = ttk.Entry(marco_matrices, textvariable=self.cadena_solicitados)
        entrada_solicitados.grid(row=1, column=1)

    def __crear_widgets_botones(self):
        marco_botones = ttk.LabelFrame(self.marco_principal)
        marco_botones.pack(padx=5, pady=5)
        boton_correr = ttk.Button(marco_botones, text='Correr')
        boton_correr.grid(row=0, column=0)

    def __crear_widgets_resultado(self):
        marco_resultado = ttk.LabelFrame(self.marco_principal)
        marco_resultado.pack(padx=5, pady=5)

        texto_resultado = tk.Text(
            marco_resultado,
            height=2,
            width=50,
            state='disabled'
            )

        texto_resultado.grid(row=0, column=0)

    def __crear_widgets(self):
        self.__crear_widgets_existentes()
        self.__crar_widgets_matrices()
        self.__crear_widgets_botones()
        self.__crear_widgets_resultado()
