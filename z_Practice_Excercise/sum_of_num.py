total = 0

for i in range(1, 10):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        print(f"{i} {total}")