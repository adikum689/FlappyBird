import pygame, random 
pygame.init()
TITLE= "Flappy Bird"
passpipe=False
HEIGHT= 900
WIDTH=864
run=True
gameover= False
flying= False
groundx= 0
pipe_space= 150
score= 0
timer= 5000
background= pygame.image.load("FlappyBird4.png")
bird1=pygame.image.load("FlappyBird 6.png")
bird2= pygame.image.load("FlappyBird5.png")
bird3= pygame.image.load("FlappyBird3.png")
ground=pygame.image.load("Flappy bird2.png")
pipe_image= pygame.image.load("Flappy Bird.png")
screen= pygame.display.set_mode((WIDTH, HEIGHT))
last_pipe_time= pygame.time.get_ticks()-timer
pygame.display.set_caption(TITLE)

class Birds (pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images= [bird1, bird2, bird3]
        self.index= 0
        self.image= self.images[0]
        self.rect= self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.click= False
        self.velocity= 0
    def update(self):
        if flying== True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
               self.velocity= -5
            if self.velocity<2:
                self.velocity+= 0.5
            else:
                self.velocity=2
            self.rect.y+= self.velocity

class Pipes (pygame.sprite.Sprite):
    def __init__(self,x, y, pos):
        super().__init__()
        self.image= pipe_image
        self.rect= self.image.get_rect()
        if pos== "up":
           self.image= pygame.transform.flip(self.image, False, True)
           self.rect.bottomleft= x, y-pipe_space/2
        if pos== "down":
            self.rect.topleft= x, y+pipe_space/2
    def update(self):
        self.rect.x-=1
        if self.rect.right<0:
            self.kill()
        
bird1= Birds(200,450)
birdgroup= pygame.sprite.Group()
birdgroup.add(bird1)
pipegroup= pygame.sprite.Group()




    


while run:
    screen.blit(background, (0,0)) 
    birdgroup.draw(screen)
    birdgroup.update()
    pipegroup.draw(screen)
    screen.blit(ground, (groundx,800))
    if gameover==False and flying==True:
        if groundx> -35:
            groundx-=1
        else: 
            groundx=0
    #checking for collision
    if pygame.sprite.groupcollide(birdgroup, pipegroup, False, False):
        gameover=True
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_UP and gameover==False and flying==False:
                flying=True
    if bird1.rect.bottom>650:
       bird1.rect.bottom=650
       gameover= True
       flying=False
    if flying==True and gameover==False:
        time_now= pygame.time.get_ticks()
        if time_now-last_pipe_time > timer:
            pipe_height= random.randint(-100, 100)
            pipe1= Pipes(864, 800/2+ pipe_height,"down")
            pipe2= Pipes(864, 800/2+pipe_height, "up")
            pipegroup.add(pipe1)
            pipegroup.add(pipe2)
            last_pipe_time= time_now
        pipegroup.update()
    #checking score
    if len(pipegroup)> 0:
        if birdgroup.sprites()[0].rect.left> pipegroup.sprites()[0].rect.left and birdgroup.sprites()[0].rect.right< pipegroup.sprites()[0].rect.right and passpipe==False:
            passpipe=True
        if passpipe==True:
            if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.right:
                score+=1
                passpipe=False
    font=pygame.font.SysFont("Arial", 30)
    message=font.render("Score"+str(score),True, "red")
    screen.blit(message, (100,30 ))
    
    
    
    

    pygame.display.update()

        