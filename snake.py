"""Snake mínimo con turtle — versión para clase (un solo jugador).

Come cuadrados rojos para crecer. Chocar con el borde o contigo mismo
termina la partida (pulsa cualquier tecla para reiniciar).

Controles: flechas Arriba / Abajo / Izquierda / Derecha.

Conceptos que practica: listas (el cuerpo), bucle con reloj (ontimer),
condicionales de colisión y funciones.
"""
import random
import turtle

LADO = 20                     # tamaño de cada cuadrito (píxeles)
RETARDO = 120                 # milisegundos entre movimientos (menos = más difícil)

# ---------- ventana ----------
pantalla = turtle.Screen()
pantalla.title("Snake básico")
pantalla.bgcolor("black")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)

# ---------- marcador ----------
puntos = 0
marcador = turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.color("white")
marcador.goto(0, 265)

def escribir_marcador():
    marcador.clear()
    marcador.write(f"Puntos: {puntos}", align="center",
                   font=("Courier", 20, "bold"))

# ---------- serpiente ----------
# El cuerpo es una LISTA de tortugas; el índice 0 es la cabeza.
cabeza = turtle.Turtle()
cabeza.shape("square")
cabeza.color("lime")
cabeza.penup()

cuerpo = []                   # el resto de cuadritos (empieza vacío)
direccion = "stop"            # "up" / "down" / "left" / "right" / "stop"

# ---------- comida ----------
comida = turtle.Turtle()
comida.shape("square")
comida.color("red")
comida.penup()

def mover_comida():
    # salta a un punto aleatorio alineado a la cuadrícula de 20 px
    x = random.randrange(-280, 280, LADO)
    y = random.randrange(-280, 240, LADO)
    comida.goto(x, y)

# ---------- controles ----------
def ir_arriba():
    global direccion
    if direccion != "down":      # no permitir media vuelta
        direccion = "up"

def ir_abajo():
    global direccion
    if direccion != "up":
        direccion = "down"

def ir_izquierda():
    global direccion
    if direccion != "right":
        direccion = "left"

def ir_derecha():
    global direccion
    if direccion != "left":
        direccion = "right"

pantalla.listen()
pantalla.onkey(ir_arriba, "Up")
pantalla.onkey(ir_abajo, "Down")
pantalla.onkey(ir_izquierda, "Left")
pantalla.onkey(ir_derecha, "Right")

# ---------- lógica ----------
def mover():
    """Avanza un paso: el cuerpo sigue a la cabeza y la cabeza avanza."""
    # cada trozo copia la posición del que va delante (de la cola al cuello)
    for i in range(len(cuerpo) - 1, 0, -1):
        cuerpo[i].goto(cuerpo[i - 1].pos())
    if cuerpo:
        cuerpo[0].goto(cabeza.pos())

    if direccion == "up":
        cabeza.sety(cabeza.ycor() + LADO)
    elif direccion == "down":
        cabeza.sety(cabeza.ycor() - LADO)
    elif direccion == "left":
        cabeza.setx(cabeza.xcor() - LADO)
    elif direccion == "right":
        cabeza.setx(cabeza.xcor() + LADO)

def game_over():
    marcador.goto(0, 0)
    marcador.write("¡GAME OVER!", align="center",
                   font=("Courier", 30, "bold"))

def crecer():
    trozo = turtle.Turtle()
    trozo.shape("square")
    trozo.color("lime")
    trozo.penup()
    cuerpo.append(trozo)        # nace en el centro; la cola lo arrastra

def tick():
    """Un fotograma del juego; se re-agenda con ontimer."""
    global puntos

    mover()

    # ¿choque con el borde? (la ventana útil va de -290 a 290)
    if abs(cabeza.xcor()) > 290 or abs(cabeza.ycor()) > 290:
        game_over()
        return

    # ¿choque consigo mismo?
    for trozo in cuerpo:
        if trozo.distance(cabeza) < LADO - 2:
            game_over()
            return

    # ¿comer? (basta estar cerca del cuadrito rojo)
    if cabeza.distance(comida) < LADO:
        puntos += 1
        escribir_marcador()
        mover_comida()
        crecer()

    pantalla.update()
    pantalla.ontimer(tick, RETARDO)   # la gracia: se llama a sí mismo

# ---------- arranque ----------
mover_comida()
escribir_marcador()
pantalla.ontimer(tick, RETARDO)
pantalla.mainloop()
