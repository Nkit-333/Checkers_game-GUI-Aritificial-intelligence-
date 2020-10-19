import pygame
from AI.play import Game
from AI.minimax_algo import minimax
class computer:
    def get_position_input(self,pos,SQUARE_SIZE):
        self.x, self.y = pos
        self.row = self.y // SQUARE_SIZE
        self.col = self.x // SQUARE_SIZE
        return self.row, self.col

    def start(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Checkers- AI vs Humans')
        self.ROWS, self.COLS = 8, 8
        self.SQUARE_SIZE = self.WIDTH//self.COLS
        self.Orange=(255, 128, 0)
        self.FPS = 60
        
        self.WHITE = (255, 255, 255)
        #BLACK = (0, 0, 0)
        #BLUE = (0, 0, 255)
        #GREY = (128,128,128)

        
        run = True
        clock = pygame.time.Clock()
        game = Game(self.WIN)
    #b=board()
        while run:
            clock.tick(self.FPS)
        
            if game.turn == self.WHITE:
                value, new_board = minimax(game.get_board(), 4, self.WHITE, game,game.get_alpha(),game.get_beta())
                game.ai_move(new_board)
        
            if game.get_board().win_decider() !=None:
                print(game.get_board().win_decider())
                run =False
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
    
        