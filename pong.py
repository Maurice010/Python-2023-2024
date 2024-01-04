import sys
import random
import pygame

# PLAYER
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, up_key, down_key):
        pygame.sprite.Sprite.__init__(self, game.allSprites)
        self.image = pygame.Surface((20, 120))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.Vector2(0, 0)

        self.up_key = up_key
        self.down_key = down_key

        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.velocity.y = -8
        elif keys[self.down_key]:
            self.velocity.y = 8
        else:
            self.velocity.y = 0

        self.rect.y += self.velocity.y
        if self.rect.bottom >= height:
            self.rect.bottom = height
        elif self.rect.top <= 0:
            self.rect.top = 0

        collisions = pygame.sprite.spritecollide(self, game.allSprites, False)
        for sprite in collisions:
            if sprite == game.ball:
                game.ball.bounce(self.rect.centery)

# COMPUTER PLAYER
class ComputerPlayer(Player):
    def update(self):
        ball_center_y = game.ball.rect.centery
        player_center_y = self.rect.centery

        if ball_center_y > player_center_y:
            self.velocity.y = 6
        elif ball_center_y < player_center_y:
            self.velocity.y = -6
        else:
            self.velocity.y = 0

        self.rect.y += self.velocity.y
        if self.rect.bottom >= height:
            self.rect.bottom = height
        elif self.rect.top <= 0:
            self.rect.top = 0

        collisions = pygame.sprite.spritecollide(self, game.allSprites, False)
        for sprite in collisions:
            if sprite == game.ball:
                game.ball.bounce(self.rect.centery)

# BALL
class Ball(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites)
        self.game = game
        self.radius = 15
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(10, 10)

    def update(self):
        if (self.rect.top <= 0) or (self.rect.bottom >= height):
            self.velocity.y *= -1
        if (self.rect.right >= game.width):
            self.rect.center = game.width // 2, random.randint(self.rect.height, game.height - self.rect.height)
            self.velocity.x *= -1
        if (self.rect.left <= 0):
            self.rect.center = game.width // 2, random.randint(self.rect.height, game.height - self.rect.height)
            self.velocity.x *= -1

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def bounce(self, player_centery):
        temp = self.rect.centery - player_centery
        if temp >= 0:
            self.velocity.y = abs(self.velocity.y)
        else:
            self.velocity.y = -abs(self.velocity.y)
        self.velocity.x *= -1

# GAME
class Game:
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)

        self.font = pygame.font.Font(None, 36)
        self.game_over_text = None

        self.vs_computer = True

    def new_round(self):
        self.ball.velocity = pygame.Vector2(random.choice([-10, 10]), random.choice([-10, 10]))

    def new(self):
        self.allSprites = pygame.sprite.Group()
        self.select_mode()
        if self.vs_computer:
            self.player1 = Player(self, width - 40, height // 2 - 60, pygame.K_UP, pygame.K_DOWN)
            self.player2 = ComputerPlayer(self, 20, height // 2 - 60, None, None)
        else:
            self.player1 = Player(self, width - 40, height // 2 - 60, pygame.K_UP, pygame.K_DOWN)
            self.player2 = Player(self, 20, height // 2 - 60, pygame.K_w, pygame.K_s)
        self.ball = Ball(self, width // 2, height // 2)
    
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if self.game_over_text:
                    if event.key == pygame.K_y:
                        self.reset_game()
                    elif event.key == pygame.K_n:
                        self.quit()

    def update(self):
        self.allSprites.update()

        if (self.ball.rect.right >= self.width):
            self.player1.score += 1
            if self.player1.score == 11:
                self.game_over("Player 1 wins!")
            else:
                self.new_round()

        if (self.ball.rect.left <= 0):
            self.player2.score += 1
            if self.player2.score == 11:
                self.game_over("Player 2 wins!")
            else:
                self.new_round()

    def draw(self):
        self.screen.fill("black")
        self.allSprites.draw(self.screen)

        player1_score_text = self.font.render(f"Player 1: {self.player1.score}", True, (255, 255, 255))
        self.screen.blit(player1_score_text, (10, 10))

        player2_score_text = self.font.render(f"Player 2: {self.player2.score}", True, (255, 255, 255))
        self.screen.blit(player2_score_text, (self.width - player2_score_text.get_width() - 10, 10))

        if self.game_over_text:
            self.screen.blit(self.game_over_text, (self.width // 2 - self.game_over_text.get_width() // 2, self.height // 2))

        pygame.display.flip()

    def reset_game(self):
        self.player1.score = 0
        self.player2.score = 0
        self.new_round()
        self.game_over_text = None

    def game_over(self, winner_text):
        self.game_over_text = self.font.render(f"{winner_text} Another round? Press y/n", True, (255, 255, 255))
        self.ball.velocity.x = 0
        self.ball.velocity.y = 0

    def quit(self):
        pygame.quit()
        sys.exit()

    def select_mode(self):
        self.screen.fill("black")
        vs_computer_text = self.font.render("Play vs computer: Press 1", True, (255, 255, 255))
        vs_player_text = self.font.render("Play vs player: Press 2", True, (255, 255, 255))
        self.screen.blit(vs_computer_text, (self.width // 2 - vs_computer_text.get_width() // 2, self.height // 2 - 50))
        self.screen.blit(vs_player_text, (self.width // 2 - vs_player_text.get_width() // 2, self.height // 2))
        pygame.display.flip()

        mode_selected = False
        while not mode_selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.vs_computer = True
                        mode_selected = True
                    elif event.key == pygame.K_2:
                        self.vs_computer = False
                        mode_selected = True

# INITIALIZE GAME
size = (width, height) = (1000, 600)
title = 'Ping Pong'

game = Game(width, height, title)
game.new()
game.run()