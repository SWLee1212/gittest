# 문자열 함수 예제

a="agency for defense development"

print(a.capitalize())                   # 첫 글자를 대문자로
print(a.title())                        # 띄어쓰기 기준 첫 글자를 대문자로
print(a.count("a"))                     # 문자열 내 a 문자 갯수
print(a.find("f"))
print(a.startswith("a"))

a=" agency for defense development "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(a.split())                        # 띄어을 구분하여 문자를 단어로 구분함

a= "123"
print(a.isdigit())
a= "aaa"
print(a.islower())
print("12345".isdigit())
print("AAA".isupper())

print("It\'s Ok.")
print("It's Ok.")

a= """It's OK.
Bye. """
print(a)
a="I\'m fine. \nThank you"
print(a)
# \n, \t, \', \e \b
