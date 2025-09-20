#SOLVED
#Digit Sum
numbers = int(input("Enter numbers: "))


string_numbers = str(numbers)


listed_numbers = list(string_numbers)

final_result = 0
for num in listed_numbers:
    final_result += int(num)


print(final_result)

