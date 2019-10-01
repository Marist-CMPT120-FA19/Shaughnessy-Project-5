def main():
    
    s = str(input("Please write a sentence: "))

    WordTotal = len(s.split(" "))

    average = 0
    
    for x in s:
        average = average + len(x)
        
    average = (average - s.count(" "))/ WordTotal
    
    print("Number of characters: ", len(s))
    print("Number of words: ",  WordTotal)
    print("Average word length: ", average)

main()
