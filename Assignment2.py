# Task 1

number = int(input('Enter a number :'))

if number%2 ==0:
    print(number, "Number is even")
else: print(number, "Number is odd")

# Task 2

total_sum = 0
for number in range(1,51):
    total_sum = total_sum + number
print("total sum of 1 to 50 is ", total_sum)
