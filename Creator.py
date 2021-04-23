import json
import math
import random
import sys

#load words
with open("words_dictionary.json") as f:
    wrd = json.load(f)
words = list(wrd.keys())
#print(len(words))

#pick starting word
strtIndex = random.randrange(0, len(words))
start = words[strtIndex]
#print(start, strtIndex)

usedWords = start
lbuilt = ""
built = start
addedWords = 0
making = True

#set this to None to remove limit
wordLimit = 50

#exit function
def bungalow():
    print(f"Finished. Used {addedWords} of {len(words)} words. Result is {len(built)} letters long.")
    with open("result.txt", "w") as rslt:
        rslt.write(built)
    input("Press enter to display.")
    print(built)
    sys.exit(0)


# for sig in (SIGABRT, SIGBREAK, SIGILL, SIGINT, SIGSEGV, SIGTERM):
#    signal(sig, bungalow)
try:
    while making:
        for ind, i in enumerate(words):
            if i in usedWords:
                continue
            elif i[0] == built[len(built) - 1]:
                #Update lists and add word
                usedWords += i
                lbuilt = built
                built += i[1:]
                addedWords += 1
                del words[ind]
                random.shuffle(words)
                break
        if not lbuilt == built:
            #print occasional status updates if portmanteu has been expanded
            if addedWords % 10 == 0:
                print(f"Used {addedWords} of {len(words)} words ({math.floor(addedWords / len(words) * 100)}%).")
                # print(usedWords)
            if addedWords % 100 == 0:
                print(f"Portmanteu is {len(built)} letters long.")
        if wordLimit:
            if addedWords >= wordLimit:
                bungalow()
    bungalow()
except:
    bungalow()
