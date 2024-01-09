from tkinter import *
from PIL import Image, ImageTk
import json
import VentanaMainPOO
import pygame
import os


def reproducir_audio(audio):
    pygame.mixer.init()
    # Reemplaza con la ruta de tu archivo de audio
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()


def show_info(title_var, data, info_display, *args):
    selected_title = title_var.get()

    # Buscar el diccionario correspondiente al título seleccionado
    selected_dict = next(
        item for item in data if item["titulo"] == selected_title)

    # Mostrar la información en el widget Text
    info_display.delete(1.0, END)  # Borra el contenido actual
    info_display.insert(END, f"{selected_dict['descripcion']}")


def eliminar_sueno(title_var, data, title_menu, info_display, audio):
    if title_var.get() != 'Welcome':
        reproducir_audio(audio)
        selected_title = title_var.get()

        # Eliminar el diccionario correspondiente al título seleccionado
        data[:] = [item for item in data if item["titulo"] != selected_title]

        # Actualizar el menú desplegable con los nuevos títulos
        titles = [item["titulo"] for item in data]
        # Borra todas las opciones actuales
        title_menu["menu"].delete(0, "end")
        for title in titles:
            title_menu["menu"].add_command(
                label=title, command=lambda t=title: title_var.set(t))

        # Borra la información en el widget Text
        info_display.delete(1.0, END)

        # Escribir los datos actualizados en el archivo "datos.json"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_datos = os.path.join(current_dir, 'datos.json')
        
        with open(ruta_datos, 'w') as archivo_json:
            json.dump(data, archivo_json, indent=2)


def salir(root, audio):
    reproducir_audio(audio)
    root.destroy()
    VentanaMainPOO.crear_ventana()


def crear_ventana():
    root = Tk()
    root.title("DreamApp :)")
    root.resizable(width=False, height=False)

    # Cargar la imagen
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(current_dir, 'background_angel_2.png')
    ruta_icono = os.path.join(current_dir, 'icon_dreamapp.ico')
    ruta_datos = os.path.join(current_dir, 'datos.json')
    ruta_sonido_eliminar = os.path.join(current_dir, 'takeover - glitch fx 7.wav')
    ruta_sonido_exit = os.path.join(current_dir, 'takeover - glitch fx 8.wav')
    
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 500), Image.LANCZOS)
    imagen = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen
    label_imagen = Label(root, image=imagen)
    label_imagen.pack()

    # Crear widgets
    boton_exit = Button(root, text="Exit", command=lambda: salir(
        root, ruta_sonido_exit))
    boton_eliminar = Button(root, text="Delete Trauma", command=lambda: eliminar_sueno(
        title_var, data, title_menu, info_display, ruta_sonido_eliminar))

    # Variables
    title_var = StringVar()
    title_var.set("Dreams")  # Valor inicial

    # Cargar datos de los sueños uwu
    with open(ruta_datos) as archivo_json:
        data = json.load(archivo_json)

    # Cargar datos al menú desplegable
    titles = [item["titulo"] for item in data]

    # Crear el menú desplegable
    title_menu = OptionMenu(root, title_var, *titles)
    title_menu.config(width=20)  # Ajusta el ancho según tus necesidades

    # Configurar el rastreador para la variable de control
    title_var.trace_add(
        "write", lambda *args: show_info(title_var, data, info_display, *args))

    # Crear el widget Text para mostrar la información
    info_display = Text(root, wrap=WORD, width=40, height=10)
    info_display.place(relx=0.50, rely=0.50, anchor=CENTER)

    # Colocar widgets
    boton_exit.place(relx=0.08, rely=0.9, anchor=CENTER)
    boton_eliminar.place(relx=0.9, rely=0.9, anchor=CENTER)
    title_menu.place(relx=0.17, rely=0.1, anchor=CENTER)

    # icono app
    root.iconbitmap(ruta_icono)

    # Ejecutar el bucle principal de la ventana
    root.geometry(f"{600}x{500}+{625}+{225}")
    root.mainloop()


