file = open('input.txt', 'r')
a = ''
for line in file:
    if int(line) != 100:
        a += line
file.close()

file = open('input.txt', 'w')
file.write(a)
file.close()
