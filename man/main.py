import pygame
from man.play import Game 
class human:

    def get_position_input(self,pos,SQUARE_SIZE):
        self.x, self.y = pos
        self.row = self.y // SQUARE_SIZE
        self.col = self.x // SQUARE_SIZE
        return self.row, self.col

    def start(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Checkers')
        self.ROWS, self.COLS = 8, 8
        self.SQUARE_SIZE = self.WIDTH//self.COLS
        self.Orange=(255, 128, 0)
        self.FPS = 60
        run = True
        clock = pygame.time.Clock()
        game = Game(self.WIN)

        while run:
            clock.tick(self.FPS)

            if game.winner() != None:
                print(game.winner())
                run = False
                pygame.quit()
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.row, self.col = self.get_position_input(self.pos,self.SQUARE_SIZE)
                    game.select(self.row, self.col)

            game.update()
    
    

