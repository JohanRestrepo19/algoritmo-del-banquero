def suma_listas(lista1, lista2):
    resultado = []
    acc = 0
    for i in range(len(lista1)):
        acc = lista1[i] + lista2[i]
        resultado.append(acc)
    return resultado

def resta_listas(lista1, lista2):
    resultado = []
    acc = 0
    for i in range(len(lista1)):
        acc = lista1[i] - lista2[i]
        resultado.append(acc)
    return resultado

def imprimir_matriz(matriz):
    for lista in matriz:
        print(lista)


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

    def __init__(self, existentes, asignados, solicitados):
        self.existentes = existentes
        self.asignados = asignados
        self.solicitados = solicitados
        self.acabado = [False for x in range(len(self.asignados))]
        self.poseidos = self.calcular_recursos_poseidos()
        self.disponibles = self.calcular_disonibles()

    def correr_banquero(self):
        while not self.procesos_despachados():
            solicitud_recursos = self.buscar_solicitud()
            if solicitud_recursos == None:
                return f'El estado inicial no es seguro'
            
            self.iterar(solicitud_recursos)

        return f'El estado inicial es seguro'


    def procesos_despachados(self):
        return all(self.acabado)

    def buscar_solicitud(self):
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
            
            if existe_solictud != None:
                return existe_solictud

        return existe_solictud

    def iterar(self, solicitud_proceso):
        index = self.solicitados.index(solicitud_proceso)
        
        self.asignados[index] = suma_listas(self.asignados[index], solicitud_proceso)
        self.poseidos = self.calcular_recursos_poseidos()
        self.disponibles = resta_listas(self.existentes, self.poseidos)
        self.imprimir_estado()
        self.disponibles = suma_listas(self.disponibles, self.asignados[index])
        self.acabado[index] = True
        self.poseidos = self.calcular_recursos_poseidos()
        self.asignados[index] = ['x' for x in self.asignados]
        self.solicitados[index] = ['x' for x in self.solicitados]
        self.imprimir_estado()



    def calcular_recursos_poseidos(self):
        poseidos = [0 for x in range(len(self.existentes))]

        for j, proceso in enumerate(self.asignados):
            if self.acabado[j]:
                continue

            for i, recurso in enumerate(proceso):
                poseidos[i] += recurso

        return poseidos

    def calcular_disonibles(self):
        disponibles = [0 for x in range(len(self.existentes))]
        for i, recurso_existente in enumerate(self.existentes):
            disponibles[i] = recurso_existente - self.poseidos[i] 

        return disponibles

    
    def imprimir_estado(self):
        print('=============================================')
        print(f'Recursos existentes:     {self.existentes}')
        print(f'Recursos poseidos:       {self.poseidos}')
        print(f'Recursos disponibles:    {self.disponibles}')
        print()
        print(f'Procesos terminados:     {self.acabado}')
        print()
        print(f'Recursos asignados')
        imprimir_matriz(self.asignados)
        print()
        print(f'Recursos solicitados')
        imprimir_matriz(self.solicitados)
        print('=============================================')


if __name__ == '__main__':
    # existentes = [6,3,4,2]
    # asignados = [
    #     [3,0,1,1],
    #     [0,1,0,0],
    #     [1,1,1,0],
    #     [1,1,0,1],
    #     [0,0,0,0]
    # ]

    # solicitados = [
    #     [1,1,0,0],
    #     [0,1,1,2],
    #     [3,1,0,0],
    #     [0,0,1,0],
    #     [2,1,1,0]
    # ]

    existentes = [4,2,3,1]
    asignados = [
        [0,0,1,0],
        [2,0,0,1],
        [0,1,2,0]
    ]

    solicitados = [
        [2,0,0,1],
        [1,0,1,0],
        [2,1,0,0]
    ]


    banquero = Banquero(existentes, asignados, solicitados)
    print(banquero.correr_banquero())