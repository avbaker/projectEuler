'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
, is the
th name in the list. So, COLIN would obtain a score of
.

What is the total of all the name scores in the file?'''
def getscore(word, multiplier, show): #returns the score of the word
    score = 0
    wordScore = 0
    for letter in word: #for each letter, calculate score.
        asciiChar = ord(letter)
        letterScore = asciiChar - 64
        wordScore += letterScore
    score = wordScore * multiplier #multiply score by position in array+1 (so the first is not negated by *0)
    if show:
        print(f"{name+1}. {names[name]}: {letterScore}x{multiplier}={score}") # show debug data
    return score

f = open("0022_names.txt", "r") #1. import names
names = f.read().split(",")
f.close()
names.sort() # remember to sort!
print(f"number of names: {len(names)}") # number of names
total = 0
for name in range(len(names)): # for each name, strip parentheses, and add score of the word * position
    thisname = names[name][1:-1]

    total += getscore(thisname,name+1,False)

print(f"total score: {total}") #output total score