n = 5
#TOP HALF
for i in range(1, 5 +1):
    print(" " * (n-i), end ="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i- 1, 0, -1):
        print(j, end="")
    
    print()

#BOTTOM HALF
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")

    for j in range(1, i + 1):
        print(j, end ="")
    
    for j in range(i-1, 0, -1):
        print(j, end="")
    
    print()


