import random

def fitness(K, T):
    return -abs(K[0] + K[1] - T)

def mutate(K):
    random_index = random.randint(0, len(K) - 1)
    K[random_index ] = random.randint(0, 9)

def evolve(T, k):
    K = [random.randint(0, 9) for _ in range(k)]

    while fitness(K, T) != 0:
        new_K = K[:]
        mutate(new_K)

        if fitness(new_K, T) >= fitness(K, T):
            K = new_K

    return K

# Test Cases
print("Case1 Output:", *evolve(7, 3))   # e.g. 4 3 0
print("Case2 Output:", *evolve(10, 3))  # e.g. 8 2 0
