Title: Pieces

This script consists of the followinng functions:

#### **1. castle()**

~~~ python

def castle(move, board_view, piece_view):

    home_rank, king, rook = "1", "K", "R" if move[0] == "O" else "8", "k", "r"

    king_before = "e" + home_rank
    rook_before = ("a" if len(move) == 3 else "h") + home_rank

    king_after = ("c" if len(move) == 3 else "g") + home_rank
    rook_after = ("d" if len(move) == 3 else "f") + home_rank

    board_view[king_before] = SPACE
    board_view[king_after] = king

    board_view[rook_before] = SPACE
    board_view[rook_after] = rook

    piece_view[king] = [king_after]
    piece_view[rook].append(rook_after)
    piece_view[rook].remove(rook_before)

    return board_view, piece_view
~~~

This function is used to make the castling move.

It finds the current position of the king and rook and also the final position of the king and rook and removes the king and rook from their current positions and adds them to the final position.

This function returns the board view and the piece view after castling.


#### **2. not_blocked()**

~~~ python
def not_blocked(board_view, a, b):
    if a > b:
        a, b = b, a

        if a[0] == b[0]:
            between = [a[0] + r for r in "12345678" if a[1] < r < b[1]]
        elif a[1] == b[1]:
            between = [f + a[0] for f in "12345678" if a[0] < f < b[0]]
        else:
            between = DIAGONAL
    return [board_view[sq] for sq in between].count(SPACE) == len(between)
~~~

This function checks i their is any other piece present between the current position and the final position.

It first creates a list of pieces between the current and final position and returns 'True' if the count of spaces in the list is same as the length of the list i.e there are empty blocks between the final and current positions. It returns 'False' if there is a single piece present between the current position and the final position.


#### **3. get_from_square()**

~~~ python
def get_from_square(move, board_view, candidates):
    piece = move[0]
    to_square = move[-2:]
    if piece in "nN":
        for from_square in candidates:
            if checkmove.check_move(piece, from_square, to_square):
                return from_square
    for from_square in candidates:
        if checkmove.check_move(piece, from_square, to_square):
            if not_blocked(board_view, from_square, to_square):
                return from_square
~~~

This function is used to get the current position of the piece if the if it is not specified in the pgn notation.

It takes a list of candidates i.e the list of position of the piece and then checks if the move from the current position to the final position is valid. 

If it is any piece other than the knight then it also checks if the piece is blocked by using the not_blocked() function. (described above)


#### **4. move_piece()**

~~~ python
def move_piece(move, board_view, piece_view):
    piece, to_square = move[0], move[-2:]

    capture = "x" in move
    if capture:
        move = move[:-3] + move[-2:]
        captured_piece = board_view[to_square]
        piece_view[captured_piece].remove(to_square)

    if len(move) == 5:
        from_square = move[1:3]
    elif len(piece_view[piece]) == 1:
        from_square = piece_view[piece][0]
    else:
        from_square = get_from_square(move, board_view, piece_view[piece])

    board_view[from_square] = SPACE
    board_view[to_square] = piece

    piece_view[piece].append(to_square)
    piece_view[piece].remove(from_square)

    return board_view, piece_view
~~~

This function examines if the move is a capture. If it is a capture it removes the piece ot has captured i.e the piece at the final position and adds the piece which captured the other piece to the final position.

If the current position is not found it generates the current position using the get_from_square() function (described above).
Then it removes the piece from the current position and appends the piece in the new position.



   
