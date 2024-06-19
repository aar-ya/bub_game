import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Pop Game")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bubble class
class Bubble:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 20
        self.time_to_turn_red = 3000  # 3 seconds

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, dt):
        self.time_to_turn_red -= dt
        if self.time_to_turn_red <= 0 and self.color == BLUE:
            self.color = RED

# Display text
def display_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Start screen
def start_screen():
    screen.fill(WHITE)
    display_text("Bubble Pop Game", 64, BLACK, WIDTH // 2, HEIGHT // 3)
    display_text("Click to Start", 48, BLACK, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# Game over screen
def game_over_screen(score):
    screen.fill(WHITE)
    display_text("Game Over!", 64, BLACK, WIDTH // 2, HEIGHT // 3)
    display_text(f"Score: {score}", 48, BLACK, WIDTH // 2, HEIGHT // 2)
    display_text("Click to Restart", 48, BLACK, WIDTH // 2, 2 * HEIGHT // 3)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# Game variables
bubbles = []
score = 0
red_bubble_count = 0
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    start_screen()

    bubbles = []
    score = 0
    red_bubble_count = 0
    game_running = True

    while game_running:
        dt = clock.tick(100)  # Time elapsed since last frame in milliseconds
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for bubble in bubbles[:]:
                    if (bubble.x - pos[0]) ** 2 + (bubble.y - pos[1]) ** 2 <= bubble.radius ** 2:
                        if bubble.color == BLUE:
                            bubbles.remove(bubble)
                            score += 1
                        else:
                            red_bubble_count += 1 
                            bubbles.remove(bubble)

        if red_bubble_count > 10:
            game_running = False

        if random.randint(0, 50) == 0:
            new_bubble = Bubble(random.randint(20, WIDTH-20), random.randint(20, HEIGHT-20), BLUE)
            bubbles.append(new_bubble)

        for bubble in bubbles:
            bubble.update(dt)
            bubble.draw(screen)

        pygame.display.flip()

    game_over_screen(score)
