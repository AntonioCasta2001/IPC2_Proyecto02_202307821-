import tkinter as tk
from tkinter import ttk, messagebox
from turnos import ListaTurnos, Turno, tiempos_espera
from grafos import visualizar_turnos
from PIL import Image, ImageTk

class MenuListaTurnos:
    def __init__(self, root):
        self.lista = ListaTurnos()
        self.root = root
        self.root.title("Gestión de Turnos Médicos")
        self.root.geometry("600x400+560+240")
        tk.Label(root, text="Nombre", anchor="center",width=20, bg="white").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Edad", anchor="center", bg="white").grid(row=1, column=0)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=1, column=1)

        tk.Label(root, text="Especialidad", anchor="center", bg="white").grid(row=2, column=0)
        self.especialidad_combo = ttk.Combobox(root, values=list(tiempos_espera.keys()))
        self.especialidad_combo.grid(row=2, column=1)
        
        
        tk.Button(root, text="Registrar Turno", command=self.registrar_turno, bg="yellow").grid(row=3, column=3, columnspan=2)
        tk.Button(root, text="Atender Turno", command=self.atender_turno, bg="red").grid(row=4, column=3, columnspan=2)
        self.tree = ttk.Treeview(root, columns=("Nombre", "Edad", "Especialidad", "Tiempo"), show="headings")
        self.tree.grid(row=6, column=0, columnspan=2)
        for col in ("Nombre", "Edad", "Especialidad", "Tiempo"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.canvas = tk.Label(root)
        self.canvas.grid(row=5, column=3, columnspan=2)

    def registrar_turno(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        especialidad = self.especialidad_combo.get()

        if not nombre or not edad or not especialidad:
            messagebox.showwarning("Campos incompletos")
            return

        turno = Turno(nombre, int(edad), especialidad)
        self.lista.agregar_turno(turno)
        self.actualizar_visualizacion()
        self.lista.agregar_turno(turno)
        self.actualizar_lista_pacientes()

    def atender_turno(self):
        turno = self.lista.atender_turno()
        if turno:
            msg = f"Atendiendo a {turno.nombre} ({turno.edad} años)  en la especialidad {turno.especialidad}\n"
            msg += f"Tiempo de atencion: {turno.tiempo_atencion} min\n Tiempo de espera: {turno.tiempo_espera} min"
            messagebox.showinfo("Turno Atendido", msg)
        else:
            messagebox.showinfo("Sin turnos", "No hay turnos pendientes.")
        self.actualizar_visualizacion()
        self.actualizar_lista_pacientes()

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
    def actualizar_lista_pacientes(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for turno in self.lista.obtener_turnos():
            self.tree.insert("", "end", values=(
                turno.nombre,
                turno.edad,
                turno.especialidad,
                f"{turno.tiempo_atencion} min",
                f"{turno.tiempo_espera} min"
            ))
