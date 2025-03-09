def print_board(board, n):
    """Helper function to print the chessboard."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
   
    for i in range(row):
        if board[i][col]:
            return False

  
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

   
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row, n):
    """Recursive function to place queens dynamically."""
    if row == n: 
        print_board(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1 
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0 

    return False

def n_queens(n):
    """Main function to solve N-Queens dynamically."""
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")
    else:
        print("Solution found!")


n_queens(8)
