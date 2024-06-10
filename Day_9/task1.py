from math import dist

def update_heads(last_heads, step):
    d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    heads_x = last_heads[0]
    heads_y = last_heads[1]
    heads_x += d[step[0]][0]
    heads_y += d[step[0]][1]
    return ((heads_x, heads_y))

def update_tails(last_heads, last_tails):
    Hx = last_heads[0]
    Hy = last_heads[1]
    Tx = last_tails[0]
    Ty = last_tails[1]
    if abs(Ty - Hy) > 1 and Tx == Hx:
        Ty += [-1, 1][Ty < Hy]
    elif abs(Tx - Hx) > 1 and Ty == Hy:
        Tx += [-1, 1][Tx < Hx]
    elif dist((Hx,Hy),(Tx,Ty)) > 2:
        Tx += [-1, 1][Tx < Hx]
        Ty += [-1, 1][Ty < Hy]
    A = (Tx, Ty)
    return A



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    with open('text.txt') as file:
        lines = file.readlines()
    lines = [[x,int(y)] for [x,y] in [_.rstrip().split(" ") for _ in lines]]
    last_heads = [0, 0]
    last_tails = (0,0)
    visited = [last_tails]
    for item in lines:
        for i in range(item[1]):
            last_heads = update_heads(last_heads, item)
            last_tails = update_tails(last_heads, last_tails)
            visited.append(last_tails)
    print(len(set(visited)))