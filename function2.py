#function2.py
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"##

    for key in user.keys():
        str += key + "=" + user[key] +"&"
        
    return str

print(userURIBuilder("test.com","8080",id="kim",passwd="1234"))

userURIBuilder("test.com","8080",id="Park",passwd="5678",name="Mike")



#람다함수 ( 이름이 없는 간결한 함수 정의)
g = lambda x,y:x*y
print(g(3,4))
#보통은 정의하고 바로 호출
print((lambda x:x*x)(5))
print(globals())

d={"a":100,"b":200,"c":300}
for k,v in d.items():
    print(k,v)
