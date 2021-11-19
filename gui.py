from os import close
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os



from matriz import *
from djikstra import *

def show_map_graph():
    pass

def get_route(value):
    if len(value) == 0:
        messagebox.showinfo(message="Debe seleccionar un nodo", title= "Error")
    else:
        if value == "Pasion":
            node = 25
        elif value == "Darkness":
            node = 4
        elif value == "Rolita":
            node = 2
        matriz_ad_javier = crear_matriz_javier()
        camino_mas_corto(matriz_ad_javier, node)
        reconstruir_camino(matriz_distancias, node) #Pasion: 25 / Darkness: 4 / Rolita:2
        messagebox.showinfo(message="Se ha encontrado el camino mas corto hacia: " + value + ".")


def get_selection(combo_box):
    value = combo_box.get()
    get_route(value)


def close_window():
    main_window.destroy()


def main_window():

    main_window = Tk()

    frame = Frame(main_window).place(x = 0, y = 0)

    main_window.geometry("800x500")
    main_window.title("Ruta más corta.")
    main_window.config(background="light grey")

    icon = PhotoImage(file="logo.png")
    main_window.iconphoto(True, icon)

    label1 = Label(frame, 
                    text="Bienvenidos Javier y Andreína\nPara comenzar, por favor ingresen su lugar de encuentro.", 
                    background="light grey", 
                    font=("Arial",14,"bold"),
                    justify="center",
                    )
    label1.place(x = 140, y = 50)

    close = Button(frame, text="Cancelar", command= close_window).place(x = 150, y = 400)

    combo_box = ttk.Combobox(frame)
    combo_box["state"] = "readonly"
    combo_box.place(x= 140, y= 200)
    combo_box["values"] = ("Rolita", "Darkness", "Pasion")

    menubar = Menu(frame)
    main_window.config(menu=menubar)

    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=file_menu)
    file_menu.add_command(label="Personalización")
    file_menu.add_command(label="Hallar ruta", command= lambda: get_selection(combo_box))
    file_menu.add_separator()
    file_menu.add_command(label="Cerrar", command=close_window)

    show_map = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Mostrar mapa", menu=show_map)
    show_map.add_command(label="Bogota", command= lambda: show_map_graph)
    

    get_route_button = Button(main_window, text="Hallar ruta", command= lambda: get_selection(combo_box))
    get_route_button.place(x = 210, y = 400)

    main_window.mainloop()