#"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#""  -->  ""


#NEW: SORTED, .ISDIGIT

x=0

sentence = "is2 Thi1s T4est 3"


splitted = sentence.split(" ")



def extract_number(splitted):

    for word in splitted:
        for ch in word:
            if ch.isdigit():
                return int(ch)
        
    return 0
    

sorted_sentence = sorted(splitted, key=extract_number)

print(sorted_sentence)