class falsePadding(Exception):
    def __init__(self, arg):
        self.args = arg

inp = raw_input("enter string: ")
while not inp.find("\\x") == -1:
    print(inp[inp.find("\\x")+2: inp.find("\\x")+4])
    if inp[inp.find("\\x")+2: inp.find("\\x")+4] == "04":
        print(inp[:inp.find("\\x")] + inp[inp.find("\\x")+4:])
        inp = inp[:inp.find("\\x")] + inp[inp.find("\\x")+4:]
    else:
        raise falsePadding("false padding")
print(inp)
