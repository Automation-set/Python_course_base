text = open('dataset_3363_3.txt', 'r')
s = text.read().replace('\n', '').lower().split()
s = sorted(s)

x = 0
sl = ''
for i in s:
    if s.count(i) > x:
        x = s.count(i)
        sl = i
out2 = sl + ' ' + str(x)
text.close()

with open('dataset_3363_3.txt', 'w') as out:
    out.write(out2)