# Kesimpulan
# Install Python dan Pygame
# Dasar Pemrograman Python (Variable, Collections, Control Flow, Function, Classes)
# Develop Game sambil belajar mengenai Pygame

# Mengakses Library Pygame
import pygame, sys

# Mengatur ukuran layar
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Memberikan Judul Game
SCREEN_TITLE = 'Cross The Road'

#mengatur warna background (RGB Code)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Attribute clock digunakan untuk update game event dan frame
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('ComicSans', 75)

class Game:

    # Frame rate yg digunakan 60 frame per detik
    TICK_RATE = 60

    # Inisialisasi Class Game untuk set up width, height, dan Title
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width= width
        self.height = height

        # Menampilkan screen dengan ukuran spesifik
        self.game_screen = pygame.display.set_mode((width, height))
        # Memberi warna putih pada game screen
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        # Load and Set background image untuk layar game
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('asset/pemain.png', 520, 700, 50, 50)
        enemy_0 = EnemyCharacter('asset/musuh1.png', 20, 450, 50, 50)
        # Kecepatan naik ketika telah mencapai Goal
        enemy_0.SPEED *= level_speed

        # Membuat musuh baru
        enemy_1 = EnemyCharacter('asset/musuh2.png', self.width - 40, 300, 50, 50)
        enemy_1.SPEED *= level_speed

        # Membuat musuh baru
        enemy_2 = EnemyCharacter('asset/musuh3.png', 20, 150, 50, 50)
        enemy_2.SPEED *= level_speed

        OnePiece = GameObject('asset/onepiece.png', 520, 50, 50, 50)

        # Main game loop, digunakan untuk update semua gameplay seperti movement, checks, dan graphic
        # Berjalan sampai is_game_over = True
        while not is_game_over:

            for event in pygame.event.get():
                # ketika kita menekan tombol keluar (esc), maka akan keluar dari game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Terdeteksi ketika menekan panah turun
                elif event.type == pygame.KEYDOWN:
                    # Player bergerak ke atas
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Ketika panah/arah dilepaskan
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # ketika menekan panah naik
                elif event.type == pygame.KEYUP:
                    # Gerakan player berhenti
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))

            OnePiece.draw(self.game_screen)
            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            # Move and draw more enemies when we reach higher levels of difficulty
            if level_speed > 2:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)
            if level_speed > 4:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)

            if player_character.detection_collision(OnePiece):
                is_game_over = True
                did_win = True
                text = font.render('You Win! :)', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detection_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You Lose! :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detection_collision(enemy_1):
                is_game_over = True
                did_win = False
                text = font.render('You Lose! :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detection_collision(enemy_2):
                is_game_over = True
                did_win = False
                text = font.render('You Lose! :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            pygame.display.update()
            clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

# Generic game object class to be subclassed by other objects in the game
class GameObject:
    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


# Class to represent the character contolled by the player
class PlayerCharacter(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50

    # Return False (no collision) jika posisi player baik di sumbu x dan y,
    # tidak bertabrakan dengan tubuh enemy
    def detection_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True

# Class to represent the enemies moving left to right and right to left
class EnemyCharacter(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

pygame.init()



SCREEN = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("asset/backgroundmenu.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)

def play():
    while True:

        new_game = Game('asset/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
        new_game.run_game_loop(0.5)
        
        #keluar dari program
        pygame.quit()
        quit()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(540, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("asset/Play Rect.png"), pos=(540, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("asset/Quit Rect.png"), pos=(540, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()