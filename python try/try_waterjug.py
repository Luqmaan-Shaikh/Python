from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    visited_states = set()
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state == target:
            return path

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        a, b = current_state

        # Fill jug A
        if a < capacity_a:
            queue.append(((capacity_a, b), path + ['Fill Jug A']))

        # Fill jug B
        if b < capacity_b:
            queue.append(((a, capacity_b), path + ['Fill Jug B']))

        # Empty jug A
        if a > 0:
            queue.append(((0, b), path + ['Empty Jug A']))

        # Empty jug B
        if b > 0:
            queue.append(((a, 0), path + ['Empty Jug B']))

        # Pour water from A to B
        if a > 0 and b < capacity_b:
            pour = min(a, capacity_b - b)
            queue.append(((a - pour, b + pour), path + [f'Pour {pour}L from A to B']))

        # Pour water from B to A
        if b > 0 and a < capacity_a:
            pour = min(b, capacity_a - a)
            queue.append(((a + pour, b - pour), path + [f'Pour {pour}L from B to A']))

    return None

def print_solution_path(solution_path):
    if solution_path:
        print("Solution Steps:")
        for step in solution_path:
            print(f"- {step}")
    else:
        print("No solution found.")

# Define capacities and target state
capacity_a = 4
capacity_b = 3
target_state = (2, 0)

# Solve the water jug problem
solution_path = water_jug_problem(capacity_a, capacity_b, target_state)

# Print the solution
print_solution_path(solution_path)
