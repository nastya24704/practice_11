def calculate_monthly_averages(steps_per_day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthly_averages = []
    day_counter = 0

    for days in days_in_month:
        month_steps = steps_per_day[day_counter:day_counter + days]
        average = sum(month_steps) / days
        monthly_averages.append(round(average, 2))
        day_counter += days

    return monthly_averages


def main():
    try:
        with open('input.txt', 'r', encoding="utf-8") as f:
            steps = [int(line.strip()) for line in f if line.strip()]

        if len(steps) != 365:
            raise ValueError("Файл должен содержать данные ровно за 365 дней")

        averages = calculate_monthly_averages(steps)

        with open('output.txt', 'w', encoding="utf-8") as f_2:
            for i in averages:
                f_2.write(f"{i}\n")

    except ValueError as e:
        with open('output.txt', 'w', encoding="utf-8") as f_2:
            f_2.write(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    main()
