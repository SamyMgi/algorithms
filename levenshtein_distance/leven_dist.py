""" Levenshtein's distance implementation and application"""

def DistLev(word1, word2) :
    d = [ [0]*(len(word2)+1) for i in range(len(word1)+1)]
    for i in range(len(word1)+1) :
        for j in range(len(word2)+1) :
            if i == 0 and j == 0 :
                d[i][j] = 0
            elif i == 0 :
                d[i][j] = j
            elif j == 0 :
                d[i][j] = i
    for i in range(0,len(word1)) :
        for j in range(0,len(word2)) :
            if word1[i]==word2[j] :
                cost = 0
            else :
                cost = 1
            d[i+1][j+1] = min(d[i][j+1] + 1, d[i+1][j] + 1, d[i][j] + cost)
    return d[-1][-1]


#Using a country list
with open("country.txt") as txt_file :
        dictionary = txt_file.readlines()

for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].replace("\n","")


#User input word
inputWord = input("Word :")

#Initializing minimum Levenshtein Distance and list of Words
minDist = DistLev(inputWord, dictionary[0])
bestWord = [dictionary[0]]

for word in dictionary :
    if DistLev(inputWord, word) <= minDist :
        if DistLev(inputWord, word) < minDist :
            bestWord = [word]
            minDist = DistLev(inputWord, word)
        else :
            bestWord.append(word)
            
print("Approximating", inputWord, "by :")
for word in bestWord :
    print(word)
