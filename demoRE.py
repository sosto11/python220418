# demoRE.py
import re
print(dir(re))


result =re.search("[0-9]*th", "35th")
# 매칭 오브젝트
print(result)
print(result.group())

result =re.match("[0-9]*th", "35th")
print(result)
print(result.group())

print("-----비교-----")

result =re.search("[0-9]*th", "   35th")
print(result)
print(result.group())

result =re.match("[0-9]*th", "   35th")
print(result)
#print(result.group())


#apple이 있는 경우
print(bool(re.search("apple",'this is apple')))
print(bool(re.match(" apple",'this is apple')))

year = re.search("\d{4}", '올해는 2022년 입니다.')
print(year.group())

postCode = re.search('\d{5}', '우리 동네느 53400')
print(postCode.group())
