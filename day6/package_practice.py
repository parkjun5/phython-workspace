## 클래스나 함수는 가져오는것은 불가능 모듈이나 패키지를 가져와야한다.
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()

# trip_to.detail()

## import가 아닌 from구문은 함수를 가져오는것이 가능하다.

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

## 별을 쓴단느 것은 모든 것을 가져온다는 의미지만 공개 범위도 설정해야한다.
## init 패키지에서 __all__ 으로 설정해주면 가능한다.
from travel import *

trip_to = vietnam.VietnamPackage()
trip_to.detail()