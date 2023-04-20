import sys 
import pygame as pg

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
class Rec:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.R = 250
        self.G = 0
        self.B = 0
    def draw(self,screen):
        pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h))

class Button(Rec):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rec.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        x = 0 #cursur mouse
        y = 0
        x,y = pg.mouse.get_pos()
        if x >= self.x and x <= self.x + self.w and y >= self.y and y <= self.y + self.h :
            return True #activate function
        else : return False
        pass
    
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 250, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(100, 400, 140, 32) # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('First name', True, (255,0,255), (0,0,0)) 
text2 = font.render('Last name', True, (255,0,255), (0,0,0))# (text,is smooth?,letter color,background color)
text3 = font.render('Age', True, (255,0,255), (0,0,0))
text4 = font.render('Submit', True, (255,255,255), (0,0,0))
textRect = text.get_rect() # text size
textRect2 = text.get_rect() # text size
textRect3 = text.get_rect() # text size
textRect4 = text.get_rect() # text size
textRect5 = text.get_rect() # text size
textRect.center = (160,80)
textRect2.center = (140,60)
textRect3.center = (120,40)
textRect4.center = (100,20)
textRect5.center = (80,0)
btn = Button(400-50,240-50,100,100)
btn.draw(screen)
Click = False

while run:
    screen.fill((255, 255, 255))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        screen.bilt(text,textRect)
        btn.draw(screen)
        screen.bilt(text2,textRect2)
        screen.bilt(text3,textRect3)
        screen.bilt(text4,textRect4)
    if btn.isMouseOn():
        if pg.mouse.get_pressed() == (1,0,0):
                Click = True
                btn.r,btn.g,btn.b = (0,255,128)
        else:
                btn.r,btn.g,btn.b = (0,0,0)
        if Click == True:
            text5 = font.render('hello '+str(input_box1.text)+' '+str(input_box2.text)+'! You are '+str(input_box3.text)+' years old.',True,(0,0,153),(255,255,255))
            screen.blit(text5,textRect5)

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()