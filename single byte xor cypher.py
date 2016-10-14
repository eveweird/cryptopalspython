results = {}
file = open("inp.txt", "r")


def xored(inp, word):
    inp2= []
    hexinp2 = []
    for i in range(0, len(inp), 2):
        inp2.append(inp[i:i+2])
    for i in range(97,123):
        store = ""
        for j in range(len(inp2)):
            res = int(inp2[j], 16) ^ i
            store = store + chr(res)
        if not store.lower().find(word) == -1:
            results[chr(i)] = store.lower()



for line in file:
    xored(line.rstrip(), "of")
for k, v in results.items():
    print(k + ": " + v)
results = {}
print(" ")
xored(line.rstrip(), "the")
for k, v in results.items():
    print(k + ": " + v)
results = {}
print(" ")
xored(line.rstrip(), "and")
for k, v in results.items():
    print(k + ": " + v)
results = {}
print(" ")
xored(line.rstrip(), "be")
for k, v in results.items():
    print(k + ": " + v)
results = {}
print(" ")
xored(line.rstrip(), "in")
for k, v in results.items():
    print(k + ": " + v)











