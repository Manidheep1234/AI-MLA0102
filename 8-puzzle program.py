from queue import PriorityQueue

goal = [[1,2,3],[4,5,6],[7,8,0]]

def move(state, pos, new_pos):
    s = [row[:] for row in state]
    s[pos[0]][pos[1]], s[new_pos[0]][new_pos[1]] = s[new_pos[0]][new_pos[1]], s[pos[0]][pos[1]]
    return s

def get_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0: moves.append(move(state, (i,j), (i-1,j)))
                if i < 2: moves.append(move(state, (i,j), (i+1,j)))
                if j > 0: moves.append(move(state, (i,j), (i,j-1)))
                if j < 2: moves.append(move(state, (i,j), (i,j+1)))
                return moves

def heuristic(state):
    return sum(state[i][j] != goal[i][j] for i in range(3) for j in range(3))

def solve_puzzle(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), start))
    visited = set()
    while not pq.empty():
        _, state = pq.get()
        if state == goal:
            return "Goal Reached!"
        visited.add(str(state))
        for move_state in get_moves(state):
            if str(move_state) not in visited:
                pq.put((heuristic(move_state), move_state))
    return "No Solution"

start = [[1,2,3],[5,0,6],[4,7,8]]
print(solve_puzzle(start))
