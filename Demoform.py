# Demoform.py

# web2.py 
#웹서버와 통신
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType('Demoform.ui')[0]

class Demoform(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt 데모")


    def first(self):
        print('first!!')


        #파일에 저장
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        #페이지 번호를 생성
        for i in range(1,6): 
            #웹서버에 요청
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print(url)
            data = urllib.request.urlopen(url)
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")

            for item in cartoons:
                title = item.find("a").text 
                print(title.strip())
                f.write(title + "\n")

        f.close() 








    def second(self):
        print('second')
    def third(self):
        print('third')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoWinodw = Demoform()
    demoWinodw.show()
    app.exec_()