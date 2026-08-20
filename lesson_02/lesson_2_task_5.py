def month_to_season(month: int) -> str:
    """Возвращает название сезона по номеру месяца (1–12)."""
    if not 1 <= month <= 12:
        raise ValueError("Номер месяца должен быть от 1 до 12.")

    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    else:  # 9, 10, 11
        return "Осень"


if __name__ == "__main__":
    while True:
        user_input = input(
            "\nВведите номер месяца (1–12) или 'stop' для выхода: "
        ).strip()

        if user_input.lower() == "stop":
            print("Выход из программы.")
            break

        try:
            month = int(user_input)
            season = month_to_season(month)
            print(f"Месяц {month} относится к сезону: {season}")
        except ValueError as e:
            if "должен быть от 1 до 12" in str(e):
                print(f"Ошибка: {e}")
            else:
                print("Ошибка: введите целое число")
