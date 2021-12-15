import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Taller place()")
ventana.geometry('600x300')
ventana.resizable(False, False)
 

principal_frame = tk.Frame(ventana)
principal_frame.config(bg='cyan', bd=1)
principal_frame.place(width= 600, height=300)

frame1 = tk.Frame(principal_frame)
frame1.config(bg='white',bd=5,cursor="plus",relief="ridge")
frame1.place(x=10, y=10, width=580, height=60)

title = tk.Label(frame1, text='The hospital is ________ the bank')
title.config(fg='red', bg='white', font=("Times",15))
title.place(x=120, y= 15)

frame2 = tk.Frame(principal_frame,bg='white',bd=1,cursor="pirate",relief="ridge")
frame2.place(x=10, y=85, relwidth=0.6, height=200)

cuadro_imagen = tk.PhotoImage(file = r"cuadro.png")
imagen_cuadro = cuadro_imagen.subsample(2, 2)
label_image = tk.Label(frame2, image = imagen_cuadro)
label_image.config(bg="white")
label_image.place(x=0, y=0)

frame3 = tk.Frame(principal_frame,bg='white',bd=1,cursor="pirate",relief="ridge")
frame3.place(relx=0.65, y=85, relwidth=0.33, height=200)

boton1 = tk.Button(frame3, text="A between")
boton1.config(bg='sky blue', fg='black', cursor="question_arrow")
boton1.place(height=50, relwidth=1, relx=0, rely=0)

boton2 = tk.Button(frame3, text="B behind")
boton2.config(bg='red', fg='black', cursor="question_arrow")
boton2.place(height=50, relwidth=1, relx=0, rely=0.25)

boton3 = tk.Button(frame3, text="C next to")
boton3.config(bg='orange', fg='black', cursor="question_arrow")
boton3.place(height=50, relwidth=1, relx=0, rely=0.5)

boton4 = tk.Button(frame3, text="D in front of")
boton4.config(bg='green', fg='black', cursor="question_arrow")
boton4.place(height=50, relwidth=1, relx=0, rely=0.75)


ventana.mainloop()