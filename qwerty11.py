x = int(input())
if 1900 <= x <= 3000:
    if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
        print('Високосный')
    else:
        print('Обычный')