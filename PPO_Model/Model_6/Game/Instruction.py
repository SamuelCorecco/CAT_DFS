import itertools

TOT_istructions2 = [
[2, 0, 1, -1, 0, 0, -1]
]

TOT_istructions = [
[0, 0, 1],
[0, 1, 0],
[0, -1, 1],
[0, -1, -1],
[2, 0, 1, -1, 0, 0, -1],
[2, -1, 0, -1, 0, 0, -1, 0, -1],
[2, -1, 0, -1, 0, 0, 1, 0, 1],
[2, 0, -1, 0, -1, -1, 0, -1, 0],
[2, 0, 1, 0, 1, -1, 0, -1, 0],
[0, -1, 1, 1, 1],
[0, 1, 1, -1, 1],
[1, 1, 1, 1, -1],
[1, 1, -1, 1, 1]
]

def generate_combinations(n):
    result = []
    for combination in itertools.product(range(1, n+1), repeat=4):
        result.append(list(combination))
    return result