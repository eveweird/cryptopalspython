inp = raw_input("enter string: ")
blen = int(raw_input("enter block lenght: "))
slen = len(inp)
while slen > blen:
    slen = slen - blen
for i in range(blen - slen):
    inp = inp + "\x04"
print(inp)
