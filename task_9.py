with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()

with open('simple/output.txt', 'w', encoding="utf-8") as f_2:
    for i in range(1, len(data) + 1):
        if i % 2 == 0:
            f_2.write(data[i - 1])
