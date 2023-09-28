import tkinter as tk
from tkinter import ttk
import re
import time

expresion_regular = r'^(G|g)[G-Yg-y][A-Za-z]-(0[1-9][0-9]|00[1-9]|[1-9][0-9][0-9])-[A-Za-z]$'


def validar_cadena(cadena):
    return bool(re.match(expresion_regular, cadena))


def automata_validacion(cadena):
    estado_actual = 'inicio'
    
    for caracter in cadena:
        time.sleep(0.5)  
        if estado_actual == 'inicio':

            canvas.itemconfig(circulo0, fill="#FF8360")
            canvas.itemconfig(q0, fill="white")
            canvas.itemconfig(initial, fill="#FF8360")
            ventana.update()
            time.sleep(0.5)  
            
            if caracter.lower() == 'g':
                estado_actual = 'letra_g'
                canvas.itemconfig(circulo1, fill="#FF8360")
                canvas.itemconfig(q1, fill="white")
                canvas.itemconfig(q0q1, fill="#FF8360")
                ventana.update()

            else:
                return False
        elif estado_actual == 'letra_g':
            
            if 'g' <= caracter.lower() <= 'y':
                estado_actual = 'letra_2'
                canvas.itemconfig(circulo2, fill="#FF8360")
                canvas.itemconfig(q2, fill="white")
                canvas.itemconfig(q1q2, fill="#FF8360")
                ventana.update()

            else:
                return False
        elif estado_actual == 'letra_2':
            
            if 'a' <= caracter.lower() <= 'z':
                estado_actual = 'guion'
                canvas.itemconfig(circulo3, fill="#FF8360")
                canvas.itemconfig(q3, fill="white")
                canvas.itemconfig(q2q3, fill="#FF8360")
                ventana.update()
            else:
                return False
        elif estado_actual == 'guion':
            
            if caracter == '-':
                estado_actual = 'numero'
                canvas.itemconfig(circulo4, fill="#FF8360")
                canvas.itemconfig(q4, fill="white")
                canvas.itemconfig(q3q4, fill="#FF8360")
                ventana.update()

            else:
                return False
        
        elif estado_actual == 'numero':
            
            if caracter== '0':
                estado_actual = 'numerocaso1'
                canvas.itemconfig(circulo5, fill="#FF8360")
                canvas.itemconfig(q5, fill="white")
                canvas.itemconfig(q4q5, fill="#FF8360")
                ventana.update()
                
            elif '1' <= caracter <= '9':
                estado_actual = 'numerocaso2'
                canvas.itemconfig(circulo7, fill="#FF8360")
                canvas.itemconfig(q7, fill="white")
                canvas.itemconfig(q4q7, fill="#FF8360")
                ventana.update()
            else:
                return False
        

        elif estado_actual == 'numerocaso1':
            
            if caracter == '0':
                estado_actual = 'numerocaso12'
                canvas.itemconfig(circulo6, fill="#FF8360")
                canvas.itemconfig(q6, fill="white")
                canvas.itemconfig(q5q6, fill="#FF8360")
                ventana.update()  
            elif '1' <= caracter <= '9':
                estado_actual = 'numerocaso13'
                canvas.itemconfig(circulo8, fill="#FF8360")
                canvas.itemconfig(q8, fill="white")
                canvas.itemconfig(q5q8, fill="#FF8360")
                ventana.update()
            else:
                return False
        elif estado_actual == 'numerocaso12':   
            if '1' <= caracter <= '9':
                estado_actual = 'guion2'
                canvas.itemconfig(circulo9, fill="#FF8360")
                canvas.itemconfig(q9, fill="white")
                canvas.itemconfig(q6q9, fill="#FF8360")
                ventana.update()
            else:
                return False        
        elif estado_actual == 'numerocaso13':
                     
            if '0' <= caracter <= '9':
                estado_actual = 'guion2'
                canvas.itemconfig(circulo9, fill="#FF8360")
                canvas.itemconfig(q9, fill="white")
                canvas.itemconfig(q8q9, fill="#FF8360")
                ventana.update()
            else:
                return False       
        elif estado_actual == 'numerocaso2':
                      
            if '0' <= caracter <= '9':
                estado_actual = 'numerocaso22'
                canvas.itemconfig(circulo8, fill="#FF8360")
                canvas.itemconfig(q8, fill="white")
                canvas.itemconfig(q7q8, fill="#FF8360")
                ventana.update()
            else:
                return False        
        elif estado_actual == 'numerocaso22':
                       
            if '0' <= caracter <= '9':
                estado_actual = 'guion2'
                canvas.itemconfig(circulo9, fill="#FF8360")
                canvas.itemconfig(q9, fill="white")
                canvas.itemconfig(q8q9, fill="#FF8360")
                ventana.update()
            else:
                return False        
        elif estado_actual == 'guion2':
                      
            if caracter == '-':
                estado_actual = 'last_letter'
                canvas.itemconfig(circulo10, fill="#FF8360")
                canvas.itemconfig(q10, fill="white")
                canvas.itemconfig(q9q10, fill="#FF8360")
                ventana.update()
            else:
                return False       
        elif estado_actual == 'last_letter':
                     
            if 'a' <= caracter.lower() <= 'z':
                estado_actual = 'last'
                canvas.itemconfig(circulo11, fill="#FF8360")
                canvas.itemconfig(q11, fill="white")
                canvas.itemconfig(q10q11, fill="#FF8360")
                ventana.update()
            else:
                return False

        
    
    
    return estado_actual in {'last'}





ventana = tk.Tk()
ventana.title("Autómata")
ventana.geometry("1000x700")


ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

x = (ancho_pantalla - ventana.winfo_reqwidth()-450) // 2
y = (alto_pantalla - ventana.winfo_reqheight()-550) // 2

ventana.geometry("+{}+{}".format(x, y))
ventana.configure(bg="#f7f7f8")
string = tk.Label(ventana, text="Ingresa tu cadena",bg="#f7f7f8", fg="#413936" )
string.pack()

entry = ttk.Entry(ventana,style=ttk.Style().configure("estilo",bordercolor="", borderwidth=0, highlightbackground = ""))
entry.pack()

result = tk.Label(ventana, text="",bg="#f7f7f8", fg="#413936")
result.pack()
'''
def validate_regex():
    cadena=entry.get()
    valid=validar_cadena(cadena)
    if valid:
        result.config(text="Es válida tu cadena con REGEX")
    else:
        result.config(text="No es válida con REGEX")
'''
def validate():
    cadena=entry.get()
    circulos = [circulo0, circulo1, circulo2, circulo3, circulo4, circulo5, circulo6, circulo7, circulo8, circulo9, circulo10, circulo11]
    flechas = [initial, q0q1, q1q2, q2q3, q3q4, q4q5, q5q6, q4q7, q5q8, q7q8, q6q9, q8q9, q9q10, q10q11]
    textos = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]

    for circulo_id in circulos:
        canvas.itemconfig(circulo_id, fill="#ffffff", outline="#FF8360")

    for flecha_id in flechas:
        canvas.itemconfig(flecha_id, fill="#413936")

    for texto_id in textos:
        canvas.itemconfig(texto_id, fill="black")
    result.config(text="")
    valid=automata_validacion(cadena)
    if valid:
        result.config(text="Es válida tu cadena")
    else:
        result.config(text="No es válida")

'''boton = tk.Button(ventana, text="Validar con REGEX", command=validate_regex)
boton.pack()'''
boton2 = tk.Button(ventana, text="Validar", command=validate, borderwidth=5, bg="blue",highlightbackground="#f7f7f8")
boton2.pack()


canvas = tk.Canvas(ventana, width=1000, height=300,bg="#f7f7f8", highlightbackground="#f7f7f8")  
canvas.pack()

initial = canvas.create_line(0, 75, 50, 75, arrow=tk.LAST, fill="#413936")
circulo0 = canvas.create_oval(50, 50, 100, 100, fill="white", outline="#FF8360")
q0 = canvas.create_text(75, 75, text="q0", fill="black", font=("Arial", 12))

q0q1 = canvas.create_line(100, 75, 150, 75, arrow=tk.LAST, fill="#413936")
cond1 = canvas.create_text(125, 60, text="G", fill="black", font=("Arial", 12))
circulo1 = canvas.create_oval(150, 50, 200, 100, fill="white", outline="#FF8360")
q1 = canvas.create_text(175, 75, text="q1", fill="black", font=("Arial", 12))

q1q2 = canvas.create_line(200, 75, 250, 75, arrow=tk.LAST, fill="#413936")
cond2 = canvas.create_text(225, 60, text="[G-Y]", fill="black", font=("Arial", 12))
circulo2 = canvas.create_oval(250, 50, 300, 100, fill="white", outline="#FF8360")
q2 = canvas.create_text(275, 75, text="q2", fill="black", font=("Arial", 12))

q2q3 = canvas.create_line(300, 75, 350, 75, arrow=tk.LAST, fill="#413936")
cond3 = canvas.create_text(325, 60, text="[A-Z]", fill="black", font=("Arial", 12))
circulo3 = canvas.create_oval(350, 50, 400, 100, fill="white", outline="#FF8360")
q3 = canvas.create_text(375, 75, text="q3", fill="black", font=("Arial", 12))

q3q4 = canvas.create_line(400, 75, 450, 75, arrow=tk.LAST, fill="#413936")
cond4 = canvas.create_text(425, 60, text="-", fill="black", font=("Arial", 12))
circulo4 = canvas.create_oval(450, 50, 500, 100, fill="white", outline="#FF8360")
q4 = canvas.create_text(475, 75, text="q4", fill="black", font=("Arial", 12))

q4q5 = canvas.create_line(500, 75, 550, 75, arrow=tk.LAST, fill="#413936")
cond5 = canvas.create_text(525, 60, text="0", fill="black", font=("Arial", 12))
circulo5 = canvas.create_oval(550, 50, 600, 100, fill="white", outline="#FF8360")
q5 = canvas.create_text(575, 75, text="q5", fill="black", font=("Arial", 12))

q5q6 = canvas.create_line(600, 75, 650, 75, arrow=tk.LAST, fill="#413936")
cond6 = canvas.create_text(625, 60, text="0", fill="black", font=("Arial", 12))
circulo6 = canvas.create_oval(650, 50, 700, 100, fill="white", outline="#FF8360")
q6 = canvas.create_text(675, 75, text="q6", fill="black", font=("Arial", 12))

q4q7 = canvas.create_line(475, 100, 475, 150, arrow=tk.LAST, fill="#413936")
cond8 = canvas.create_text(500, 125, text="[1-9]", fill="black", font=("Arial", 12))

circulo7 = canvas.create_oval(450, 150, 500, 200, fill="white", outline="#FF8360")
q7 = canvas.create_text(475, 175, text="q7", fill="black", font=("Arial", 12))

q5q8 = canvas.create_line(575, 100, 575, 150, arrow=tk.LAST, fill="#413936")
cond8 = canvas.create_text(600, 125, text="[1-9]", fill="black", font=("Arial", 12))

q7q8 = canvas.create_line(500, 175, 550, 175, arrow=tk.LAST, fill="#413936")
cond7 = canvas.create_text(525, 160, text="[0-9]", fill="black", font=("Arial", 12))
circulo8 = canvas.create_oval(550, 150, 600, 200, fill="white", outline="#FF8360")
q8 = canvas.create_text(575, 175, text="q8", fill="black", font=("Arial", 12))

q6q9 = canvas.create_line(675, 100, 675, 150, arrow=tk.LAST, fill="#413936")
cond8 = canvas.create_text(700, 125, text="[1-9]", fill="black", font=("Arial", 12))

q8q9 = canvas.create_line(600, 175, 650, 175, arrow=tk.LAST, fill="#413936")
cond8 = canvas.create_text(625, 160, text="[0-9]", fill="black", font=("Arial", 12))
circulo9 = canvas.create_oval(650, 150, 700, 200, fill="white", outline="#FF8360")
q9 = canvas.create_text(675, 175, text="q9", fill="black", font=("Arial", 12))

q9q10 = canvas.create_line(700, 175, 750, 175, arrow=tk.LAST, fill="#413936")
cond9 = canvas.create_text(725, 160, text="-", fill="black", font=("Arial", 12))
circulo10 = canvas.create_oval(750, 150, 800, 200, fill="white", outline="#FF8360")
q10 = canvas.create_text(775, 175, text="q10", fill="black", font=("Arial", 12))

q10q11 = canvas.create_line(800, 175, 850, 175, arrow=tk.LAST, fill="#413936")
cond10 = canvas.create_text(825, 160, text="[A-Z]", fill="black", font=("Arial", 12))
circulo11 = canvas.create_oval(850, 150, 900, 200, fill="white", outline="#FF8360")
q11 = canvas.create_text(875, 175, text="q11", fill="black", font=("Arial", 12))


  # Salida: "Hola, Mundo"
ventana.mainloop()


