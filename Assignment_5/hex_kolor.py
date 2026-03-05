import re
def B(hex_string):
    pattern = r'^#[0-9A-Fa-f]{6}$'

    if re.match(pattern, hex_string):
        return True
    else:
        return False

hex_input = input("Enter a hex string: ")
if B(hex_input):
    print("Hex string is valid")
else:
    print("Hex string is not valid")