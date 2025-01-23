import random

toistot = 0
N = int(input("Anna N: "))
n = 0
while toistot <= N:
    X = random.uniform(-1, 1)
    Y = random.uniform(-1, 1)
    if X ** 2 + Y ** 2 < 1:
        n = n + 1
    toistot = toistot + 1
tulos = 4 * n / N
print(f"{tulos:.4f}")
