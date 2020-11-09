# import theater_module
# ## import 같은 위치 py를 가져옴

# theater_module.price(3)
# theater_module.price_soldier(4)
# theater_module.price_morning(5)

# import theater_module as tm
# ## import 같은 위치 py를 가져옴

# tm.price(3)
# tm.price_soldier(4)
# tm.price_morning(5)

# # theater moudle에서 전부 사용하겠다.
# from theater_module import *

# price(3)
# price_morning(3)
# price_soldier(3)
# ## 필요한 함수만 가져ㅓ오기
# from theater_module import price,price_morning
# price(5)
# price_morning(5)

from theater_module import price_soldier as price
price(5)