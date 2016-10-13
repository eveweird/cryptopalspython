from binascii import unhexlify, b2a_base64
answer = raw_input("input: ")
result = b2a_base64(unhexlify(answer))
print(result)
