import pygame as pg

pg.init()
rect_w = 100
rect_h = 100
win_x, win_y = 800, 600
screen = pg.display.set_mode((win_x, win_y))

rect_x = 0
rect_y = 0
rect_speed = 5

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    key = pg.key.get_pressed()
    if key[pg.K_a]:
        rect_x -= rect_speed
    elif key[pg.K_d]:
        rect_x += rect_speed
    elif key[pg.K_w]:
        rect_y -= rect_speed
    elif key[pg.K_s]:
        rect_y += rect_speed
    
    if rect_x < 0:
        rect_x = 0
    elif rect_x > win_x - rect_w:
        rect_x = win_x - rect_w
    if rect_y < 0:
        rect_y = 0
    elif rect_y > win_y - rect_h:
        rect_y = win_y - rect_h
    
    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_w, rect_h))

    pg.display.update()

pg.quit()
