
from os import close
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
from tkinter import colorchooser
from matriz import *
from djikstra import *
from time import*


def create_new_window(main_window):
    new_window = Tk()

def set_color(main_window, label1, close, get_route_button):
    messagebox.showinfo(message="Seleccione un color de fondo", title= "Color de fondo")
    bgcolor = colorchooser.askcolor()
    color_hex_value = bgcolor[1]
    main_window.config(bg = color_hex_value)
    label1.config(bg = color_hex_value)
    messagebox.showinfo(message="Seleccione un color de letra", title= "Color de letra")
    fgcolor = colorchooser.askcolor()
    fg_color_hex_value = fgcolor[1]
    label1.config(fg= fg_color_hex_value)


def show_map_graph():
    pass

#def get_route(value, main_window):
#    if len(value) == 0:
#        messagebox.showinfo(message="Debe seleccionar un nodo", title= "Error")
#    else:
#        if value == "Pasion":
#            node = 25
#        elif value == "Darkness":
#            node = 4
#        elif value == "Rolita":
#            node = 2
#        matriz_ad_javier = crear_matriz_javier()
#        camino_mas_corto(matriz_ad_javier, node)
#        reconstruir_camino(matriz_distancias, node) #Pasion: 25 / Darkness: 4 / Rolita:2
#        messagebox.showinfo(message="Se ha encontrado el camino mas corto hacia: " + value + ".")
#        create_new_window(main_window)


#def get_selection(combo_box, main_window):
 #   value = combo_box.get()
  #  get_route(value, main_window)


def close_window(main_window):
    main_window.destroy()


def main_window_function():


    


    def get_route():
        value = combo_box.get()
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

            f = open("temp.txt","r")
            string = f.read()
            string_javier = string.split("/")[0]
            string_andreina = string.split("/")[1]

            javier_label = "Javier debe caminar por las esquinas: " + string_javier.split("-")[0] 
            for i in range(1, len(string_javier.split("-,")[0].split("-"))):
                javier_label = javier_label + " -> " + string_javier.split("-,")[0].split("-")[i] 
            
            javier_label = javier_label + "\nEl tiempo estimado de llegada de Javier es de: " + string_javier.split("-,")[1] + " minutos."

            label2 = Label(frame, text=javier_label, 
                            background="light grey", 
                            font=("Arial",11,"bold"),
                            justify="center",).place(x=140,y=100) 

            andreina_label = "Andreina debe caminar por las esquinas: " + string_andreina.split("-")[0]          
            for i in range(1, len(string_andreina.split("-,")[0].split("-"))):
                andreina_label = andreina_label + " -> " + string_andreina.split("-,")[0].split("-")[i] 
            andreina_label = andreina_label + "\nEl tiempo estimado de llegada de Andreina es de: " + string_andreina.split("-,")[1] + " minutos."
            label3 = Label(frame, text=andreina_label, 
                            background="light grey", 
                            font=("Arial",11,"bold"),
                            justify="center",).place(x=140,y=170)

            label4_string = ""


            if int(string_andreina.split("-,")[1]) > int(string_javier.split("-,")[1]):
                label4_string = "Andreina debe salir " + str(int(string_andreina.split("-,")[1]) - int(string_javier.split("-,")[1])) + " minutos antes que Javier."
            else:
                label4_string = "Javier debe salir " + str(int(string_javier.split("-,")[1]) - int(string_andreina.split("-,")[1])) + " minutos antes que Andreina."
            
            label4 = Label(frame,
                            text=label4_string,
                            background="light grey", 
                            font=("Arial",11,"bold"),
                            justify="center",).place(x=140,y=300) 
    def update_time():
        time = strftime("Hora: " + "%I:%M:%S %p")
        time_label.config(text=time)
        time_label.after(1000,update_time)
        day = strftime("%A")
        day_label.config(text=day)

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

    time_label = Label(frame, font=("Arial",10), 
                        background = "light grey",
                        justify= "right")
    time_label.place(x=470,y=0)

    day_label = Label(frame, font=("Arial",10), 
                        background = "light grey",
                        justify = "right")
    day_label.place(x=470, y=20)
    update_time()
    
                        
    close = Button(frame, text="Cancelar", command= lambda: close_window(main_window)).place(x = 150, y = 400)

    combo_box = ttk.Combobox(frame)
    combo_box["state"] = "readonly"
    combo_box.place(x= 140, y= 200)
    combo_box["values"] = ("","Rolita", "Darkness", "Pasion")
    combo_box.current(0)

    menubar = Menu(frame)
    main_window.config(menu=menubar)

    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=file_menu)
    file_menu.add_command(label="Personalización", command= lambda: set_color(main_window, label1, close, get_route_button))
    file_menu.add_command(label="Hallar ruta", command=get_route)

    file_menu.add_separator()
    file_menu.add_command(label="Cerrar", command= lambda: close_window(main_window))

    show_map = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Mostrar mapa", menu=show_map)
    show_map.add_command(label="Bogota", command= lambda: show_map_graph)
    

    #get_route_button = Button(main_window, text="Hallar ruta", command= lambda: get_selection(combo_box, main_window))
    get_route_button = Button(main_window, text="Hallar ruta", command=get_route)
    get_route_button.place(x = 210, y = 400)


    main_window.mainloop()