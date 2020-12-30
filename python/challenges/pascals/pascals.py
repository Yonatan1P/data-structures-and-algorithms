def printPascal(n=0):
    if type(n) != int:
        return

    output = []
    for line in range(1, n + 1):
        current = 1
        current_line = []
        for i in range(1, line + 1):
                # The first value in a
                # line is always 1
                current_line += [current]
                current = int(current * (line - i) / i)
        output += [current_line]
    return output
