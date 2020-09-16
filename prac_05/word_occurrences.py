word_count = {}
sentence = input("Enter words: ")
words = sentence.split()
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1
print(word_count)
words = list(word_count.keys())
words.sort()
max_len = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_len, word_count[word]))
