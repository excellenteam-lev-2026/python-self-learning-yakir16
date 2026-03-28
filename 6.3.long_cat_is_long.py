import math
import string


def long_cat_is_long(text):
    cleaned_text = ''.join(ch.lower() if ch.isalpha() or ch.isspace() else ' ' for ch in text)
    words = cleaned_text.split()
    word_lengths = {word: len(word) for word in words}
    return word_lengths




text ="""
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
if __name__ == "__main__":
    print(long_cat_is_long(text))


