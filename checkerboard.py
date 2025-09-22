
for i in range(1, 3+1):
    for j in range(1, 7+1):
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(".", end ="")
    
    print()