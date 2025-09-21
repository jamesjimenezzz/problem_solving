#"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#""  -->  ""


#NEW: SORTED, .ISDIGIT



sentence = "is2 Thi1s T4est 3a"

words = sentence.split()

def extract_number(words: str) -> int:
    for ch in words:

        if ch.isdigit():
            return int(ch)
    
    return 0 


words_sorted = sorted(words, key=extract_number) # kaya niyang isort yung isang array, kahit full of strings, basta may key na integer.

print(words_sorted)