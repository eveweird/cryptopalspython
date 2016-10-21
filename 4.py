import collections
import re
results = {}
close = 10000000000000000000
regex = re.compile('[^a-zA-Z]')
lttrFreq = {"A" : 8.55, "K" : 0.81, "U" : 2.68, "B" : 1.60, "L" : 4.21, "V" :  1.06, "C" :  3.16, "M" :  2.53, "W" :  1.83, "D" :  3.87, "N" :  7.17, "X" :  0.19, "E" : 12.10, "O" :  7.47, "Y" :  1.72, "F" :  2.18, "P" :  2.07, "Z" :  0.11, "G" :  2.09, "Q" :  0.10, "H" :  4.96, "R" :  6.33, "I" :  7.33, "S" :  6.73, "J" :  0.22, "T" :  8.94}
file = open("inp.txt", "r")
    

def xored(inp, close):
    
    inp2= []
    hexinp2 = []
    
    #seperate hex into bytes
    for i in range(0, len(inp), 2):
        inp2.append(inp[i:i+2])

    #cycle through letters
    for i in range(97,123):
        store = ""
        
        #xor text byte by byte using the current letter i
        for j in range(len(inp2)):
            res = int(inp2[j], 16) ^ i
            store = store + chr(res)
            #store = regex.sub('', store.upper())
            
            
        #find letter frequency of decrypted string and store in letters
        letters = collections.Counter(store)
        score = 0
        
        #attempt to score the letter freq against actual english freq
        for let in lttrFreq:
            if not (100 *(letters[let]/len(store))) == 0:
                score = score + (abs(lttrFreq[let] - (100 *(letters[let]/len(store)))))
            

        #if the score is lower than the current lowest, make the score the current lowest 
        if score < close:
            results.clear()
            results[chr(i)] = store.lower()
            close = score
    return close


i = 0
for line in file:
    i = i + 1
    close = xored(line.rstrip(), close)
    #print(str(close) + " " + str(i))
print(results)
