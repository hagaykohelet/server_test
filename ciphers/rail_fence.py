def fence_encrypt(txt):
    word = ""
    odd = ""
    even = ""
    encrypt = ""
    for i in txt:
        if not i.isspace():
            word += i

    for char in range(len(word)):
        if char % 2 ==0:
            even += word[char]
        else:
            odd += word[char]
    encrypt = even + odd
    return encrypt

def fence_decrypt(txt):
    even = txt[:len(txt)//2+1]
    odd = txt[len(txt)//2+1:]
    print(odd)
    print(even)
    even_idx = 0
    odd_idx = 0
    decrypt = ""
    for _ in range(len(even+odd)):
        if even_idx <len(even) and odd_idx < len(odd):
            decrypt += even[even_idx] + odd[odd_idx]
            even_idx += 1
            odd_idx += 1
        elif even_idx < len(even) and odd_idx == (len(odd)):
            decrypt += even[even_idx]
            even_idx += 1
        elif even_idx == len(even) and odd_idx < (len(odd)):
            decrypt += odd[odd_idx]
            odd_idx += 1

    return decrypt








