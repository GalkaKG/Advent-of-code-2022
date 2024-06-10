import math

lines = [x.split() for x in open("text.txt")]
d = 0


def init_mon():
    global d
    items = [''.join(x[2:]).split(',') for x in lines[1::7]]
    op = [''.join(x[1:]) for x in lines[2::7]]
    div = [int(x[-1:][0]) for x in lines[3::7]]
    t = [int(x[-1:][0]) for x in lines[4::7]]
    f = [int(x[-1:][0]) for x in lines[5::7]]
    mon = [[items[i], op[i], div[i], t[i], f[i], 0] for i in range(len(f))]
    d = math.lcm(*div)
    return mon


print(f'd: {d}')


def part(mo, rounds, worry):
    old, new = 0, 0
    for _ in range(rounds):
        for m in mo:
            while m[0]:
                m[5] += 1
                old = int(m[0].pop(0))
                loc = {'old': old, 'new': new}
                exec(m[1], globals(), loc)
                new = loc['new']
                if worry:
                    new //= 3
                elif new > d:
                    new = d + (new % d)
                if new % m[2] == 0:
                    mo[m[3]][0].append(str(new))
                else:
                    mo[m[4]][0].append(str(new))
    smon = sorted(mo, key=lambda x: x[5])
    print(f'monbiz: {smon[-1][5] * smon[-2][5]}')


part(init_mon(), 20, True)
part(init_mon(), 10000, False)
