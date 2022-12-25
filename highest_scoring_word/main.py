def high(text):
    array_text = text.split(" ")
    words_to_int = {}
    ascii_start = 96
    for i in range(len(array_text)):
        words_to_int[array_text[i]] = sum([ord(char) - ascii_start for char in array_text[i]])
    return max(words_to_int, key=lambda k: words_to_int[k])


high('what time are we climbing up the volcano')


# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
