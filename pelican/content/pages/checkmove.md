Title: Checkmove

The checkmove script contains the following function:

### **1. check_move()**

~~~ python
def check_move(piece, initial_position, final_position):

# alpha_to_index is a global variable defined as below:
# alpha_to_index = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}

    r1, f1 = int(alpha_to_index[initial_position[0]]), int(initial_position[1])
    r2, f2 = int(alpha_to_index[final_position[0]]), int(final_position[1])

    if piece == "k":
        return (abs(r2 - r1), abs(f2 - f1)) in [(1, 0), (0, 1)]

    if piece == "q":
        return (f1 == f2 or r1 == r2) or (abs(f1 - f2) == abs(r2 - r1))

    if piece == "r":
        return r1 == r2 or f1 == f2

    if piece == "kn":
        return (abs(f2 - f1), abs(r2 - r1)) in [(1, 2), (2, 1)]

    if piece == "b":
        return abs(f2 - f1) == abs(r2 - r1)

    if piece == "P":
        return r2 == r1 and f2 - f1 == 1

    if piece == "p":
        return r2 == r1 and f1 - f2 == 1
~~~    

This function converts the initial position and the final position in the form of co-ordinates.

**Example:**  
        Position = e4  
        co-ordinates = (5, 4) 

Then it checks if the piece is a king, queen, bishop, rook, knight or a pawn and if the move is valid from the initial position to the final position.
