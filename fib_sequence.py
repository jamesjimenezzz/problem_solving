#DONE


fib_num = int(input("Enter a number: "))

#fibonacci = sum of latest number and the number before the latest number



fib_start = [0, 1]
final_result = ""

if fib_num == 0:
    print(fib_start[0])
elif fib_num == 1:
    print(fib_start)
else:
    for i in range(2, fib_num):
        result = fib_start[-1] + fib_start[-2]
        fib_start.append(result)

    for num in fib_start:
        final_result += str(num) + " "
    
    print(final_result)


