n = int(input()) # Количество матчей
sl = {}
while n != 0:
    n -= 1
    x = input().split(';')
    # Если в словаре нет такой команды, добавляем ее название как ключ
    if x[0] not in sl:
        sl[x[0]] = [0, 0, 0, 0]
    if x[2] not in sl:
        sl[x[2]] = [0, 0, 0, 0]
    # Сравниваем кто победил в матче
    if int(x[3]) == int(x[1]): # Если ничья
        sl[x[0]][2] += 1 # очко за ничью первой команде
        sl[x[2]][2] += 1 # очко за ничью второй команде
    elif int(x[1]) > int(x[3]): # Если первая команда победила
        sl[x[0]][1] += 1 # присвоение очка за победу первой команде
        sl[x[2]][3] += 1 # присвоение очка за поражение второй команде
    elif int(x[3]) > int(x[1]):
        sl[x[2]][1] += 1 # присвоение очка за победу второй команде
        sl[x[0]][3] += 1 # присвоение очка за поражение первой команде

    sl[x[0]][0] += 1 # очко за участие в игре первой команде
    sl[x[2]][0] += 1 # очко за участие в игре второй команде

for i, j in sl.items():
    x = j[1] * 3 + j[2]
    print((i+':'), *j, x, end='\n')


# Хороший приер с курсов
#
# def points_counter(team, goals1, goals2):
#     if team not in teams:
#         teams[team] = [0] * 5
#     teams[team][0] += 1
#     teams[team][1] += int(goals1 > goals2)
#     teams[team][2] += int(goals1 == goals2)
#     teams[team][3] += int(goals1 < goals2)
#     teams[team][4] += int(goals1 > goals2) * 3 + int(goals1 == goals2)
#
#
# teams = dict()
#
# for _ in range(int(input())):
#     k = input().split(';')
#     points_counter(k[0], int(k[1]), int(k[3]))
#     points_counter(k[2], int(k[3]), int(k[1]))
#
# for el in teams:
#     print('{}:{} {} {} {} {}'.format(el, *teams[el]))