import pygame
from pygame.locals import K_LEFT, K_RIGHT  # Importamos las teclas

pygame.init()

# Definir colores
white = (255, 255, 255)

# Crear la pantalla
screen = pygame.display.set_mode((800, 600))

# Variables para el bucle
onOff = True

# Crear la posición inicial de la barra
barra_x = 400  # Posición inicial en X
barra_y = 580  # Posición Y fija
barra_width = 100
barra_height = 10
velocidad = 1  # Velocidad de movimiento de la barra

# Bucle principal
while onOff:
    screen.fill((0, 0, 0))  # Fondo negro

    # Dibujar la barra en la pantalla
    barra = pygame.draw.rect(screen, white, (barra_x, barra_y, barra_width, barra_height))

    # Procesar los eventos
    for event in pygame.event.get():
        # Salir del juego si se presiona la X de la ventana
        if event.type == pygame.QUIT:
            onOff = False

    # Detectar teclas presionadas
    keys = pygame.key.get_pressed()  # Detecta las teclas que están siendo presionadas

    # Mover la barra con las teclas izquierda y derecha
    if keys[K_LEFT] and barra_x > 0:  # Mover hacia la izquierda
        barra_x -= velocidad
    if keys[K_RIGHT] and barra_x < 800 - barra_width:  # Mover hacia la derecha
        barra_x += velocidad

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()


