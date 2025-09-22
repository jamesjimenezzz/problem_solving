#1.)PYRAMID *
pyramid_schema = 3

def pyramid():
    pyramid_rows = 5
    for i in range(1, pyramid_rows + 1):
        print(" " * (pyramid_rows - i), end ="")
        print("*" * (2 * i  - 1))

for i in range(1, pyramid_schema + 1):
    pyramid()



line_rows = 3
for i in range(1, line_rows + 1):
    print(" ", end ="  ")
    print("|" * line_rows)


print()

#2.)MULTIPLICATION TABLE

for i in range (1,11):
    for j in range(1,11):
        product = i * j

        print(f"{product: 4}", end="")
    print()



print()

#3.)PYRAMID PALINDROME NUMBERS
n = 5
#TOP HALF TO UMAY NAKAKALITO
for i in range(1, 5 +1):
    print(" " * (n-i), end ="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i- 1, 0, -1):
        print(j, end="")
    
    print()

#BOTTOM HALF TO GRABE NA TO
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")

    for j in range(1, i + 1):
        print(j, end ="")
    
    for j in range(i-1, 0, -1):
        print(j, end="")
    
    print()



#How do nested loops make these patterns possible compared to single loops?
#Nested loops make these possible by running multiple loop in indexes run. By that, it is possible to make columns and rows, by customizing index loops  on every nested loops.