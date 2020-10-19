from copy import deepcopy
import pygame
import math
from random import shuffle
Orange = (255, 128, 0)
WHITE = (255, 255, 255)

def minimax(Board_position, depth, select_player, game,alp,bet):
    if depth == 0 or Board_position.win_decider() != None :
        return Board_position.score(), Board_position 
    if select_player:
        max_val = -math.inf
        byfar_best = None

        #Exploration
        for move in Explore_moves2(Board_position, WHITE, game):
            Check = minimax(move, depth-1, False, game,alp,bet)
            Check=Check[0]
            max_val = max(max_val, Check)
            if max_val == Check:
                byfar_best = move
                alphaa=max(alp,max_val)
                if (bet<=alp):
                    game.set_alpha(alphaa)
                    break 
        
        return max_val, byfar_best

    elif select_player == False:
        min_val = -math.inf
        byfar_best = None
        #Exploration
        for move in Explore_moves(Board_position, Orange, game):
            Check = minimax(move, depth-1, True, game,alp,bet)
            Check=Check[0]
            min_val = min(min_val, Check)
            bet_a=min(game.get_beta(),min_val)
            if (bet<=alp):
                game.set_beta(bet_a)
                break 
            if min_val == Check:
                byfar_best = move
               
        
        return min_val, byfar_best


def move_piece(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def Explore_moves2(board, color, game):
    moves = []
    lis=[]
    for piece in board.get_all_pieces(color):
        lis.append(piece)
    #x = [[i] for i in range(len(lis))]
    shuffle(lis)
    for piece in lis:
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.fetch_piece(piece.row, piece.col)
            new_board = move_piece(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

def Explore_moves(board, color, game):
    moves = []
    pieces=[]
    
    for piece in  board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.fetch_piece(piece.row, piece.col)
            new_board = move_piece(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    pygame.display.update()

