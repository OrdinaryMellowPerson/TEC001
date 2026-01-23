import sys
def leapyear_check():
    try:
        year = int(input("Enter a year to check: "))
    except ValueError:
        print("Please enter a valid year", file=sys.stderr)
        return
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("chuẩn leap year rồi!")
        else:
            print("sai rồi cu!", file=sys.stderr)


leapyear_check()