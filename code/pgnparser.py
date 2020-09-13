import re
FILES = "abcdefgh"
RANKS = '12345678'
SPACE = " "


def pgn_to_moves(game_file: str) -> [str]:
    raw_pgn = " ".join([line.strip() for line in open(game_file)])
    comments_marked = raw_pgn.replace("{", "<").replace("}", ">")
    comments_removed = re.sub("<[^>]*>", " ", comments_marked)

    str_marked = comments_removed.replace("[", "<").replace("]", ">")
    str_removed = re.sub("<[^>]*>", " ", str_marked)

    move_num = re.compile("[1-9][0-9]* *\.")
    just_moves = [_.strip() for _ in move_num.split(str_removed)]

    last_move = just_moves[-1]
    result = re.compile("( *1 *- *0 * | *0 *- *1 * | *1/2 *- *1/2 *)")
    last_move = result.sub("", last_move)

    return [pre_process_a_move(_) for _ in just_moves[1:-1]] + [pre_process_last_move(last_move)]


def clean(raw_move):
    return ''.join(filter(str.isalnum, raw_move))


def pre_process_a_move(move: str) -> (str, str):
    wmove, bmove = move.strip().split()
    if wmove[0] in FILES and wmove[1] in RANKS + "x":
        wmove = "P" + wmove
    if bmove[0] in FILES and bmove[1] in RANKS + "x":
        bmove = "p" + bmove
    else:
        bmove = bmove.lower()
    return clean(wmove), clean(bmove)


def pre_process_last_move(move):
    if SPACE in move:
        return pre_process_a_move(move)
    else:
        if move[0] in "abcdefgh":
            return "P" + clean(move)
        else:
            return clean(move),




