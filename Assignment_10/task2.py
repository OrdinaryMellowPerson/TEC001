import requests


def dem_chu_tren_web(url):
    print(f"Đang tải dữ liệu từ: {url} ...")
    try:
        response = requests.get(url)

        if response.status_code == 200:
            html_code = response.text

            so_lan = html_code.count("Python")

            print(f"✅ Báo cáo: Chữ 'Python' xuất hiện {so_lan} lần trên trang này!")
        else:
            print(f"🚨 Lỗi: Trang web trả về mã {response.status_code}")

    except Exception as e:
        print(f"🚨 Lỗi mạng hoặc sai URL: {e}")


duong_link = "https://www.python.org/"
dem_chu_tren_web(duong_link)