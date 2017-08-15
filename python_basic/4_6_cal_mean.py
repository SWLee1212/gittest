# 이차원 리스트 처리하기

kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score = [kor_score, math_score, eng_score]

loopindex = 3;
sum = 0;
for i in range(0,3) :                               # for 문은 range를 지정해줘야 함 예를 들어 range(0,3)은 0,1,2 임
    sum = sum+ midterm_score[i][0]                  # range(0,10,2) 0,2,4,6,8 순으로 증가함
    print(midterm_score[i][0])
else :
    sum = float(sum/loopindex)
    print(sum)

student_score=[0,0,0,0,0]

for subject in midterm_score:                       # for 문을 사용하여 리스트 2차원 변수 접근 하는 방법
#    print(subject)
    i=0;
    for score in subject:                           # 리스트 2차원 변수를 다시 1차원 리스트 변수 상태에서 접근
        student_score[i] += score
        i+=1
#        print(score)
else:
    a,b,c,d,e = student_score                       # 리스트 변수 unpakcing
    print(a,b,c,d,e)
    student_average = [a/3, b/3, c/3, d/3,e/3]
    print(student_average)
