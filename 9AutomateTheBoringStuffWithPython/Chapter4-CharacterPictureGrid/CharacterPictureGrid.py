#Character Picture Grid
#Written by: Jeff Brusoe
#Last Updated: January 24, 2020


grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]

print("Input:")
for i in range(len(grid)):
    print(grid[i])

print("\nOutput:")

for x in range (len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x],end='')
    print("")
