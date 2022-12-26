from bs4 import BeautifulSoup
import re
import os


def extract(path):
    htmlfile = open(path, "r", encoding="utf-8")
    htmlhandle = htmlfile.read()
    # 创建beautifulsoup对象,调用Beautifulsoup解析功能，解析器lxml
    soup = BeautifulSoup(htmlhandle, "lxml")
    # 按标签将文言文和白话文部分分别提取出来
    with open("C:/Users/WINTOUR/Desktop/太平广记文言文.txt", "r+", encoding="utf-8") as f:
        for tag in soup.find_all("p", {"class": re.compile("bodycontent$|top$")}):
            f.read()
            f.write(tag.get_text(strip=True)+"\n")
    with open("C:/Users/WINTOUR/Desktop/太平广记白话文.txt", "r+", encoding="utf-8") as f:
        for tag in soup.find_all("p", {"class": re.compile("kaiti$")}):
            f.read()
            f.write(tag.get_text(strip=True)+"\n")

if __name__ == '__main__':
    file = r"D:\太平广记\OEBPS"
    for root, dirs, files in os.walk(file):
        for i in range(len(files)):
            extract("D:/太平广记/OEBPS/"+files[i])
