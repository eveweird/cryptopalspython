#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
results = {}
inp = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
inp2= []
hexinp2 = []
for i in range(0, len(inp), 2):
    inp2.append(inp[i:i+2])
for i in range(97,123):
    store = ""
    for j in range(len(inp2)):
        res = int(inp2[j], 16) ^ i
        store = store + chr(res)
    if not store.lower().find("of") == -1:
        results[chr(i)] = store.lower()
print(results)

    
    





    #res = hex(int("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", 16) ^ i)
    #print(res)
    #if not res.find("the") == -1:
        #results[alpha[i]] = res
#print(results)



