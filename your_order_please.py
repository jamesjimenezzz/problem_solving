def order(sentence):
    
    splitted = sentence.split(" ")
  
    def extract_number(splitted):

        for word in splitted:
            for ch in word:

                if ch.isdigit():
                    return int(ch)
        return 0
    

   
    sorted_sentence = sorted(splitted, key=extract_number)

    print(sorted_sentence)
    


order("is2 Thi1s T4est 3a")