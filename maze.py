import pygame
import speech_recognition as sr
import threading

# Pygame setup
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("jumpscare.wav")
background = pygame.image.load("jump2.jpg")
back1 = pygame.image.load("star.jpeg")

WIDTH, HEIGHT = 500, 500
WHITE, RED, BLUE, BLACK = (255, 255, 255), (255, 0, 0), (0, 0, 255), (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Speech Recognition Game")

# Font setup
font = pygame.font.SysFont("Arial", 24)

# Ball and movement setup
ball_radius = 10
ball_dx, ball_dy = 0.5, 0.5
ball_x, ball_y = 30, 50
movingUP, movingDown, movingRight, movingLeft = False, False, False, False
collision = False
running = True
last_command = "Listening..."
win = False

clock = pygame.time.Clock()
FPS = 30

# Speech recognizer setup
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = False
recognizer.energy_threshold = 50  # Lower for faster processing

# Rectangle class
class Rectangles:
    def __init__(self, coords, color, w):
        self.coords = coords
        self.color = color
        self.w = w

    def display(self):
        pygame.draw.rect(screen, self.color, self.coords, self.w)

# Maze walls
rectangles_array = [
    Rectangles((0, 0, 2, 300), "PINK", 2),
    Rectangles((100, 0, 2, 250), "PINK", 2),
    Rectangles((0, 300, 300, 2), "PINK", 2),
    Rectangles((100, 250, 100, 2), "YELLOW", 2),
    Rectangles((200, 150, 2, 100), "YELLOW", 2),
    Rectangles((200, 150, 50, 2), "YELLOW", 2),
    Rectangles((250, 100, 2, 50), "GREEN", 2),
    Rectangles((250, 100, 250, 2), "GREEN", 2),
    Rectangles((300, 200, 2, 100), "GREEN", 2),
    Rectangles((300, 200, 100, 2), "YELLOW", 2),
    Rectangles((400, 200, 2, 200), "PINK", 2),
    Rectangles((495, 100, 2, 350), "ORANGE", 2),
    Rectangles((0, 450, 500, 2), "PURPLE", 2),
    Rectangles((0, 400, 400, 2), "PURPLE", 2)
]

# Collision detection
def collisions():
    global collision
    for rect in rectangles_array:
        if rect.coords[2] != 2:  # Horizontal walls
            if (rect.coords[0] <= ball_x <= rect.coords[0] + rect.coords[2] and 
                abs(ball_y - rect.coords[1]) <= 10):
                collision = True
                break
        else:  # Vertical walls
            if (rect.coords[1] <= ball_y <= rect.coords[1] + rect.coords[3] and 
                abs(ball_x - rect.coords[0]) <= 10):
                collision = True
                break

# Voice command listener
def listen_for_commands():
    global movingUP, movingDown, running, movingRight, movingLeft, last_command

    while running:
        try:
            with sr.Microphone() as mic:
                last_command = "Listening..."
                audio = recognizer.listen(mic, timeout = 7.0, phrase_time_limit = 2)
                text = recognizer.recognize_google(audio).lower()
                last_command = f"Command: {text}"
                print(last_command)

                if "up" in text:
                    movingUP, movingDown, movingRight, movingLeft = True, False, False, False
                elif "down" in text:
                    movingDown, movingUP, movingRight, movingLeft = True, False, False, False
                elif "right" in text:
                    movingRight, movingUP, movingDown, movingLeft = True, False, False, False
                elif "left" in text:
                    movingLeft, movingUP, movingDown, movingRight = True, False, False, False
                elif "stop" in text:
                    movingUP = movingDown = movingRight = movingLeft = False
                elif text == "please quit":
                    running = False

        except (sr.UnknownValueError, sr.WaitTimeoutError):
            last_command = "Couldn't recognize command."

# Start speech recognition in a thread
threading.Thread(target=listen_for_commands, daemon=True).start()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ball movement updates
    if movingUP: ball_y -= ball_dy
    if movingDown: ball_y += ball_dy
    if movingRight: ball_x += ball_dx
    if movingLeft: ball_x -= ball_dx
    if (ball_y >= 400 and ball_y <= 500) and (ball_x - 10) <=0:
        win = True
    collisions()

    # Drawing the game screen
    if not collision and not win:
        screen.fill(WHITE)
        screen.blit(back1, (0,0))
        pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
        for rect in rectangles_array:
            rect.display()
        # Display last recognized command
        command_text = font.render(last_command, True, WHITE)
        screen.blit(command_text, (20, HEIGHT - 40))
    elif collision:
        screen.blit(background, (0, 0))
        sound.play()
    elif win:
        screen.fill(WHITE)
        win_text = font.render("YOU WIN", True, BLACK)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
