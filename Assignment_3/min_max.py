import sys

smallest = None
biggest = None
while True:
    user_input = input("Nhập một số (nhấn Enter để kết thúc): ")
    if user_input == "":
        break
    try:
        num = float(user_input)

        if smallest is None or num < smallest:
            smallest = num
        if biggest is None or num > biggest:
            biggest = num

    except ValueError:
        print("\nLỗi: Không phải là số hợp lệ!", file=sys.stderr)

print("-" * 36)
if smallest is not None:
    print(f"✅ Số nhỏ nhất: {smallest}")
    print(f"✅ Số lớn nhất: {biggest}")
else:
    print("Bạn chưa nhập số nào hợp lệ!",file=sys.stderr)