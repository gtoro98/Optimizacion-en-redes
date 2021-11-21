from os import close
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
from tkinter import colorchooser
from tkinter import font
from matriz import *
from djikstra import *
from grafo import*
from time import*


def create_new_window(main_window):
    new_window = Tk()

def set_color(main_window, labelTitulo, close, get_route_button):
    messagebox.showinfo(message="Seleccione un color de fondo", title= "Color de fondo")
    bgcolor = colorchooser.askcolor()
    color_hex_value = bgcolor[1]
    main_window.config(bg = color_hex_value)
    labelTitulo.config(bg = color_hex_value)
    messagebox.showinfo(message="Seleccione un color de letra", title= "Color de letra")
    fgcolor = colorchooser.askcolor()
    fg_color_hex_value = fgcolor[1]
    labelTitulo.config(fg= fg_color_hex_value)

def close_window(main_window):
    main_window.destroy()


def main_window_function():

    def get_route():
        value = combo_box.get()
        if len(value) == 0:
            messagebox.showinfo(message="⚠️Debe seleccionar un punto de encuentro⚠️", title= "Error")
        else:
            if value == "Bar La Pasión":
                node = 25
            elif value == "The Darkness":
                node = 4
            elif value == "Cervecería Mi Rolita":
                node = 2
            matriz_ad_javier = crear_matriz_javier()
            camino_mas_corto(matriz_ad_javier, node)
            reconstruir_camino(matriz_distancias, node) #Pasion: 25 / Darkness: 4 / Rolita:2
            messagebox.showinfo(message="Se ha encontrado el camino mas corto hacia: " + value + ".")

            f = open("temp.txt","r")
            string = f.read()
            string_javier = string.split("/")[0]
            string_andreina = string.split("/")[1]

            javier_label = "JAVIER debe caminar por las esquinas: [" + string_javier.split("-")[0]+"]" # javier...: 28
            for i in range(1, len(string_javier.split("-,")[0].split("-"))):
                javier_label = javier_label + " ➜ [" +string_javier.split("-,")[0].split("-")[i]+"]" 
            
            javier_label = javier_label + "\nTiempo estimado de llegada de Javier a su destino: 🕓 " + string_javier.split("-,")[1] + " min."

            labelJavierInfo.config(text=javier_label) #se llena el label con la info de Javier

            andreina_label = "Andreina debe caminar por las esquinas: [" + string_andreina.split("-")[0]+"]"          
            for i in range(1, len(string_andreina.split("-,")[0].split("-"))):
                andreina_label = andreina_label + " ➜ [" + string_andreina.split("-,")[0].split("-")[i]+"]"
            andreina_label = andreina_label + "\nTiempo estimado de llegada de Javier a su destino: 🕓 " + string_andreina.split("-,")[1] + " min."

            labelAndreinaInfo.config(text=andreina_label) #se llena el label con la info de Andreina
            
            label4_difTiempo = ""
            if int(string_andreina.split("-,")[1]) > int(string_javier.split("-,")[1]):
                label4_difTiempo = "Andreina debe salir " + str(int(string_andreina.split("-,")[1]) - int(string_javier.split("-,")[1])) + " minutos antes que Javier para llegar al mismo tiempo."
            else:
                label4_difTiempo = "Javier debe salir " + str(int(string_javier.split("-,")[1]) - int(string_andreina.split("-,")[1])) + " minutos antes que Andreina para llegar al mismo tiempo."
            
            labelTiempo.config(text=label4_difTiempo, background="light green") #se llena el label con el tiempo

            dibujarGrafo("Ambos", node)
            
    def update_time():
        time = strftime("Hora: " + "%I:%M:%S %p")
        time_label.config(text=time, background="light blue")
        time_label.after(1000,update_time)
        day = strftime("%A")
        day_label.config(text=day, background="light blue", )

    #ABRIR VENTANA MATRIZ AD JAVIER ###############################################################################  
    def openNewWindowJaviMAD():
        newWindow = Toplevel(main_window)
        newWindow.title("Matriz de adyacencia: Javier")
        newWindow.geometry("1045x780")

        matriz_ad_javier = crear_matriz_javier()
        for i in range(len(matriz_ad_javier)):
            matriz_ad_javier[i].insert(0,i)
        fila1=["",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        matriz_ad_javier.insert(0,fila1)
        
        for r in range(len(matriz_ad_javier)):
            for c in range(len(matriz_ad_javier)):
                cell = Entry(newWindow, width=3, font=("Arial",11), justify= "center")
                cell.grid(row=r, column=c)
                if c==0 or r==0:
                    cell.insert(0, '[{}]'.format((matriz_ad_javier[r][c])))
                    cell["disabledbackground"] = "grey"
                else: 
                    cell.insert(0, '{}'.format((matriz_ad_javier[r][c])))
                    if matriz_ad_javier[r][c] != 0 and r!=0 and c!=0:
                        cell["disabledbackground"] = "#63EAFC"
                    else:
                        cell["disabledbackground"] = "light grey"
                cell["disabledforeground"] = "black"
                cell["state"] = DISABLED

    #ABRIR VENTANA MATRIZ AD ANDREINA ###############################################################################  
    def openNewWindowAndreMAD():
        newWindow = Toplevel(main_window)
        newWindow.title("Matriz de adyacencia: Andreina")
        newWindow.geometry("1045x780")

        matriz_ad_javier = crear_matriz_javier()
        matriz_ad_andreina = crear_matriz_andreina(matriz_ad_javier)
        for i in range(len(matriz_ad_andreina)):
            matriz_ad_andreina[i].insert(0,i)
        fila1=["",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        matriz_ad_andreina.insert(0,fila1)

        for r in range(len(matriz_ad_andreina)):
            for c in range(len(matriz_ad_andreina)):
                cell = Entry(newWindow, width=3, font=("Arial",11), justify= "center")
                cell.grid(row=r, column=c)
                if c==0 or r==0:
                    cell.insert(0, '[{}]'.format((matriz_ad_andreina[r][c])))
                    cell["disabledbackground"] = "grey"
                else: 
                    cell.insert(0, '{}'.format((matriz_ad_andreina[r][c])))
                    if matriz_ad_andreina[r][c] != 0 and r!=0 and c!=0:
                        cell["disabledbackground"] = "#D19CE5"
                    else:
                        cell["disabledbackground"] = "light grey"
                cell["disabledforeground"] = "black"
                cell["state"] = DISABLED

    #ABRIR VENTANA MATRIZ AUXILIAR ###############################################################################  
    def openNewWindowMatrisAux():
        newWindow = Toplevel(main_window)
        newWindow.title("Estructura Auxiliar:")
        newWindow.geometry("700x700")
        newWindow.config(background="#DB6060")

        label_AUX=""
        for i in range(len(matriz_distancias)):
            label_AUX =label_AUX+str(matriz_distancias[i])+"\n"

        labelAUX = Label(newWindow,  
                    text=label_AUX, 
                    background="#DB6060", 
                    font=("Arial",12,"bold"),
                    justify="left",
                    )
        labelAUX.place(x=0, y=0)

    #DIBUJAR GRAFOS JAVIER ANDREINA #########################################################################################
    def grafoJavierDibujar():
        dibujarGrafo("Javier", 0)

    def grafoAndreinaDibujar():
        dibujarGrafo("Andreina", 0)

    #CREAR PANTALLA Y DETALLES DE LA MISMA #########################################################################################
    main_window = Tk()
    frame = Frame(main_window).place(x = 0, y = 0)
    main_window.geometry("1100x600")
    main_window.title("Ruta más corta.")
    main_window.config(background="light blue")

    icon = PhotoImage(file="logo.png")
    main_window.iconphoto(True, icon)
    
    #HORA Y FECHA CONFIGURACION #####################################################################################################
    time_label = Label(frame, font=("Arial",10), # tiempo
                        background = "light blue",
                        justify= "right")
    time_label.place(x=0,y=0)

    day_label = Label(frame, font=("Arial",10), 
                        background = "light blue",
                        justify = "right")
    day_label.place(x=0, y=20)

    update_time()

    #BOTONES ##############################################################################################################
    close = Button(frame, text="X", font=font.Font(size=15, weight='bold'), width=3, command= lambda: close_window(main_window), bg='red').pack(side=TOP, anchor=E)

    get_route_button = Button(main_window, text="Hallar ruta", command=get_route, width =20, bg='#0052cc', fg='#ffffff', font=font.Font(size=11, weight='bold')) 
    get_route_button.place(x = 350, y = 128)

    matrizJavier_button = Button(main_window, text="MatrizAD. Javier",command= openNewWindowJaviMAD,  width =13, bg='#1E5692', fg='#ffffff', font=font.Font(size=14, weight='bold')) 
    matrizJavier_button.place(x = 130, y = 450)

    matrizAndreina_button = Button(main_window, text="MatrizAD. Andre", command= openNewWindowAndreMAD, width =13, bg='#D484EB', fg='#ffffff', font=font.Font(size=14, weight='bold')) 
    matrizAndreina_button.place(x = 305, y = 450)

    matrizAuxiliar_button = Button(main_window, text="Estructura Aux", command= openNewWindowMatrisAux, width =13, bg='#C70039', fg='#ffffff', font=font.Font(size=14, weight='bold')) 
    matrizAuxiliar_button.place(x = 505, y = 450)

    grafoJavier_button = Button(main_window, text="Grafo Javier", command= grafoJavierDibujar, width =13, bg='#FF5733', fg='#ffffff', font=font.Font(size=14, weight='bold')) 
    grafoJavier_button.place(x = 705, y = 450)

    grafoAndreina_button = Button(main_window, text="Grafo Andreina", command= grafoAndreinaDibujar, width =13, bg='#900C3F', fg='#ffffff', font=font.Font(size=14, weight='bold')) 
    grafoAndreina_button.place(x = 880, y = 450)

    #LABEL TITULO ##########################################################################################################
    labelTitulo = Label(frame,  #titulo
                    text="Javier y Andreína estan enamorados 💘, pero sus padres no lo aprueban\nAyudemos a la pareja a estar juntos determinando sus rutas de encuentro.", 
                    background="light blue", 
                    font=("Arial",16,"bold"),
                    justify="center",
                    )
    labelTitulo.place(x = 140, y = 40)

    #LABEL JAVIER INFO #####################################################################################################
    labelJavierInfo = Label(frame, text="", 
                    background="light blue", 
                    font=("Arial",16,"bold"),
                    justify="left",)
    labelJavierInfo.place(x=140,y=190) 

    #LABEL ANDREINA INFO #####################################################################################################
    labelAndreinaInfo = Label(frame, text="", 
                        background="light blue", 
                        font=("Arial",16,"bold"),
                        justify="left",)
    labelAndreinaInfo.place(x=140,y=260)
   
    #LABEL TIEMPO INFO #####################################################################################################
    labelTiempo = Label(frame,text="",
                        background="light blue", 
                        font=("Arial",18,"bold italic"),
                        justify="center",)
    labelTiempo.place(x=140,y=340) 

    #DROPBOX DE OPCIONES #####################################################################################################
    labelselect = ttk.Label(text="-Seleccione un destino:", background="light blue",  font=("Arial",11,"bold"))
    labelselect.place(x = 140, y = 120)

    combo_box = ttk.Combobox(frame, width =25, font=font.Font(size=9))
    combo_box["state"] = "readonly"
    combo_box.place(x= 140, y= 140)
    combo_box["values"] = ("","Bar La Pasión","The Darkness","Cervecería Mi Rolita")
    combo_box.current(0)

    #OPCIONES BARRA DE HERRAMEINTAS #####################################################################################################
    menubar = Menu(frame)
    main_window.config(menu=menubar)

    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=file_menu)
    file_menu.add_command(label="Personalización", command= lambda: set_color(main_window, labelTitulo, close, get_route_button))
    file_menu.add_command(label="Hallar ruta", command=get_route)

    file_menu.add_separator()
    file_menu.add_command(label="Cerrar", command= lambda: close_window(main_window))

    show_map = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Mostrar mapa", menu=show_map)
    show_map.add_command(label="Bogota", command= lambda: show_map_graph)
    ######################################################################################################################################

    main_window.mainloop()
