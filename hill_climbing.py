import random

N = 4

def generate_board():
    return [random.randint(0, N - 1) for _ in range(N)]

def count_conflicts(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_best_neighbor(state):
    current_conflicts = count_conflicts(state)
    best_state = list(state)
    best_conflicts = current_conflicts
    neighbors = []

    for col in range(N):
        original_row = state[col]
        for row in range(N):
            if row == original_row:
                continue
            
            neighbor_state = list(state)
            neighbor_state[col] = row
            neighbor_conflicts = count_conflicts(neighbor_state)
            
            if neighbor_conflicts < best_conflicts:
                best_conflicts = neighbor_conflicts
                neighbors = [neighbor_state]
            elif neighbor_conflicts == best_conflicts:
                neighbors.append(neighbor_state)
                
    if neighbors:
        return random.choice(neighbors), best_conflicts
    
    return state, current_conflicts

def print_board(state):
    for row in range(N):
        line = ""
        for col in range(N):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

def hill_climbing():
    restarts = 0
    while True:
        current_state = generate_board()
        current_conflicts = count_conflicts(current_state)
        
        while True:
            neighbor, neighbor_conflicts = get_best_neighbor(current_state)
            
            if neighbor_conflicts == 0:
                return neighbor, restarts
                
            if neighbor_conflicts >= current_conflicts:
                break
                
            current_state = neighbor
            current_conflicts = neighbor_conflicts
            
        restarts += 1

if __name__ == "__main__":
    solution, total_restarts = hill_climbing()
    print(f"Solution: {solution}")
    print(f"Restarts: {total_restarts}\n")
    print_board(solution)
