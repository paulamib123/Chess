Title: PGN Parser

The pgn parser script conatains the following functions:

### **1. pre_process_a_move()**
~~~ python

    def pre_process_a_move(move: str) -> (str, str):
        wmove, bmove = move.strip().split()
        if wmove[0] in FILES and wmove[1] in RANKS + "x":
            wmove = "P" + wmove
            if bmove[0] in FILES and bmove[1] in RANKS + "x":
            bmove = "p" + bmove
            else:
            bmove = bmove.lower()
            return clean(wmove), clean(bmove)
~~~


This function adds "P" to a white pawn and "p" to a black pawn and converts all the pieces of the black move to lowercase (as black pieces are represented by lowercase notation)

### **2. pre_process_last_move()**
~~~ python
    def pre_process_last_move(move):
        if SPACE in move:
            return pre_process_a_move(move)
        else:
            if move[0] in "abcdefgh":
                return "P" + clean(move)
        else:
            return clean(move),
~~~

This function pre process the last move in a similar way as the previous function( 2. pre_process_a_move()).

###  **3. clean()**

~~~ python
    def clean(raw_move):
        return ''.join(filter(str.isalnum, raw_move))
~~~

This function is used to remove any special symbols or punctuations and return the move in the form of alpha numeicals only.

### **4. pgn_to_moves()**

~~~ python
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
~~~
        
        
This function removes all comments from the pgn file which are of the format{ }, [ ] and even the number of the move and replaces them with an empty string.    
This is done by using regular expressions.

This function returns a list of tuples of the moves in the pgn file.

#### **Output Example: -**

_[('Pe4', 'pe5'), ('Nf3', 'nc6'), ('Bb5', 'pa6'), ('Ba4', 'nf6'), ('OO', 'be7'), ('Re1', 'pb5'), ('Bb3', 'pd6'), ('Pc3', 'oo'), ('Ph3', 'nb8'), ('Pd4', 'nbd7'), ('Pc4', 'pc6'), ('Pcxb5', 'paxb5'), ('Nc3', 'bb7'), ('Bg5', 'pb4'), ('Nb1', 'ph6'), ('Bh4', 'pc5'), ('Pdxe5', 'nxe4'), ('Bxe7', 'qxe7'), ('Pexd6', 'qf6'), ('Nbd2', 'nxd6'), ('Nc4', 'nxc4'), ('Bxc4', 'nb6'), ('Ne5', 'rae8'), ('Bxf7', 'rxf7'), ('Nxf7', 'rxe1'), ('Qxe1', 'kxf7'), ('Qe3', 'qg5'), ('Qxg5', 'phxg5'), ('Pb3', 'ke6'), ('Pa3', 'kd6'), ('Paxb4', 'pcxb4'), ('Ra5', 'nd5'), ('Pf3', 'bc8'), ('Kf2', 'bf5'), ('Ra7', 'pg6'), ('Ra6', 'kc5'), ('Ke1', 'nf4'), ('Pg3', 'nxh3'), ('Kd2', 'kb5'), ('Rd6', 'kc5'), ('Ra6', 'nf2'), ('Pg4', 'bd3'), ('Re6',)]_
