
tiempos_espera = {
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
        self.tiempo_atencion = tiempos_espera.get(especialidad, 10)
        self.tiempo_espera = 0

class NodoTurno:
    def __init__(self, turno, siguiente= None):
        self.turno = turno
        self.siguiente = siguiente

class ListaTurnos:
    def __init__(self):
        self.primero = None

    def agregar_turno(self, turno):
        nuevo = NodoTurno(turno)
        if not self.primero:
            self.primero = nuevo
        else:
            actual = self.primero
            inicial = 0
            while actual.siguiente:
                inicial += actual.turno.tiempo_atencion
                actual = actual.siguiente
            inicial += actual.turno.tiempo_atencion
            turno.tiempo_espera = inicial
            actual.siguiente = nuevo

    def atender_turno(self):
        if not self.primero:
            return None
        atendido = self.primero.turno
        self.primero = self.primero.siguiente
        return atendido

    def obtener_turnos(self):
        turnos = []
        actual = self.primero
        while actual:
            turnos.append(actual.turno)
            actual = actual.siguiente
        return turnos
    
    def calcular_tiempo_espera(self):
        total = 0
        tiempos = []
        for turno in self.turno:
            tiempos.append(total)
            total += turno.tiempo_atencion
        return tiempos
