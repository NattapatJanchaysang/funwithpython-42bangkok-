from checkmate import checkmate

def main():

    board1 = """\
R...
.K..
..P.
....\
""" 
    print(board1)
    print("Test 1:")
    checkmate(board1)
    
    
    board2 = """\
..
.K
..\
""" 
    
    print("Test 2:")
    checkmate(board2)

    
    board3 = """\
.K.
P..
...\
"""
    print("Test 3 (Pawn Check):")
    checkmate(board3)

    
    board4 = """\
K...
P...
R...\
"""
    print("Test 4 (Blocked):")
    checkmate(board4)

if __name__ == "__main__":
    main()