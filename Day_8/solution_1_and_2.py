from functools import reduce

map = []
with open("text.txt") as f:
    for line in f.readlines():
        map.append([int(i) for i in list(line[:-1])])

j_max = len(map[0])
i_max = len(map)
invisible = 0
scenic_scores = []
for i in range(1, len(map[0]) - 1):
    for j in range(1, len(map) - 1):
        L = [map[i][l] for l in [x for x in range(j - 1, 0, -1)] + [0]]  # Left
        R = [map[i][r] for r in range(j + 1, j_max)]  # Right
        U = [map[u][j] for u in [x for x in range(i - 1, 0, -1)] + [0]]  # Up
        D = [map[d][j] for d in range(i + 1, i_max)]  # Down

        # invisible
        if len([1 for s in [max(L), max(R), max(U), max(D)] if s < map[i][j]]) == 0:
            invisible += 1
        # sceinic scores
        scores = []
        for view in [L, R, U, D]:
            s = []
            for t in view:
                if map[i][j] > t:
                    s.append(1)
                else:
                    s.append(0)
            try:
                s = s.index(0) + 1
            except:
                s = len(s)
            scores.append(s)
        scenic_scores.append(reduce(lambda x, y: x * y, scores))

print(f"Part 1 Answer = {(j_max * i_max) - invisible}")
print(f"Part 2 Answer = {max(scenic_scores)}")
