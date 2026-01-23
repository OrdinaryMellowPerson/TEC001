import math
import sys


def calculate_unit_price(diameter_cm, price_usd):

    diameter_m = diameter_cm / 100

    radius_m = diameter_m / 2

    area_m2 = math.pi * (radius_m ** 2)

    unit_price = price_usd / area_m2
    return unit_price

def compare_pizzas():
    print("--- 🍕 CÔNG CỤ SO SÁNH GIÁ PIZZA 🍕 ---")
    try:

        d1 = float(input("\nNhập đường kính Pizza thứ 1 (cm): "))
        p1 = float(input("Nhập giá tiền Pizza thứ 1 (USD): "))


        d2 = float(input("\nNhập đường kính Pizza thứ 2 (cm): "))
        p2 = float(input("Nhập giá tiền Pizza thứ 2 (USD): "))
    except ValueError:

        print("\nLỗi: Bạn phải nhập bằng con số! Vui lòng chạy lại chương trình. ❌", file=sys.stderr)
        return

    unit_price1 = calculate_unit_price(d1, p1)
    unit_price2 = calculate_unit_price(d2, p2)

    print(f"\n--- KẾT QUẢ ---")
    print(f"Đơn giá Pizza 1: {unit_price1:.3f} USD/m²")
    print(f"Đơn giá Pizza 2: {unit_price2:.3f} USD/m²")


    if unit_price1 < unit_price2:
        print("\n=> Pizza thứ 1 đáng đồng tiền bát gạo hơn! ✅")
    elif unit_price2 < unit_price1:
        print("\n=> Pizza thứ 2 đáng đồng tiền bát gạo hơn! ✅")
    else:
        print("\n=> Hai loại Pizza có giá trị như nhau.")


compare_pizzas()