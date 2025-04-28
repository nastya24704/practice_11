def parse_date(date_str):
    day, month = map(int, date_str.split('.'))
    return day, month


def days_between_dates(current_day, current_month, day, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if current_month == month:
        return current_day - day
    else:
        total_days = days_in_month[month - 1] - day
        for m in range(month + 1, current_month):
            total_days += days_in_month[m - 1]
        total_days += current_day
        return total_days


def main():
    with open('input.txt', 'r', encoding="utf-8") as f:
        data = f.readlines()

    current_date = data[0].strip()
    current_day, current_month = parse_date(current_date)

    N = int(data[1].strip())

    result = []

    for line in data[2:2 + N]:
        parts = line.strip().split()
        cell_number = parts[0]
        date = parts[1]
        day, month = parse_date(date)

        days = days_between_dates(current_day, current_month, day, month)
        if days > 3:
            result.append(cell_number)

    with open('output.txt', 'w', encoding="utf-8") as f_2:
        for cell in result:
            f_2.write(cell + '\n')

if __name__ == "__main__":
    main()
