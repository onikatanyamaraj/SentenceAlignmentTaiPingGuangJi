def align():
    print("!!!")
    with open("C:/Users/WINTOUR/Desktop/太平广记文白对齐.txt", "r+", encoding="utf-8") as r:
        with open(r"C:/Users/WINTOUR/Desktop/太平广记文言文.txt", "r+", encoding="utf-8") as f1:
            with open("C:/Users/WINTOUR/Desktop/太平广记白话文.txt", "r+", encoding="utf-8") as f2:
                for i in range(12046):
                    r.write("【原文】")
                    r.write(f1.readline())
                    r.write("【译文】")
                    r.write(f2.readline())
                    r.read()
align()