import pygame

#mengatur layar
SCREEN_WIDHT= 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'GAME ENDOG'

clock = pygame.time.Clock()





#Mengaur warna backgroud
WHITE =(255, 255 ,255)
BLACK = (0, 0, 0)

class Game:
    TICK_RATE = 60

    def __init__(self,title, widht, height):
        self.title =title
        self.widht = widht
        self.height = height

        #Menampilkan screen
        self.game_screen = pygame.display.set_mode((widht, height))
        self.game_screen.fill(WHITE)
        pygame.display.set_caption(title)


    def run_game_loop(self):
        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('asset/pemain.png',375, 700, 50, 50)

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type ==  pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction =1
                    elif event.key == pygame.K_DOWN:
                        direction = -1    
                elif event.type ==  pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

            print(event)

            player_character.move(direction)
            player_character.draw(self.game_screen)


            pygame.display.update()
            clock.tick(self.TICK_RATE)
    
    
    





class GameObject:
    def __init__(self,image_path, x , y, widht, height):
        self.x_pos = x
        self.y_pos = y
        
        self.widht = widht
        self.height = height

        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image,(widht, height))

    def draw(self, background):
        self.background.blit(self.x_pos, self.y_pos)  


class PlayerCharacter(GameObject):

    SPEED = 10

    def __init__(self,image_path, x , y, widht, height):
        super().__init__(image_path, x , y, widht, height)         

    def move(self,direction):
        if direction  > 0 :
            self.y_pos -= self.SPEED
        elif direction  < 0 :
             self.y_pos += self.SPEED


pygame.init()
new_game = Game(SCREEN_TITLE, SCREEN_HEIGHT, SCREEN_WIDHT)
new_game.run_game_loop()


#Keluar dari program
pygame.quit()
quit()


#pygame.draw.rect(game_screen, BLACK, [350,350, 100, 100])
    #pygame.draw.circle(game_screen, BLACK, (400,300),50)
    
    
    #game_screen.blit(player_image, (375, 375))

#player_image = pygame.image.load('asset/pemain.png')
#player_image = pygame.transform.scale(player_image,(50, 50))