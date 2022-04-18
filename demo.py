tp = (1,2,3)
print(type(tp))
print(tp)
print(len(tp))
print(tp[0])

def calc(a,b):
    return  a+b, a*b


#호출
result = calc(3,4)
print(result)

args=(5,6)
print(calc(*args)) #포인터가 아니고 튜플을 담은거다.

#세트는 집합연산
a= {1,2,3,3}
b= {3,4,4,5}
print(a)
print(b)
print(a.union(b)) #합집합
print(a.intersection(b)) #교집합

print('---------------------------------------------------------')

device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device)
print(type(device))
print(len(device))
#print(device{0}) #딕셔너리는 순서가 없다. 에러남
print(device["아이폰"])


for item in device.items():
    print(item)