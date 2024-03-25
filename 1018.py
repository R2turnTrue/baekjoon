n, m = map(int, input().split())

lines = []

wb = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

bw = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

for i in range(n):
    to_array = [char for char in input()]
    lines.append(to_array)

arr = []

for y in range(len(lines) - 7):
    for x in range(len(lines[y]) - 7):

        wbc = 0
        bwc = 0

        for y2 in range(8):
            for x2 in range(8):
                if wb[y2][x2] != lines[y + y2][x + x2]:
                    wbc += 1
                
                if bw[y2][x2] != lines[y + y2][x + x2]:
                    bwc += 1
        
        arr.append(wbc)
        arr.append(bwc)

print(min(arr))