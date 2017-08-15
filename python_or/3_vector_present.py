vector_a = [1,2,10] # 일반적인 vector 표현과 같음
vector_b = (1,2,10) #튜플로 표현시 중복 데이터는 안들어감
vector_c = {'x':1, 'y':2,'z':10}    # dict 형을 전처리 수행하기 편함

# 벡터 덧셈 표현
u = [2,2]
v = [2,2]
z = [3,5]
#
# result = []
# for i in range(len(u)):
#     result.append(u[i]+v[i]+z[i])
# result

result = [sum(t) for t in zip(u,v,z)]

u = [1,2,3]
v = [4,4,4]

alpha = 2

result = [alpha*sum(t) for t in zip(u,v)]
result
