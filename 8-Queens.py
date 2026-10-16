def solve(row, columns, position):
    if row == 8:
        for r in position:
            print("." * r + "Q" + "." * (7 - r))
        return True
    for col in range(8):
        if col not in columns and all(
            abs(col - position[r]) != row - r
            for r in range(row)
        ):
            if solve(row + 1, columns | {col}, position + [col]):
                return True
    return False
solve(0, set(), [])