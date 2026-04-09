def tinh_toan_file():
    try:
        with open("numbers.txt", "r", encoding="utf-8") as file_in:
            noi_dung = file_in.read()

        danh_sach_so = []
        for x in noi_dung.split():
            danh_sach_so.append(float(x))

        if len(danh_sach_so) == 0:
            print("File không có số nào!")
            return

        tong = sum(danh_sach_so)

        tich = 1
        for so in danh_sach_so:
            tich = tich * so

        trung_binh = tong / len(danh_sach_so)

        with open("results.txt", "w", encoding="utf-8") as file_out:
            file_out.write(f"Tong (Sum): {tong}\n")
            file_out.write(f"Tich (Product): {tich}\n")
            file_out.write(f"Trung binh (Average): {trung_binh}\n")

        print("🎉 Đã tính xong! Trò hãy mở file results.txt ra xem nhé.")

    except FileNotFoundError:
        print("🚨 Lỗi: Trò chưa tạo file 'numbers.txt' rồi!")

tinh_toan_file()