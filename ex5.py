file = open('input.txt', 'r')
nums = []
for line in file:
    nums.append(line)
file.close()
file = open('output.txt', 'w')
try:
    result = int(nums[0])/int(nums[1]) + int(nums[2])
    file.write(str(result))

except ZeroDivisionError:
    file.write('division by 0')
except ValueError:
    file.write('data error')