with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read()

new_f = data.upper()

with open("output.txt", "w", encoding="utf-8") as f_2:
    f_2.write(new_f)
