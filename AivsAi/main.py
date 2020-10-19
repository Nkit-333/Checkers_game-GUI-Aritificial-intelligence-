import pygame
from AivsAi.play import Game
from AivsAi.minimax_algo import minimax
class comp:
    def start(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.ROWS, self.COLS = 8, 8
        self.SQUARE_SIZE = self.WIDTH//self.COLS
        self.Orange=(255, 128, 0)
        self.FPS = 60
        
        self.WHITE = (255, 255, 255)
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Checkers- AI vs AI')
        run = True
        clock = pygame.time.Clock()
        game = Game(self.WIN)
        while run:

            clock.tick(self.FPS)
        
            if game.turn == self.WHITE:
                value, new_board = minimax(game.get_board(), 4, True, game,game.get_alpha(),game.get_beta())
            #value=value*2
                game.ai_move(new_board)
        
            if game.turn == self.Orange:
                value, new_board = minimax(game.get_board(), 4, False, game,game.get_alpha(),game.get_beta())
                game.ai_move(new_board)
        
            if game.get_board().win_decider() !=None:
                print(game.get_board().win_decider())
                run =False
                pygame.quit()

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

            game.update()
    
        