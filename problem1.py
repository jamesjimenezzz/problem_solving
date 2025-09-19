#DONE

number = int(input("Enter a number: "))

total = 0
lists = []

for i in range(1, number + 1):
    if i % 3 == 0 or i % 5 == 0:
        lists.append(i)
        total += i
    
print(lists)    
print(total)