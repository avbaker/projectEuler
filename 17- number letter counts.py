digitValues = {
    "0": 0,
    "1": 3,
    "2": 3,
    "3": 5,
    "4": 4,
    "5": 4,
    "6": 3,
    "7": 5,
    "8": 5,
    "9": 4
}
digitSValues = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
teensValues = {
    "11": 6, # eleven
    "12": 6, # twelve
    "13": 8, # thirteen
    "14": 8, # fourteen
    "15": 7, # fifteen
    "16": 7, # sixteen
    "17": 9, # seventeen
    "18": 8, # eighteen
    "19": 8  # nineteen
}
teensSValues = {
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}
tensValues = {
    #append "and" onto these
    "1": 3, #ten
    "2": 6, #twenty
    "3": 6, #thirty
    "4": 5, #forty
    "5": 5, #fifty
    "6": 5, #sixty
    "7": 7, #seventy
    "8": 6, #eighty
    "9": 6  #ninety
}
tensSValues = {
    #append "and" onto these
    "0": "",
    "1": "ten",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

total = 0
''' #version 1
for i in range(1, 1001):
    j = str(i) # j is the string version of i
    thisScore = 0
    if len(j) == 1: #is a digit
        thisScore = digitValues[j]

        total = total + thisScore

    elif len(j) == 2: #is a ten
        if j[0] == "1" and j[1] != "0":
            thisScore = teensValues[j]
        else:
            thisScore = tensValues[j[0]] + digitValues[j[1]]

    elif len(str(i)) == 3: #is a hundred
        thisScore += digitValues[j[0]] + 10 # value + "hundredand
        if j[1] == "1" and j[2] != "0":
            thisScore += teensValues[j[1:]]
        else:
            thisScore += tensValues[j[0]] + digitValues[j[1]]


    else: #must be 1000
        thisScore = len("onethousand")

    print(f"{j} = {thisScore}")
    total+= thisScore
print(f"total count: {total}")
'''
for i in range(1, 1001):
    j = str(i) # j is the string version of i
    thisScore = 0
    if len(j) == 1: #is a digit
        thisScore = digitValues[j]
        print(f"{digitSValues[j]}")
        #total = total + len(f"{digitSValues[j]}")

    elif len(j) == 2: #is a ten
        if j[0] == "1" and j[1] != "0":
            thisScore = teensValues[j]
            print(teensSValues[j])
        else:
            thisScore = len(tensSValues[j[0]]) + len(digitSValues[j[1]])
            print(f"{tensSValues[j[0]]}{digitSValues[j[1]]}")

    elif len(str(i)) == 3: #is a hundred
        if j[1] == "0" and j[2] == "0":
            thisScore = len(digitSValues[j[0]]) + 7
            print(f"{digitSValues[j[0]]}hundred")
        else:
            thisScore += len(digitSValues[j[0]]) + 10 # value + "hundredand
            print(f"{digitSValues[j[0]]}hundredand", end="")
            if j[1] == "1" and j[2] != "0":
                thisScore += len(teensSValues[j[1:]])
                print(teensSValues[j[1:]])
            else:
                thisScore += len(tensSValues[j[1]]) + len(digitSValues[j[2]])
                print(f"{tensSValues[j[1]]}{digitSValues[j[2]]}")


    else: #must be 1000
        thisScore = len("onethousand")

    print(f"{j} = {thisScore}")
    total+= thisScore
print(f"total count: {total}")