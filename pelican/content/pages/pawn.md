Title: Pawn

This script consists of four small functions which checks if the move is a regular pawn move, pawn promotion, enpassant or a capture.
They use regular expressions to check for the type of move.

The four functions are as follows:

~~~python
def is_regular_pawn_move(move):
    return re.fullmatch("[Pp][a-h][2-7]", move) is not None


def is_capture(move):
    return re.fullmatch("[Pp][a-h]x?[a-h][2-7]?", move) is not None


def is_promotion(move):
    return re.fullmatch("[Pp][a-h](x[a-h])?[18])[RNBQrnbq]", move) is not None


def is_enpassant(move):
    return move.endswith("ep")
~~~

#### **1. capture()**

~~~python

def capture(move, board_view, piece_view):
    move = move.replace("x", "")
    pawn, from_file, to_square = move[0], move[1], move[2:]
    captured_piece = board_view[to_square]
    board_view[to_square] = pawn

    to_rank = to_square[1]
    from_square = from_file + can_capture_from[pawn][to_rank]

    board_view[from_square] = SPACE
    piece_view[captured_piece].remove(to_square)

    return board_view, piece_view
~~~

This function checks if the letter "x" is present in the move i.e it checks if the move is a capture.

Then it removes the piece which is captured and adds the piece which performed the capture to the final position and accordingly updates the board view and piece view.

#### **2. make_enpassant()**

~~~python
def make_enpassant(move, board_view, piece_view):
    move = move.replace("x", "")
    pawn, from_file, to_square = move[0], move[1], move[2:4]
    to_file = to_square[0]

    from_square = from_file + enpassant_captured[pawn]
    captured_pawn_square = to_file + enpassant_captured[pawn]

    board_view[to_square] = pawn
    board_view[from_square] = SPACE
    board_view[captured_pawn_square] = SPACE

    piece_view[pawn].remove(from_square)
    piece_view[pawn].append(to_square)
    piece_view[pawn.swapcase()].remove(captured_pawn_square)

    return board_view, piece_view
~~~

This function checks if the move is an enpassant and then gets the current position of the pawn and the current position of the captured pawn as well as the final position of the pawn which has performed the capture and finally updates the board view and piece view by removing the captured pawn and adding the pawn which performed the capture to the final position.

#### **3. capture()**

~~~python
def capture(move, board_view, piece_view):
    move = move.replace("x", "")
    pawn, from_file, to_square = move[0], move[1], move[2:]
    captured_piece = board_view[to_square]
    board_view[to_square] = pawn

    to_rank = to_square[1]
    from_square = from_file + can_capture_from[pawn][to_rank]

    board_view[from_square] = SPACE
    piece_view[captured_piece].remove(to_square)

    return board_view, piece_view
~~~

This function gets the current position of the pawn and the final position of the pawn i.e the position at which the captured piece is present and then it removes the captured pawn and adds the pawn which performed the capture to the position of the captured piece.

#### **4. move_pawn()**

~~~python
def move_pawn(move, board_view,piece_view):
    pawn, to_square = move[0], move[1:]
    to_file, to_rank = to_square[0], to_square[1:]
    for move_from in can_move_from[pawn][to_rank]:
        from_square = to_file + move_from
        if board_view[from_square] == pawn:
            board_view[from_square] = SPACE
            board_view[to_square] = pawn
            piece_view[pawn].append(to_square)
            piece_view[pawn].remove(from_square)
    return board_view, piece_view
~~~
This function performs a regular pawn move.

It gets the current position and the final position of the pawn and makes the move by removing the pawn from the initial position and adding the pawn to the final position.

#### **5. make_pawn_move()**

~~~python
def make_pawn_move(move, board_view, piece_view):
    if is_regular_pawn_move(move):
        return move_pawn(move, board_view, piece_view)
    if is_capture(move):
        return capture(move, board_view, piece_view)
    if is_promotion(move):
        return promote(move, board_view, piece_view)
    if is_enpassant(move):
        return make_enpassant(move, board_view, piece_view)
~~~

This function checks if the move is a regular pawn move, enpassant, pawn promotion or a pawn capture and then calls the required function accordingly to perform the move.


