import math
import random


def get_board_cost(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def get_neighbor_board(state):
    neighbor = list(state)
    random_row = random.randint(0, 3)
    new_column = random.randint(0, 3)
    neighbor[random_row] = new_column
    return neighbor


def solve_4_queens(max_iter=1000, init_temp=5.0, cooling_rate=0.92):
    current_state = [random.randint(0, 3) for _ in range(4)]
    current_cost = get_board_cost(current_state)
    temp = init_temp

    for iteration in range(max_iter):
        if current_cost == 0:
            return current_state, iteration

        neighbor = get_neighbor_board(current_state)
        neighbor_cost = get_board_cost(neighbor)
        delta_cost = neighbor_cost - current_cost

        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temp):
            current_state = neighbor
            current_cost = neighbor_cost

        temp *= cooling_rate

    return current_state, max_iter


def print_board(state):
    for col in state:
        row_str = [" . "] * 4
        row_str[col] = " Q "
        print("".join(row_str))


solution, steps = solve_4_queens()
print_board(solution)
