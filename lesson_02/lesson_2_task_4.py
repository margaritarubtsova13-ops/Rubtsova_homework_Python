def fizz_buzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 15 == 0: 
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    while True:
        user_input = input("Введите положительное целое число n (или 'stop' для выхода): ").strip()
        
        if user_input.lower() == "stop":
            print("Выход из программы.")
            break
        
        try:
            n = int(user_input)
            if n <= 0:
                print("Число должно быть больше нуля. Попробуйте ещё раз.\n")
                continue
            fizz_buzz(n)
            print()  # пустая строка для читаемости
        except ValueError:
            print("Ошибка: нужно ввести целое число. Попробуйте ещё раз.\n")