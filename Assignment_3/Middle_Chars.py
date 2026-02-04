import sys

def get_middle(text):
    length = len(text)
    if length == 0:
        return ""

    mid = length // 2

    if length % 2 == 0:
        return text[mid - 1: mid + 1]
    else:
        return text[mid]

while True:
    user_input = input("\nNhập chuỗi (Nhấn Enter để dừng): ")

    if user_input == "":
        print("Đã dừng chương trình.",file=sys.stderr)
        break

    result = get_middle(user_input)

    print(f"Ký tự ở giữa của '{user_input}' là: '{result}'")