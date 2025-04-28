try:
    with open('input.txt', 'r', encoding="utf-8") as f:
        numbers = f.read().split()

        if len(numbers) != 3:
            raise ValueError("Файл input.txt должен содержать ровно три числа")

        try:
            a = int(numbers[0])
            b = int(numbers[1])
            c = int(numbers[2])
        except ValueError:
            raise ValueError("Все значения в файле должны быть целыми числами")

        try:
            result = a / b + c
        except ZeroDivisionError:
            raise ZeroDivisionError("division by 0")

        with open('output.txt', 'w', encoding="utf-8") as f_2:
            f_2.write(str(result))

except ValueError as e:
    with open('output.txt', 'w', encoding="utf-8") as f_2:
        f_2.write(f"data error: {str(e)}")
except ZeroDivisionError as e:
    with open('output.txt', 'w', encoding="utf-8") as f_2:
        f_2.write(f"data error: {str(e)}")
