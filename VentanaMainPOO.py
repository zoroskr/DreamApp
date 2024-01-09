from tkinter import *
from PIL import Image, ImageTk
import pygame
import webbrowser
import VentanaAnotadorPOO
import VentanaSueñosPOO
import os


def reproducir_audio(audio):
    pygame.mixer.init()
    # Reemplaza con la ruta de tu archivo de audio
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()


def abrir_enlace(enlace, audio):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_audio = os.path.join(current_dir, audio)
    reproducir_audio(ruta_audio)
    webbrowser.open(enlace)


def abrir_anotador(root):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_audio = os.path.join(current_dir, "takeover - glitch fx 9.wav")
    reproducir_audio(ruta_audio)
    root.destroy()
    VentanaAnotadorPOO.crear_ventana()

def abrir_sueños(root):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_audio = os.path.join(current_dir, "takeover - glitch fx 10.wav")
    reproducir_audio(ruta_audio)
    root.destroy()
    VentanaSueñosPOO.crear_ventana()


def crear_ventana():
    # Crear la ventana
    root = Tk()
    root.title("DreamApp :)")
    root.resizable(width=False, height=False)

    # Cargar la imagen
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(current_dir, 'background_traumacore.png')
    ruta_icono = os.path.join(current_dir, 'icon_dreamapp.ico')

    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 500), Image.LANCZOS)
    imagen = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen
    label_imagen = Label(root, image=imagen)
    label_imagen.pack()

    # Crear un botón
    boton_save = Button(root, text="Save Dream :(", command=lambda: abrir_anotador(root))
    boton_mostrar = Button(root, text="Show Dreams", command=lambda: abrir_sueños(root))
    boton_bladee = Button(root, command=lambda: abrir_enlace(
        "https://youtu.be/xUAgawZAi5g", "fx [nokia].wav"), text='                ', bg="white", bd=0, highlightthickness=0)
    boton_tavewav = Button(root, command=lambda: abrir_enlace(
        "https://on.soundcloud.com/Muhjw", "takeover - glitch fx 1.wav"), text='       ', bg="white", bd=0, highlightthickness=0)
    boton_mostdays = Button(root, command=lambda: abrir_enlace(
        "https://on.soundcloud.com/bVgPi", "takeover - glitch fx 3.wav"), text=':(', bg="white", bd=0, highlightthickness=0)
    boton_thinkabt = Button(root, command=lambda: abrir_enlace(
        "https://youtu.be/8FgRYlgmqkk", "takeover - glitch fx 4.wav"), text='⊂(◉‿◉)つ', bg="white", bd=0, highlightthickness=0)
    boton_kiryano = Button(root, command=lambda: abrir_enlace(
        "https://youtu.be/jzRFFW1TDj0", "takeover - glitch fx 5.wav"), text='︻╦╤─', bg="white", bd=0, highlightthickness=0)
    boton_saikyoz = Button(root, command=lambda: abrir_enlace(
        "https://youtu.be/RFlABurW3Xo", "takeover - glitch fx 6.wav"), text='=^_^=', bg="white", bd=0, highlightthickness=0)

    # Colocar el botón encima de la imagen usando el método place()
    boton_save.place(relx=0.1, rely=0.9, anchor=CENTER)
    boton_mostrar.place(relx=0.90, rely=0.9, anchor=CENTER)
    boton_bladee.place(relx=0.4, rely=0.93, anchor=CENTER)
    boton_tavewav.place(relx=0.087, rely=0.71, anchor=CENTER)
    boton_mostdays.place(relx=0.080, rely=0.40, anchor=CENTER)
    boton_thinkabt.place(relx=0.406, rely=0.435, anchor=CENTER)
    boton_kiryano.place(relx=0.3, rely=0.95, anchor=CENTER)
    boton_saikyoz.place(relx=0.56, rely=0.885, anchor=CENTER)

    #icono app
    root.iconbitmap(ruta_icono)
    
    # Ejecutar el bucle principal de la ventana
    root.geometry(f"{600}x{500}+{625}+{225}")
    root.mainloop()
    
if __name__ == "__main__":
    crear_ventana()