with open("input.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
new_line = [line for line in data if len(data) >20]
with open("output.txt", "w", encoding="utf-8") as f_2:
    f_2.writelines(new_line)
