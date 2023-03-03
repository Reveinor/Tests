# принимаем значения пользователя
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# выбираем операцию
print("Выберите операцию")
print("1. Сложение")
print("2. Вычетание")
print("3. Умножение")
print("4. Деление")

# производим расчеты
choice = int(input("Enter choice(1/2/3/4): "))

if choice == 1:
    result = num1 + num2
    print(num1,"+",num2,"=", result)

elif choice == 2:
    result = num1 - num2
    print(num1,"-",num2,"=", result)

elif choice == 3:
    result = num1 * num2
    print(num1,"*",num2,"=", result)

elif choice == 4:
    result = num1 / num2
    print(num1,"/",num2,"=", result)
else:
    print("Invalid input")