def encode(msg,key):
    out = ""
    for i in range(len(msg)):
        out += chr(ord(msg[i])+key)
    return(out)
def decode(msg,key):
    out = ""
    for i in range(len(msg)):
        out += chr(ord(msg[i])-key)
    return(out)
