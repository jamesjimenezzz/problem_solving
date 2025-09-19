#SOLVED
#COLLATZ SEQUENCE LENGTH


number = int(input("Enter a number: "))

total_counts = 0

while number != 1:
    if number % 2 == 0:
        number /= 2
        total_counts += 1
    else:
        number = (number * 3) + 1
        total_counts += 1

print(total_counts)
    
