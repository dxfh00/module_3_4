def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        if i.count(root_word):
            same_words.append(i)

    for i in other_words:
        i = i.lower()
        root_word = root_word.lower()
        if root_word.count(i):
            i = i.title()
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
