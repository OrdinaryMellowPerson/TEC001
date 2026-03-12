def word_frequency(text):
    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    top_5 = sorted_words[:5]

    total_words = len(words)
    top_5_sum = 0

    for item in top_5:
        top_5_sum = top_5_sum + item[1]

    proportion = (top_5_sum / total_words) * 100

    print(f"Top 5: {dict(top_5)}")
    print(f"Total number of words: {total_words}")
    print(f"Proportion of 5 most common words: {top_5_sum} / {total_words} = {proportion:.2f}%")
user_text = input("Write your sentence: ")
word_frequency(user_text)