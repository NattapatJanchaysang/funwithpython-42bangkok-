def checkmate(board):
    
    # แปลง String ให้เป็น List ของแถว 
    rows = [row for row in board.split('\n') if len(row) > 0]

    
    if not rows:
        return

    # หาขนาดกระดาน
    height = len(rows)
    width = len(rows[0])

    # หาตำแหน่ง King (K)
    k_row, k_col = -1, -1
    for r in range(height):
        for c in range(width):
            if rows[r][c] == 'K':
                k_row, k_col = r, c
                break
        if k_row != -1:
            break
            
    
    if k_row == -1:
        return

    
    # ทิศตรง: บน, ล่าง, ซ้าย, ขวา
    straights = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # ทิศเฉียง: บนซ้าย, บนขวา, ล่างซ้าย, ล่างขวา
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # เซ็ตของตัวหมาก
    pieces_set = {'K', 'Q', 'B', 'R', 'P'}

    # 1. เช็คแนวตรง (ต้องเจอ Rook หรือ Queen)
    for dr, dc in straights:
        curr_r, curr_c = k_row + dr, k_col + dc
        while 0 <= curr_r < height and 0 <= curr_c < width:
            piece = rows[curr_r][curr_c]
            if piece in pieces_set: # เจอตัวหมาก 
                if piece == 'R' or piece == 'Q':
                    print("Success")
                    return
                else:
                    break # เจอตัวอื่นบังทาง 
            
            curr_r += dr
            curr_c += dc

    # 2. เช็คแนวเฉียง (ต้องเจอ Bishop หรือ Queen หรือ Pawn)
    for dr, dc in diagonals:
        curr_r, curr_c = k_row + dr, k_col + dc
        distance = 1
        while 0 <= curr_r < height and 0 <= curr_c < width:
            piece = rows[curr_r][curr_c]
            if piece in pieces_set: # เจอตัวหมาก
                if piece == 'B' or piece == 'Q':
                    print("Success")
                    return
                elif piece == 'P':
                    
                    #pawn
                    if distance == 1 and dr == 1: 
                        print("Success")
                        return
                    else:
                        break 
                else:
                    break # เจอตัวอื่นบัง
            
            curr_r += dr
            curr_c += dc
            distance += 1

    # รอดทุกทิศทาง
    print("Fail")