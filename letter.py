def same_letter(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
        
    print('The list of words with same first and last characters ',lst )
    return ctr
count = same_letter(['abc', 'cfc', 'bab', 'fgc'])
print('The number of times the first and last letter are same is ', count)