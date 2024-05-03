file = open("input.txt",'r')
a = ''
for line in file:
    if line[0] == 'A' or line[0] == 'a':
        a += line
file.close()

file2 = open('output.txt', 'w')
file2.write(a)
file2.close()
