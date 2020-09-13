alpha_to_index = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}


def is_valid_position(r, f):
    return


def check_move(piece, initial_position, final_position):
    r1, f1 = int(alpha_to_index[initial_position[0]]), int(initial_position[1])
    r2, f2 = int(alpha_to_index[final_position[0]]), int(final_position[1])

    if not is_valid_position(r2, f2):
        return False

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











