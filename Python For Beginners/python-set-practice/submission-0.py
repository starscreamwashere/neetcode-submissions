from typing import List

def contains_duplicate(words: List[str]) -> bool:
    list_length=len(words)
    words_set=set(words)
    set_length=len(words_set)
    diff=list_length-set_length
    if (diff>0):
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
