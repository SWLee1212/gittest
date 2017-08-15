# 3주차 실습 화씨 변환기
# 섭씨 온도를 입력하면 화씨로 변환
# 화씨 온도 = ((9/5) * 섭씨온도) + 32

print("변환하고 싶은 섭씨 온도를 입력하세요 : ")

InTemp = float(input());
OutTemp = ((9/5)*InTemp) +32;

print("섭씨온도", InTemp)           #print에서 str 변환없이도 변수 출력 가능
print("화씨온도", OutTemp)
