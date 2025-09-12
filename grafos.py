from graphviz import Digraph

def generar_grafico_cola(cola):
    dot = Digraph(comment='Cola de Turnos')
    for i, turno in enumerate(cola):
        label = f"{turno.nombre}\n{turno.especialidad}"
        dot.node(str(i), label)
        if i > 0:
            dot.edge(str(i-1), str(i))
    dot.render('cola_turnos', format='png', cleanup=True)
