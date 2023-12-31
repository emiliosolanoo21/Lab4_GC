import pygame
from pygame.locals import *
import glm
from gl import Renderer
from model import Model
from shaders import *

width = 960
height = 540

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)

clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(complex_shader, fragment_shader)

#---------------------------------------------------------------
#Montaje de figuras

obj1 = rend.loadModel(filename = "axe.obj", texture = "axe.bmp", position = (0,-2,-5))

#Comentarle a Carlos esto del LookAt
rend.target = obj1.position

isRunning = True
while isRunning:
    
    deltaTime = clock.tick(60)/1000
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_SPACE:
                rend.toggleFilledMode()
                
            elif event.key == pygame.K_1:
                rend.setShaders(complex_shader, chess_shader)
            elif event.key == pygame.K_2:
                rend.setShaders(complex_shader, golden_shader)
            elif event.key == pygame.K_3:
                rend.setShaders(complex_shader, disco_shader)
            elif event.key == pygame.K_4:
                rend.setShaders(complex_shader, pattern_shader)            

    #5 unidades por segundo
    if keys[K_d]:
        rend.camPosition.x -= 5 * deltaTime 
         
    elif keys[K_a]:
        rend.camPosition.x += 5 * deltaTime
    
    if keys[K_w]:
        rend.camPosition.y -= 5 * deltaTime
         
    elif keys[K_s]:
        rend.camPosition.y += 5 * deltaTime
            
    if keys[K_q]:
        rend.camPosition.z += 5 * deltaTime
        
    elif keys[K_e]:
        rend.camPosition.z -= 5 * deltaTime
        
    obj1.rotation.y += 45 * deltaTime
    
    if keys[K_RIGHT]:
        obj1.rotation.y += 45 * deltaTime 
         
    elif keys[K_LEFT]:
        obj1.rotation.y -= 135 * deltaTime #135 con rotacion constante
        
    if keys[K_f]:
        if rend.fatness <1.0:
            rend.fatness += 1 *deltaTime
            
    elif keys[K_t]:
        if rend.fatness >0.0:
            rend.fatness -= 1 *deltaTime
            
    rend.elapsedTime += deltaTime
        
    rend.update()
    rend.render()
    
    pygame.display.flip()

pygame.quit()