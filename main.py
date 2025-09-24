import pygame
from Game import Arena, Kotak, Ular, Makan

#init
window = Arena(500,500,20,20)
ular = Ular(window, (10, 10), arah_x=1)

makan = Makan(window, nama='makan')
is_run = True
tick = 8

while is_run:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False
    
    #update
    ular.move()
    
    if ular.is_collide():
        window.reset_member()
        ular.reset()
        makan = Makan(window, nama='makan')
    
    if ular.get_posisi() == makan.get_posisi():
        ular.tambah_kotak()
        makan.ubah_posisi()
    
    #render
    window.render(tick)


pygame.quit()