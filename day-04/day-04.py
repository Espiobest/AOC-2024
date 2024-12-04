with open('data.txt', 'r') as r:
    grid = r.read().splitlines()
    p1 = 0
    # horizontal
    for row in grid:
        p1 += row.count("XMAS") + row.count("SAMX")

    # vertical
    for col in range(len(grid[0])):
        col_str = "".join(row[col] for row in grid)
        p1 += col_str.count("XMAS") + col_str.count("SAMX")
    
    # diagonal
    for i in range(len(grid) - 3):
        for j in range(len(grid[0]) - 3):
            main = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3]
            off = grid[i][j + 3] + grid[i + 1][j + 2] + grid[i + 2][j + 1] + grid[i + 3][j]
            p1 += main.count("XMAS") + off.count("XMAS")
            p1 += main.count("SAMX") + off.count("SAMX")
    
    print("Part 1:", p1) 


    p2 = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            main = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
            off = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
            if main in ["MAS", "SAM"]:
                p2 += off == "MAS" or off == "SAM"
    
    print("Part 2:", p2)
