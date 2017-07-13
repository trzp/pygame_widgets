from pygame_textbox import textbox
from pygame_label import label
from pygame_button import button
import pygame

class example:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((320, 260))
        self.screen.fill((0,180,0))

        self.label1 = label(self.screen,(20,50),'left',borderon = 0,text='username:',textsize = 25,forecolor=(0,0,0,0))
        self.label2 = label(self.screen,(20,100),'left',borderon = 0,text='password:',textsize = 25,forecolor=(0,0,0,0))

        self.label3 = label(self.screen,(60,150),'left',borderon = 0,text='state:',textsize = 25,forecolor=(0,0,0,0))
        self.label4 = label(self.screen,(150,150),'left',borderon = 0,text='',textsize = 25,forecolor=(0,0,0,0))

        self.textbox1 = textbox(self.screen,(150,50),(150,25),'left')
        self.textbox2 = textbox(self.screen,(150,100),(150,25),'left')

        self.bt1 = button(self.screen,(150,200),'center',size=(100,25),text='login',textsize = 20)
        self.clk = pygame.time.Clock()

    def callback(self):
        if self.textbox1.gettext=='mrtang' and self.textbox2.gettext=='123456': self.label4.text='correct'
        else:   self.label4.text='incorrect'

    def run(self):
        while True:
            self.screen.fill((100, 100, 100))
            events = pygame.event.get()

            self.textbox1.update(events)
            self.textbox2.update(events)
            self.label1.update()
            self.label2.update()
            self.label3.update()
            self.label4.update()
            self.bt1.update(events,self.callback)
            
            pygame.display.update()
            self.clk.tick(30)
            for event in events:
                if event.type == pygame.QUIT:pygame.quit()

a = example()
a.run()