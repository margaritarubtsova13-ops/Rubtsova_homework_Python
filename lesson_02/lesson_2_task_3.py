def square_with_input():
    user_input = input("Введите длину стороны квадрата: ")

    try:
        side = float(user_input)
    except ValueError:
        print("Ошибка: сторона квадрата должна быть числом.")
        return

    if isinstance(side, bool) or side <= 0:
        if side == 0:
            print("Ошибка: сторона квадрата должна быть больше нуля.")
        elif side < 0:
            print("Ошибка: сторона квадрата не может быть отрицательной.")
        else:
            print("Ошибка: некорректное значение стороны.")
    else:
        area = side * side
        print(f"Площадь квадрата: {area}")


square_with_input()
