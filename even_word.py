def even_word(string):
    chars = {}
    makeEven = 0
    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
            
    for char in chars:
        if chars[char] % 2 != 0:
            makeEven += chars[char] % 2 
    return makeEven
    
print(even_word('potato'))
print(even_word('aaabbbccc'))
print(even_word('aaaa'))
print(even_word('aabbbb'))