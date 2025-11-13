def encrypt_caesar(txt, offset):
    encrypt = ""
    for i in txt:
        if not i.isspace():
            if ord(i) + offset <= 122:
                encrypt += chr(ord(i) + offset)
            else:
                encrypt += chr(ord(i) + offset - 26)
        if i.isspace():
            encrypt += i

    return encrypt


def decrypt_caesar(txt, offset):
    decrypt = ""
    for i in txt:
        if not i.isspace():
            if ord(i) - offset >= 97:
                decrypt += chr(ord(i) - offset)
            else:
                decrypt += chr(ord(i) - offset + 26)
        if i.isspace():
            decrypt += i
    return decrypt
