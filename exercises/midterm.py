command = "path"
while command != "quit":
    if command == "path":
        filePath = input("Enter a file path:")
        myFile = open(filePath)
        lines = myFile.readlines()
        myFile.close()
        lines = " ".join(lines)
        words = lines.split()
        for i in range(len(words)):
            newWord = ""
            for c in words[i]:
                if c.isalpha():
                    newWord += c.lower()
            words[i] = newWord
    while True:
        letters = input("Enter a list of letters:")
        letters = letters.lower()
        letterList = []
        for chr in letters:
            if chr.isalpha():
                letterList.append(chr)
        if len(letterList) == 0:
            print("Invalid input.")
        else : break
    letterList = list(set(letterList))
    letterList.sort()

    for letter in letterList:
        wordList = []
        lengthList = []
        for word in words:
            if letter in word:
                wordList.append(word)
                lengthList.append(len(word))
        if len(wordList) == 0 :
            result = "Letter not found!"
        else:
            result = wordList[lengthList.index(max(lengthList))]
        print(letter,":",result)

    while True:
        command = input("Enter *path* for a new path, *list* for a new list of letters and *quit* to quit:")
        if command in ["path","list","quit"]:
            break
print("Goodbye!")