rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows -i ), end="")
    for j in range(1, i * 2):
        print("*", end="")
    
    print()



