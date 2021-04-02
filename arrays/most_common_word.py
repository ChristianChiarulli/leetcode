from collections import defaultdict
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:

    clean_input = []

    for char in paragraph:
        if char.isalpha():
            clean_input.append(char.lower())
        else:
            clean_input.append(" ")

    list_of_words = "".join(clean_input)

    words = list_of_words.split()

    word_count = defaultdict(int)

    for word in words:
        if word not in banned:
            word_count[word] += 1

    v = list(word_count.values())
    k = list(word_count.keys())

    return k[v.index(max(v))]

    # print(word_count.get("ball"))
    # return max(word_count, key=word_count.get)


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))


# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
