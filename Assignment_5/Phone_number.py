import re
def phone_numbers(text):
    pattern = r'\+84\d+|\b\d{10}\b'
    redacted_text = re.sub(pattern, '[REDACTED]', text)
    return redacted_text

sample = input("nhap di:")
print(phone_numbers(sample))