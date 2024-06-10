from functools import cmp_to_key


def right_order(left, right):
    for i in range(min(len(left), len(right))):
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] == right[i]:
                continue
            return left[i] - right[i]
        ret = right_order(
            left[i] if type(left[i]) == list else [left[i]],
            right[i] if type(right[i]) == list else [right[i]]
        )
        if ret:
            return ret
    return len(left) - len(right)


with open("text.txt") as file:
    packets = [eval(line) for line in file.read().splitlines() if line]
    indices1 = sum(i // 2 + 1 for i in range(0, len(packets), 2) if right_order(*packets[i:i + 2]) < 0)
    packets += [[[2]], [[6]]]
    packets = sorted(packets, key=cmp_to_key(right_order))
    indices2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    print(indices1)
    print(indices2)
