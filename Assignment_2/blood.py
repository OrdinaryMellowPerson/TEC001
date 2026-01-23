
import sys
def hemoglobin_value () :
    sex = input("nhập giới tính ở đây_[male/female]: ").lower()

    if sex != "male" and sex != "female" :
        print("I said 'giới tính', are u okey?", file=sys.stderr)
        return
    try:
        hemoglobin_value = float(input("điền chỉ số ở đây_[g/l]: "))
    except ValueError:
        print("này, tôi đang quan tâm bạn đấy, nghiêm túc đi!", file=sys.stderr)
        return

    if sex == "male":
        if hemoglobin_value < 117 :
            print("thấp quá rồi!", file=sys.stderr)
        elif hemoglobin_value > 155 :
            print("impressive! u're gonna be cooked soon😭", file=sys.stderr)
        else :
            print("U are good to go man, stay strong!")
    if sex == "female":
        if hemoglobin_value < 134 :
            print("gurl, để ý bản thân hơn nhé. I'm not your boifriend!", file=sys.stderr)
        elif hemoglobin_value > 167 :
            print("Ma'am, nausea là thứ cô nên tránh ngay đi!", file=sys.stderr)
        else:
            print("U're as beauty as your hemoglobin rate, what a DIVA!")
hemoglobin_value()