size = 10
moves = [3, 2, -1, 5, -8, 2]
def simulate_movement(board_size,moves_list):
    position=0
    for i in moves_list:
        position+=i
        if position<0:
            position=0
        elif position>=board_size:
            position=board_size-1
    return position
final_pos = simulate_movement(size,moves)
print(final_pos)
