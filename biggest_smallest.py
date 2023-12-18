print("exercise to check the smallest and the largest number in list \n")

numbers = [20,30,40,50,60,76,44,222,245,1566,15,23]

smallest = numbers[0]
biggest = numbers[0]
for number in numbers:
    if number > biggest:
        biggest = number
    elif number < smallest:
        smallest = number

print(f"the smallest number is: {smallest}")
print(f"the biggest number is: {biggest}")
