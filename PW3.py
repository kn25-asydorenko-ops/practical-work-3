def count_valid_numbers(p):
    if p <= 0:
        return 0
    if p == 1:
        return 2
    if p == 2:
        return 4
    
    # Початкові значення для p = 1 та p = 2
    prev2 = 2
    prev1 = 4
    
    # Обчислюємо значення для наступних розрядів
    for _ in range(3, p + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return prev1

# Зчитування вхідних даних
try:
    p = int(input("Введіть кількість розрядів p (p <= 30): "))
    if 1 <= p <= 30:
        result = count_valid_numbers(p)
        print(f"Кількість чисел із {p} розрядів: {result}")
    else:
        print("Будь ласка, введіть число в діапазоні від 1 до 30.")
except ValueError:
    print("Некоректне введення. Очікується ціле число.")