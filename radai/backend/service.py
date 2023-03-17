import re
from fastapi import HTTPException
from string import punctuation

def pig_latin(sentence):
    if not isinstance(sentence, str):
        raise HTTPException(status_code=400, detail="Sentence must be a string")
        return None;
    words = sentence.split()
    result = []
    for word in words:
        sign = ''
        if word[-1] in punctuation:
            sign = word[-1]
            word = word[:-1]
        converted_word = handle_word(word)
        if sign:
            converted_word += sign
        result.append(converted_word)
    return ' '.join(result)
    
def handle_word(word):
    flag = False
    if word[0].isupper():
        word = word.lower()
        flag = True
    for char in word:
        if char in "aeiou":
            if flag:
                return word[0].upper() + word[1:] + "ay"
            return word+'ay'
        else:
            word = word[1:]+char
    if flag:
        return word[0].upper() + word[1:] + "ay"
    return word+'ay'


if __name__ == "__main__":
    test = "Hello, how are you? I'm fine, thank you."
    print(pig_latin(test))