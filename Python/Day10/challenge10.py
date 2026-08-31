def count_words(words):
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

result = count_words(words)

print(result)