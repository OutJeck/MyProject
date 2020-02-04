def chess_puzzle(t, q):
    '''
    (str, str) -> set

    >>> chess_puzzle('b5', 'f4')
    {'d8', 'g8', 'h1', 'c2', 'c6', 'e1', 'c8',
     'h3', 'e8', 'h8', 'a1', 'g7', 'g6', 'e6',
     'd1', 'd3', 'a2', 'h7', 'a7', 'c3', 'e7',
     'g2', 'e2', 'a8', 'd7', 'a6', 'g1', 'a3'}
    '''
    lst = []
    for i in range(8):
        for j in range (8):
            lst.append(str(chr(i+97)+str(j+1)))
    tour_lst = []
    for i in range(8):
        tour_lst.append(str(chr(i+97) + t[1]))
        tour_lst.append(t[0] + str(i+1))
    tour_lst.pop(tour_lst.index(t))


    queen_lst = []
    temp_q = q
    for i in range(8):
        queen_lst.append(str(chr(i+97) + q[1]))
        queen_lst.append(q[0] + str(i+1))
    queen_lst.pop(queen_lst.index(q))
    n = 0
    while temp_q[0] != "h" and temp_q[1] != '8':
        queen_lst.append(chr(ord(temp_q[0])+1)+str(int(temp_q[1])+1))
        temp_q = chr(ord(temp_q[0])+1) + str(int(temp_q[1])+1)
    temp_q = q

    while temp_q[0] != "h" and temp_q[1] != '1':
        queen_lst.append(chr(ord(temp_q[0])+1)+str(int(temp_q[1])-1))
        temp_q = chr(ord(temp_q[0])+1) + str(int(temp_q[1])-1)
    temp_q = q

    while temp_q[0] != "a" and temp_q[1] != '8':
        queen_lst.append(chr(ord(temp_q[0])-1)+str(int(temp_q[1])+1))
        temp_q = chr(ord(temp_q[0])-1) + str(int(temp_q[1])+1)
    temp_q = q

    while temp_q[0] != "a" and temp_q[1] != '1':
        queen_lst.append(chr(ord(temp_q[0])-1)+str(int(temp_q[1])-1))
        temp_q = chr(ord(temp_q[0])-1) + str(int(temp_q[1])-1)


    for el in tour_lst:
        if el in lst:
            lst.pop(lst.index(el))

    for el in queen_lst:
        if el in lst:
            lst.pop(lst.index(el))

    return set(lst)


print(chess_puzzle('b5', 'f4'))
