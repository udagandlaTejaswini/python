def is_valid(matrix, x, y, visited):
    rows = len(matrix)
    cols = len(matrix[0])
    return x >= 0 and y >= 0 and x < rows and y < cols and matrix[x][y] == 1 and not visited[x][y]

def is_path(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]

    while stack:
        current_x, current_y = stack.pop()

        if current_x == x and current_y == y:
            return True

        visited[current_x][current_y] = True

        # Move right
        if is_valid(matrix, current_x, current_y + 1, visited):
            stack.append((current_x, current_y + 1))

        # Move down
        if is_valid(matrix, current_x + 1, current_y, visited):
            stack.append((current_x + 1, current_y))

        # Move left
        if is_valid(matrix, current_x, current_y - 1, visited):
            stack.append((current_x, current_y - 1))

        # Move up
        if is_valid(matrix, current_x - 1, current_y, visited):
            stack.append((current_x - 1, current_y))

    return False

# Taking input from the user
rows = int(input())
cols = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))
x = int(input())
y = int(input())

# Checking if there exists a path
if is_path(matrix, x, y):
    print("path found")
else:
    print("path not found")