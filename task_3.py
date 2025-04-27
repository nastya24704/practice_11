with open("input.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
new_line = ''.join([line[0] for line in data if line.strip()])
with open("output.txt", "w", encoding="utf-8") as f_2:
    f_2.write(new_line)
