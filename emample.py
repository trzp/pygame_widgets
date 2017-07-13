from pygame_textbox import textbox
from pygame_label import label
from pygame_button import button
from pygame_callback import gui_callback

import pygame
pygame.init()

def check(arg):
    if arg[0]=='mrtang' and arg[1]=='12345678': return 1
    else:                                       return 0
callback = gui_callback()
callback.func = check

screen = pygame.display.set_mode((320, 260))
screen.fill((0,180,0))

label1 = label(screen,(20,50),'left',borderon = 0,text='username:',textsize = 25,forecolor=(0,0,0,0))
label2 = label(screen,(20,100),'left',borderon = 0,text='password:',textsize = 25,forecolor=(0,0,0,0))

label3 = label(screen,(60,150),'left',borderon = 0,text='state:',textsize = 25,forecolor=(0,0,0,0))
label4 = label(screen,(150,150),'left',borderon = 0,text='',textsize = 25,forecolor=(0,0,0,0))

textbox1 = textbox(screen,(150,50),(150,25),'left')
textbox2 = textbox(screen,(150,100),(150,25),'left')

bt1 = button(screen,(150,200),'center',size=(100,25),text='login',textsize = 20)

arg = []
while True:
    screen.fill((100, 100, 100))
    events = pygame.event.get()
    textbox1.update(events)
    textbox2.update(events)
    label1.update()                                                                
    label2.update()
    label3.update()
    label4.update()
    callback.args = [textbox1.gettext,textbox2.gettext]
    bt1.update(events,callback)
    if callback.res==0:label4.text='incorrect'
    else:     label4.text='correct'
    pygame.display.update()
    for event in events:
        if event.type == pygame.QUIT:pygame.quit()
    