#PALINDROME
#DONE


word = input("Enter a word: ")

if word == word[::-1]:
    print("YES")
else:
    print("NO")