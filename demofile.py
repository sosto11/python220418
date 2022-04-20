# demofile.py
url = "http://www.credu.com/?page=" + str(1) 
print(url)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---약간 변경---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---약간 변경---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(10))

    

print("{0:x}".format(10))
print("{0:.2f}".format(4/3))

#파일 생성
f = open("c:\\work\\demo.txt","wt",encoding="utf-8")
f.write("하나\n\t둘\n셋\n\n")
f.close()

