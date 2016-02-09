def reverse(text):
    """

    :rtype: String
    """
    result = ""
    for i in range(len(text) - 1, -1, -1):
        print i, len(text)
        result += text[i]
    return result

def anti_vowel(text):
    result = ""
    for i in range(0, len(text), 1):
        if text[i].lower() not in ['a','e','i','o','u', 'ö','ä','ü']:
            result += text[i]
    return result

def censor (text, word):
    lst = text.split()
    for i in range(0, len(lst),1):
        if lst[i] == word:
            lst[i] = "*" * len(lst[i])
    return " ".join(lst)

#print reverse(raw_input('Give me a word!'))

print anti_vowel(raw_input('Antovowel it!'))