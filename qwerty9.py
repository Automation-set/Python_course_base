# if x % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

a = int(input())
b = int(input())
if b != 0:
    print(a / b)
else:
    print('Деление невозможно')
    b = int(input('Введите не нулевое значение '))
    if b == 0:
        print("Вы не справились!")
    else:
        print(a / b)
