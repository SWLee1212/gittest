# 연습 당신은 무슨 학교를 다니세요?
# 태어난 연도를 계산하여 학교 종류를 맞추는 프로그램


print("당신이 태어난 연도를 입력하세요.")

intGetBirthYear = int(input())

age = 2017 - intGetBirthYear +1;
print(age)

if age<= 26 and age >= 20:
    print("대학생")
elif age < 20 and age >= 17:
    print("고등학생")
elif age < 17 and age >= 14:
    print("중학생")
elif age < 14 and age >= 8:
    print("초등학교")
else:
    print("학생이 아닙니다.")
