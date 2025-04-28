try:
    with open('input.txt', 'r', encoding="utf-8") as f:
        data = f.readlines()

        if not data:
            with open('output.txt', 'w', encoding="utf-8") as f_2:
                f_2.write("ERROR")
            exit()

        try:
            N = int(data[0].strip())
        except ValueError:
            with open('output.txt', 'w', encoding="utf-8") as f_2:
                f_2.write("ERROR")
            exit()

        if len(data[1:]) == N:
            result = "YES"
        else:
            result = "NO"

        with open('output.txt', 'w', encoding="utf-8") as f_2:
            f_2.write(result)

except Exception as e:
    with open('output.txt', 'w', encoding="utf-8") as f_2:
        f_2.write("ERROR")
