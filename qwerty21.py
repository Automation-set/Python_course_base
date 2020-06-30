x = 0
while x <= 100:
    x = int(input())
    if x < 10:
        continue
    if x > 100:
        break
    print(x)

# Тут показано как запустить While насильно :)
# while True:
#     a = int(input())
#     if (a < 10):
#         continue
#     if (a > 100):
#         break
#     print(a)