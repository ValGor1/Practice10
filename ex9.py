file = open('input.txt','r')
a = ''
n = 1
for line in file:
    if n % 2 == 0:
        a += line
        n += 1
file.close()

file2 = open('output.txt', 'w')
file2.write(a)
file2.close()
