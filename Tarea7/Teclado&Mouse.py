import tkinter as tk

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.x = None
        self.y = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            self.raiz.x = 400
            self.raiz.y = 50
        else:
            self._insertar_recursivo(valor, self.raiz, 400, 50, 200)

    def _insertar_recursivo(self, valor, nodo, x, y, espacio):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
                nodo.izquierda.x = x - espacio
                nodo.izquierda.y = y + 50
            else:
                self._insertar_recursivo(valor, nodo.izquierda, x - espacio, y + 50, espacio // 2)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
                nodo.derecha.x = x + espacio
                nodo.derecha.y = y + 50
            else:
                self._insertar_recursivo(valor, nodo.derecha, x + espacio, y + 50, espacio // 2)

# Crear ventana
ventana = tk.Tk()
ventana.title("Árbol con Tkinter")

# Crear canvas
canvas = tk.Canvas(ventana, width=800, height=600)
canvas.pack()

# Crear árbol
arbol = Arbol()

def insertar_nodo(event):
    valor = event.char
    if valor.isdigit():
        arbol.insertar(int(valor))
        dibujar_arbol(canvas, arbol.raiz)

def dibujar_arbol(canvas, nodo):
    if nodo is not None:
        dibujar_arbol(canvas, nodo.izquierda)
        dibujar_arbol(canvas, nodo.derecha)
        canvas.create_oval(nodo.x-20, nodo.y-20, nodo.x+20, nodo.y+20, fill="sea green", outline="black")
        canvas.create_text(nodo.x, nodo.y, text=str(nodo.valor))

def mouse_move(event):
    x = event.x
    y = event.y
    label.config(text=f'Posición del ratón: x={x}, y={y}')

def key_press(event):
    key = event.keysym
    label.config(text=f'Tecla presionada: {key}')
    insertar_nodo(event)

def key_release(event):
    label.config(text='')

# Asociar el evento de movimiento del ratón con la función mouse_move
canvas.bind('<Motion>', mouse_move)

# Asociar el evento de presionar una tecla con la función key_press
canvas.bind('<KeyPress>', key_press)

# Asociar el evento de soltar una tecla con la función key_release
canvas.bind('<KeyRelease>', key_release)

# Crear una etiqueta para mostrar la posición del ratón y la tecla presionada
label = tk.Label(ventana, text="")
label.pack()

# Capturar eventos de teclado
canvas.focus_set()

# Iniciar la ventana
ventana.mainloop()
