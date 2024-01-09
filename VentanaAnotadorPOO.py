from cgitb import text
from math import fabs
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

def guardar_datos(entrada, entrada_2):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_datos = os.path.join(current_dir, 'datos.json')
    informacion = {
        'titulo': entrada.get(),
        'descripcion': entrada_2.get()
    }
    with open(ruta_datos) as archivo_json:
        data = json.load(archivo_json)
        data.append(informacion)
    with open(ruta_datos, 'w') as archivo_json:
        json.dump(data, archivo_json)

def salir(root):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_sonido = os.path.join(current_dir, 'takeover - glitch fx 8.wav')
    reproducir_audio(ruta_sonido)
    root.destroy()
    VentanaMainPOO.crear_ventana()
    
def guardar_salir(entrada, entrada_2, root):
    guardar_datos(entrada, entrada_2)
    salir(root)

def crear_ventana():
    root = Tk()
    root.title("DreamApp :)")
    root.resizable(width=False, height=False)

    # Cargar la imagen
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(current_dir, 'background_dreamcore_2.jpeg')
    ruta_icono = os.path.join(current_dir, 'icon_dreamapp.ico')
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 500), Image.LANCZOS)
    imagen = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen
    label_imagen = Label(root, image=imagen)
    label_imagen.pack()

    # Crear widgets
    entrada = Entry(root, width=30)
    entrada_2 = Entry(root, width=30)
    titulo_sueño = Label(root, text='Enter the Dream title')
    descr_sueño = Label(root, text='Show your dream :)')
    boton_save = Button(root, text="Save", command=lambda: guardar_salir(entrada, entrada_2, root))
    boton_exit = Button(root, text="Exit", command=lambda: salir(root))

    # Colocar widget
    titulo_sueño.place(relx=0.145, rely=0.15, anchor=CENTER)
    entrada.place(relx=0.2, rely=0.2, anchor=CENTER)
    descr_sueño.place(relx=0.140, rely=0.30, anchor=CENTER)
    entrada_2.place(relx=0.2, rely=0.35, anchor=CENTER)
    boton_save.place(relx=0.08, rely=0.45, anchor=CENTER)
    boton_exit.place(relx=0.08, rely=0.9, anchor=CENTER)

    #icono app
    root.iconbitmap(ruta_icono)


    # Ejecutar el bucle principal de la ventana
    root.geometry(f"{600}x{500}+{625}+{225}")
    root.mainloop()