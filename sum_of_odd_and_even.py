numbers = int(input("Enter numbers: "))

odd_sum = 0
even_sum = 0
odd_list = []
even_list = []
even_result = ""

stringed_numbers = str(numbers)
list_numbers = list(stringed_numbers)

for num in list_numbers:
    x = int(num)

    if x % 2 == 0:
        even_sum += x
        even_list.append(x)
    else:
        odd_sum +=x
        odd_list.append(x)


odd_result = "+".join(str(odd) for odd in odd_list)
even_result = "+".join(str(even) for even in even_list)


print(f"Odd Sum = {odd_sum}, {odd_result}" )
print(f"Even Sum = {even_sum}, {even_result}")
