# conda 가상 환경에서 패키지 설치하는 방법
# mypython이라는 가상 환경을 만들고 파이썬 버전은 3.4로 함

# window cmd 창에서 실행 하면 됨
conda create -n mypython python =3.4

activate mypython           # 나의 가상환경 실행
deactivate mypython         # 나의 가상환경 종료

conda install matplotlib    # matplotlib 패키지를 나의 가상환경에 설치
#http:matplotlib.org에 상세한 내용이 있음
