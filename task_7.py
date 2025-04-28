with open('input.txt', 'r') as f:
    data = f.readlines()

new_lines = [line for line in data if line.strip() != '100']

with open('input.txt', 'w') as f:
    f.writelines(new_lines)
