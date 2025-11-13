def encript_caesar(txt,offset):
    encript = ""
    for i in txt:
        if not i.isspace():
            if ord(i) + offset <= 122 :
                encript += chr(ord(i) + offset)
            else:
                encript += chr(ord(i)+offset - 26)
        if i.isspace():
            encript+= i
    return encript

def decript_caesar(txt, offset):
    encript = ""
    for i in txt:
        if not i.isspace():
            if ord(i) - offset >= 97:
                encript += chr(ord(i) - offset)
            else:
                encript += chr(ord(i) - offset + 26)
        if i.isspace():
            encript += i
    return encript

