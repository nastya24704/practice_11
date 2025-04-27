with open("input.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
new_lines = [line for line in data if line.strip().startswith(('А', 'а'))]
with open("output.txt", "w", encoding="utf-8") as f_2:
    f_2.writelines(new_lines)
