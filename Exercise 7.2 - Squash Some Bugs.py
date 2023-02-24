def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word = new_word + word[i] + "_"
        print(f"i = {i}; new word = {new_word}")
    return new_word


phrase = "hello"
print(add_underscores(phrase))
