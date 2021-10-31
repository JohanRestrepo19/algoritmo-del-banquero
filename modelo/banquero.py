from helpers import *


class Banquero():
    '''
    m --> cantidad de recursos
    n --> cantidad de procesos

    self.disponibles = [m]   --> lista de tamaño m
    self.asignados = [n, m] --> matriz de n(procesos) filas por m(recursos) columnas que representa los
                                los recursos asignados a cada proceso
    self.solicitados = [n, m] --> matriz de n(procesos) filas por m(recursos) columnas que representa los
                                los recursos solicitados por cada proceso 
    '''

    def __init__(self, existentes: list, asignados: list, solicitados: list):
        self.existentes = existentes
        self.asignados = asignados
        self.solicitados = solicitados
        self.acabado = [False for x in range(len(self.asignados))]
        self.poseidos = self.calcular_recursos_poseidos()
        self.disponibles = self.calcular_disonibles()
        self.ls_estados = []

    def correr_banquero(self) -> str:
        while not self.procesos_despachados():
            solicitud_recursos = self.buscar_solicitud()
            if solicitud_recursos is None:
                return 'El estado inicial no es seguro'

            self.iterar(solicitud_recursos)

        # return 'El estado inicial es seguro'
        return self.ls_estados

    def procesos_despachados(self) -> bool:
        return all(self.acabado)

    def buscar_solicitud(self) -> list | None:
        # buscar en la matriz de solicitudes un proceso que sus recursos sea menor o igual que el vector
        # de recursos disponibles
        existe_solictud = None

        # se itera a través de las solicitudes de los procesos
        for j, solicitud in enumerate(self.solicitados):
            if self.acabado[j]:
                continue

            for i, recurso in enumerate(solicitud):
                if recurso > self.disponibles[i]:
                    break

                if i == len(solicitud) - 1:
                    existe_solictud = solicitud

            if existe_solictud is not None:
                return existe_solictud

        return existe_solictud

    def iterar(self, solicitud_proceso: list) -> None:
        index = self.solicitados.index(solicitud_proceso)

        self.asignados[index] = suma_listas(
            self.asignados[index], solicitud_proceso)
        self.poseidos = self.calcular_recursos_poseidos()
        self.disponibles = resta_listas(self.existentes, self.poseidos)
        self.disponibles = suma_listas(self.disponibles, self.asignados[index])
        self.acabado[index] = True
        self.poseidos = self.calcular_recursos_poseidos()
        self.asignados[index] = ['x' for x in self.asignados]
        self.solicitados[index] = ['x' for x in self.solicitados]
        self.ls_estados.append(self.guardar_estado(index + 1))
        self.imprimir_estado()

    def guardar_estado(self, recurso_despachado: int) -> str:
        return (
            f'Recursos existentes: {self.existentes}\n'
            f'Recursos poseidos:   {self.poseidos}\n'
            f'Recursos disponibles:{self.disponibles}\n'
            f'Recurso despachado:  {recurso_despachado}\n'
            f'Procesos terminados: {self.acabado}\n'
            f'---------------------------------------------\n'
        )

    def calcular_recursos_poseidos(self) -> list:
        poseidos = [0 for x in range(len(self.existentes))]

        for j, proceso in enumerate(self.asignados):
            if self.acabado[j]:
                continue

            for i, recurso in enumerate(proceso):
                poseidos[i] += recurso

        return poseidos

    def calcular_disonibles(self) -> list:
        disponibles = [0 for x in range(len(self.existentes))]
        for i, recurso_existente in enumerate(self.existentes):
            disponibles[i] = recurso_existente - self.poseidos[i]

        return disponibles

    def imprimir_estado(self) -> None:
        print('=============================================')
        print(f'Recursos existentes:     {self.existentes}')
        print(f'Recursos poseidos:       {self.poseidos}')
        print(f'Recursos disponibles:    {self.disponibles}')
        print()
        print(f'Procesos terminados:     {self.acabado}')
        print()
        print('Recursos asignados')
        imprimir_matriz(self.asignados)
        print()
        print('Recursos solicitados')
        imprimir_matriz(self.solicitados)
        print('=============================================')
