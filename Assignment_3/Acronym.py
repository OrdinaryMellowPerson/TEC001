def get_acronym(sentence):
    words = sentence.split()

    if len(words) == 0:
        return ""

    acronym = ""

    for word in words:
        acronym = acronym + word[0].upper()
    return acronym

user_input = input("Nhập cụm từ của bạn: ")

result = get_acronym(user_input)
print(f"Từ viết tắt là: {result}")