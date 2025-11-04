def sort_on(d):
    return d["num"]

def word_counter(books_text):
    num_words = 0
    words = books_text.split()
    num_words = len(words)
    return num_words

def char_counter(books_text):
    text = books_text.lower()
    counts = {}
    for ch in text:
        if (ch in counts) == False:
            counts[ch] = 1
        else:
            counts[ch] += 1
    return counts

def sort_list(counts):
    chars = []
    for ch, cnt in counts.items():
        if ch.isalpha() == True:
            chars.append({"char": ch, "num": cnt})
        else:
            continue
    chars.sort(key=sort_on, reverse=True)
    return chars


    