import re
def A(code):
    pattern = r"^[A-Z]{2,3}\d{3}$"

    if re.match(pattern, code):
        return True
    else:
        return False

user_input = input("me tomb po khor: ")
if A(user_input):
    print("TRUE")
else:
    print("FALSE")