import os.path
from sys import exit

import pgnparser
import pawn
import pieces

SPACE = " "
FILES, RANKS = "abcdefgh", "12345678"
START = "RNBQKBNR" + "P" * 8 + " " * 32 + "p" * 8 + "rnbqkbnr"


def setup():
    squares = [y + x for x in '12345678' for y in 'ABCDEFGH']
    board_view = dict(zip(squares, START))
    piece_view = {_: [] for _ in 'BKNPQRbknpqr'}
    for square in squares:
        piece = board_view[square]
        if piece != SPACE:
            piece_view[piece].append(square)
    return board_view, piece_view


def make_one_move(move, board_view, piece_view):
    if move[0] in "Pp":
        return pawn.make_pawn_move(move, board_view, piece_view)
    if "Oo" in move:
        return pieces.castle(move, board_view, piece_view)
    return pieces.move_piece(move, board_view, piece_view)


def display_position(b):
    print(b)


def make_moves(pgnfile, MOVE_BY_MOVE = False):
    if not os.path.exists(pgnfile):
        print(f'PGN File {pgnfile} not found')
        exit(1)
    board_view, piece_view = setup()

    moves = pgnparser.pgn_to_moves(pgnfile)
    for wmove, bmove in moves[:-1]:
        board_view, piece_view = make_one_move(wmove, board_view, piece_view)
        board_view, piece_view = make_one_move(bmove, board_view, piece_view)
        if MOVE_BY_MOVE:
            display_position(board_view)

    wmove, bmove = moves[-1]
    board_view, piece_view = make_one_move(wmove, board_view, piece_view)
    if len(bmove) > 0:
        board_view, piece_view = make_one_move(bmove, board_view, piece_view)
    display_position(board_view)
    exit(0)

if __name__ == "__main__":
    make_moves("pgn_file_chess.txt")






