from utils.structures import Question


def data_from_file(path):
    data = []
    with open(path, encoding='utf-8') as f:
        l = f.readlines()
        i = 0
        while i < len(l):
            q = l[i].rstrip('\n')
            x = int(l[i + 1])
            a = list(zip([chr(ord('a') + i) for i in range(x)], map(lambda s: s.rstrip('\n'), l[i + 2:i + x + 2])))
            c = [c for c in l[i + x + 2] if c != '\n']
            i = i + x + 4
            data.append(Question(q, a, c))
    return data
