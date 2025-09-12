import tkinter as tk
from tkinter import ttk, messagebox
from turnos import GestorTurnos, TIEMPOS_ESPECIALIDAD
from grafos import generar_grafico_cola

gestor = GestorTurnos()

def registrar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    especialidad = combo_especialidad.get()
    if nombre and edad and especialidad:
        gestor.registrar_turno(nombre, int(edad), especialidad)
        actualizar_cola()
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")

def atender():
    turno = gestor.atender_turno()
    if turno:
        messagebox.showinfo("Paciente Atendido", f"Nombre: {turno.nombre}\nEdad: {turno.edad}\nEspecialidad: {turno.especialidad}\nTiempo atención: {turno.tiempo_atencion} min")
        actualizar_cola()
    else:
        messagebox.showinfo("Sin turnos", "No hay pacientes en espera.")

def actualizar_cola():
    lista.delete(0, tk.END)
    tiempos = gestor.calcular_tiempo_espera()
    for i, turno in enumerate(gestor.obtener_cola()):
        lista.insert(tk.END, f"{turno.nombre} ({turno.especialidad}) - Espera: {tiempos[i]} min")
    generar_grafico_cola(gestor.obtener_cola())

root = tk.Tk()
root.title("Gestión de Turnos Médicos")

tk.Label(root, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Edad:").grid(row=1, column=0)
entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1)

tk.Label(root, text="Especialidad:").grid(row=2, column=0)
combo_especialidad = ttk.Combobox(root, values=list(TIEMPOS_ESPECIALIDAD.keys()))
combo_especialidad.grid(row=2, column=1)

tk.Button(root, text="Registrar Turno", command=registrar).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Atender Paciente", command=atender).grid(row=4, column=0, columnspan=2)

lista = tk.Listbox(root, width=50)
lista.grid(row=5, column=0, columnspan=2)

root.mainloop()
