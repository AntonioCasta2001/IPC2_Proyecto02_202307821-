from graphviz import Digraph

def visualizar_turnos(lista):
    dot = Digraph()
    turnos = lista.obtener_turnos()
    for i, turno in enumerate(turnos):
        label = f"{turno.nombre}\n{turno.especialidad}\nAtención: {turno.tiempo_atencion} min\nEspera: {turno.tiempo_espera} min"
        dot.node(str(i), label)
        if i > 0:
            dot.edge(str(i-1), str(i))
    dot.render("cola_turnos", format="png", cleanup=True)