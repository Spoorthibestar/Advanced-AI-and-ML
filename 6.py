import random

def fitness(x):
    return x**2

population = [random.randint(0, 31) for _ in range(6)]
generations = 5

for gen in range(generations):
    scores = [fitness(x) for x in population]

    parents = sorted(zip(population, scores), key=lambda x: x[1], reverse=True)[:2]
    p1, p2 = parents[0][0], parents[1][0]

    point = random.randint(1, 4)

    c1 = (p1 & ((1 << point) - 1)) | (p2 & ~((1 << point) - 1))
    c2 = (p2 & ((1 << point) - 1)) | (p1 & ~((1 << point) - 1))

    def mutate(x):
        bit = 1 << random.randint(0, 4)
        return x ^ bit if random.random() < 0.3 else x

    c1, c2 = mutate(c1), mutate(c2)

    population = [p1, p2, c1, c2] + [random.randint(0, 31) for _ in range(2)]

    print(f"Generation {gen+1}: {population} |
