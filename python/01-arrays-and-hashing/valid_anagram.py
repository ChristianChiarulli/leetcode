
def valid_anagram(s, t):
    
    char_frequency = {}

    if len(s) != len(t):
        return False

    for char in s:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for char in t:
        if char in char_frequency:
            char_frequency[char] -= 1
            if char_frequency[char] == 0:
                del char_frequency[char]

    if len(char_frequency) == 0:
        return True
    else:
        return False


