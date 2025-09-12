from collections import deque

TIEMPOS_ESPECIALIDAD = {
    "Medicina General": 10,
    "Pediatría": 15,
    "Ginecología": 20,
    "Dermatología": 25
}

class Turno:
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.tiempo_atencion = TIEMPOS_ESPECIALIDAD[especialidad]

class GestorTurnos:
    def __init__(self):
        self.cola = deque()

    def registrar_turno(self, nombre, edad, especialidad):
        turno = Turno(nombre, edad, especialidad)
        self.cola.append(turno)

    def atender_turno(self):
        if self.cola:
            return self.cola.popleft()
        return None

    def calcular_tiempo_espera(self):
        total = 0
        tiempos = []
        for turno in self.cola:
            tiempos.append(total)
            total += turno.tiempo_atencion
        return tiempos

    def obtener_cola(self):
        return list(self.cola)
