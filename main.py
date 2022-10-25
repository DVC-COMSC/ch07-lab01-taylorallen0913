numbers = list(map(int, input().split()))

sum = 0
min_num = numbers[0]
max_num = numbers[0]

for number in numbers:
    sum += number
    if number <= min_num:
        min_num = number
    else:
        max_num = number

print(sum - min_num - max_num)
