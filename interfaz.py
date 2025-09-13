import tkinter as tk
from tkinter import ttk, messagebox
from turnos import ListaTurnos, Turno, tiempos_espera
from grafos import visualizar_turnos
from PIL import Image, ImageTk

class AppTurnos:
    def __init__(self, root):
        self.lista = ListaTurnos()
        self.root = root
        self.root.title("Gestión de Turnos Médicos")

        # Entradas
        tk.Label(root, text="Nombre").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(root, text="Edad").grid(row=1, column=0)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=1, column=1)

        tk.Label(root, text="Especialidad").grid(row=2, column=0)
        self.especialidad_combo = ttk.Combobox(root, values=list(tiempos_espera.keys()))
        self.especialidad_combo.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Registrar Turno", command=self.registrar_turno).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Atender Turno", command=self.atender_turno).grid(row=4, column=0, columnspan=2)

        # Imagen Graphviz
        self.canvas = tk.Label(root)
        self.canvas.grid(row=5, column=0, columnspan=2)

    def registrar_turno(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        especialidad = self.especialidad_combo.get()

        if not nombre or not edad or not especialidad:
            messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos.")
            return

        turno = Turno(nombre, int(edad), especialidad)
        self.lista.agregar_turno(turno)
        self.actualizar_visualizacion()

    def atender_turno(self):
        turno = self.lista.atender_turno()
        if turno:
            msg = f"Atendiendo a {turno.nombre} ({turno.edad}) - {turno.especialidad}\n"
            msg += f"⏱ Atención: {turno.tiempo_atencion} min\n⏳ Espera previa: {turno.tiempo_espera} min"
            messagebox.showinfo("Turno Atendido", msg)
        else:
            messagebox.showinfo("Sin turnos", "No hay turnos pendientes.")
        self.actualizar_visualizacion()

    def actualizar_visualizacion(self):
        visualizar_turnos(self.lista)
        try:
            img = Image.open("cola_turnos.png")
            img = img.resize((400, 300), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            self.canvas.configure(image=photo)
            self.canvas.image = photo
        except:
            pass