# module을 호출할 클라이언트 코드임
# namespace  개념을 활용하여 모듈 내 특정 함수 및 클래스 호출 방법

#import fah_converter
#import fah_converter as fah                             # 모듈을 import할 때 별칭(alias)으로 import함
#from fah_converter import convert_c_to_f                # 모듈을 import할 때 특정 함수 또는 클래스만 import 함
from fah_converter import *                              # 모듈을 import할 때 모든 함수 또는 클래스만 import 함
                                                         # 필요없는 함수 또는 클래스를 모두 메모리에 로딩하기 때문에 비효율적임
                                                         # 필요한 특정 시험에 특정한 함수만 로딩하는 것이 가장 효율적임        

print("Enter a celsius value : ")
celsius = float(input())
#fahreheit = fah_converter.convert_c_to_f(celsius)
#fahreheit = fah.convert_c_to_f(celsius)
fahreheit = convert_c_to_f(celsius)                      # 함수 또는 클래스를 호출할 때 함수명 앞에 모듈명을 쓸 필요가 없음

print("That's ", fahreheit, " degrees fahreheit!")
