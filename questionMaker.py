import requests

def syns(word):
    wordSet = set()
    wordSet.add(word)

    URL1= "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    apiKey = "dict.1.1.20220325T172343Z.dd93028b12a85c82.e00b4181e9da913653d883e7dd098e923d2f5ff5"
    URL2 = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key="+apiKey+"&lang=en-en&text="+word

    try:
        r = requests.get(url = URL1)
        data = r.json()

        syms = data[0]['meanings'][0]['synonyms']
        for i in syms:
            wordSet.add(i)
    except:
        pass
    try:
        r = requests.get(url = URL2)
        data = r.json()
        synlist = data['def'][0]['tr'][0]['syn']

        for i in synlist:
            word = i['text']
            if " " in word:
                continue
            wordSet.add(word)
    except:
        pass
    print(wordSet)
    return wordSet

#print(syns("computer science"))

def getListOfWordSets(question):
    words = question.split(" ")
    wordIndexes =[]
    listOfWordSets = []
    for i in range(len(words)):
        word = words[i].lower()
        # you, me, I, we, us, this, them, that
        if word in ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]:
            continue
        wordIndexes.append(i)
        listOfWordSets.append(syns(word))
    return [listOfWordSets,wordIndexes]

def makeCombinations(inputQuestionArray,toPutArray,index):
    returnArray = []
    for i in toPutArray:
        inc = inputQuestionArray.copy()
        inc[index] = i
        returnArray.append(inc)
    return returnArray


question = "How can I make online payment in the AICTE website"

listofsets = getListOfWordSets(question)
print(listofsets)
input("press enter to generate strings\n\n")
gg = makeCombinations(question.split(" "),listofsets[0][0],listofsets[1][0])



Tall = gg.copy()
for x in range(0,len(listofsets[0])):
    p = Tall.copy()
    for i in p:
        gg = makeCombinations(i,listofsets[0][x],listofsets[1][x])
        for i in gg:
            Tall.append(i)

atlast = set()
for i in Tall:
    q = " ".join(i)
    atlast.add(q)
    print(q)


