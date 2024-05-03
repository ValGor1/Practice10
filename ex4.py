file = open('input.txt', 'r')
a = ''
for line in file:
    if len(line) < 20:
        a += line
file.close()

file2 = open('output.txt', 'w')
file2.write(a)
file2.close()
