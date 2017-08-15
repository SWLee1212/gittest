# dictionary type 변수 활용 예제

# dictionary 변수 선언
student_info = {1:"Lee", 2: "Jung", 3:"Gong"}
print(student_info)
print(type(student_info))

# 새로운 변수 추가 및 변경
student_info[4] = "Yang"
student_info[2] = "Kim"
print(student_info)

country_code = {"USA":1, "Kor":82, "china":86, "Japan":81}
print(country_code)
print(country_code.items())
print(country_code.keys())
print(country_code.values())
country_code["Ger"] = 49
print(country_code)

print("Ger" in country_code.keys())
print(81 in country_code.values())

for index in country_code.keys():
    print(country_code[index])
