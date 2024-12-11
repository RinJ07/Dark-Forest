import pygame as pgame, sys 
from PIL import Image

#####################################################
### Windows Display

pgame.init()
WinD = pgame.display.set_mode((960, 540))       #Window size
pgame.display.set_caption("Dark Forest")
time = pgame.time.Clock()
########################################################
########################################################
## Musics 


#pgame.mixer.music.load("Assets/audio/bg_music.mWAV")    ## BG Music

pgame.mixer.music.load("Assets/audio/bg_music1.mp3")
pgame.mixer.music.set_volume(1.0)
pgame.mixer.music.play(-1)
bttn_sound_effect = pgame.mixer.Sound("Assets/audio/bttn_hover.wav")
bttn_sound_effect.set_volume(1.0)





#######################################################
#######################################################
## Assets / Images


bg_img = Image.open("Assets/img/bg_image.gif")
idleimg_bttn = pgame.image.load("Assets/img/idle_bttn.png")
idleimg_bttn = pgame.transform.scale(idleimg_bttn,(200, 200))
hoverimg_bttn =pgame.image.load("Assets/img/hover_bttn.png")
hoverimg_bttn = pgame.transform.scale(hoverimg_bttn, (200, 200))


title_img = pgame.image.load("Assets/img/title.png")
title_img = pgame.transform.scale(title_img, (400, 300))

bgimg_size = (460,540) # Size fo the Gif BG Image


#############################################################
########################################################

## Frames

gframes = []

try:
    while True:
        frame = bg_img.convert("RGBA")
        bg_frame =pgame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
        resize = pgame.transform.scale(bg_frame, bgimg_size)
        gframes.append(resize)
        bg_img.seek(len(gframes))  # Go to the next frame

except EOFError:
    pass  # End of GIF

frame_duration = bg_img.info['duration'] / 900
current_frame = 0

######################################################################
#####################################################################
### Buttons ##########

class button:
    def __init__(self, x, y, width, height, idleimg_bttn, hoverimg_bttn, text, font_size, sound_effect, callback ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.idle_button = pgame.transform.scale(idleimg_bttn, (width, height))
        self.hover_button =pgame.transform.scale(hoverimg_bttn, (width, height))
        self.text = text
        self.font_size = font_size
        self.font = pgame.font.SysFont("Time New Roman", font_size)
        self.text_surface = self.font.render(text, True, (225,225,225))
        self.sound_effect = bttn_sound_effect
        self.callback = callback
        self.hover = False
        self.sound_play = False

        
    def draw (self, WinD):
        if self.hover:
            WinD.blit(self.hover_button, (self.x, self.y))
        else:
            WinD.blit(self.idle_button, (self.x, self.y))
        text_rect = self.text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        WinD.blit(self.text_surface, text_rect)
        pgame.display.update()

    def handle_event(self, event):
        if event.type == pgame.MOUSEMOTION:
            if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
                if not self.hover:
                    self.hover = True
                    if self.sound_effect and not self.sound_play:
                        self.sound_effect.play()
                        self.sound_play = True
            else:
                self.hover = False
                self.sound_play = False
        elif event.type == pgame.MOUSEBUTTONDOWN:
            if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
                self.callback()
                self.hover =False

    def play_sound_effect(self):
        if self.sound_effect:
            self.sound_effect.play()



def bttn1_callback():
    print("Button1 clicked.!!!!")

def bttn2_callback():
    print("Button2 clicked.!!!!")

def bttn3_callback():
    pgame.quit()
    print("Exit.!!!!")
    sys.exit()


button1 = button(100, 200, 300, 100, idleimg_bttn, hoverimg_bttn, "Start", 50, bttn_sound_effect, bttn1_callback)
button2 = button(150, 300, 300, 100, idleimg_bttn, hoverimg_bttn, "Settings",50, bttn_sound_effect, bttn2_callback)
button3 = button(100, 400, 300, 100, idleimg_bttn, hoverimg_bttn, "Exit", 50, bttn_sound_effect, bttn3_callback)


###########################
#  Main Loop
run = True
while run:

    

    for event in pgame.event.get():
        if event.type == pgame.QUIT:
            run = False


   



        button1.handle_event(event)
        button2.handle_event(event)
        button3.handle_event(event)
    

    

    WinD.fill((34, 32, 52))
    

    WinD.blit(gframes[current_frame], (500, 0)) # GIF Image Position
    WinD.blit(title_img,(400,0))

    

    button1.draw(WinD)
    button2.draw(WinD)
    button3.draw(WinD)
    current_frame = (current_frame + 1) % len(gframes)
    time.tick(1 / frame_duration)
    

   
    
    pgame.display.update()
