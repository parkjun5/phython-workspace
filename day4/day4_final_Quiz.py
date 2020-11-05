"""
총 3대의 매울이 있습니다.

강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년




"""

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
       
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    
    def show_detail(self):
        print("{0} {1} {2} {3} {4}"\
            .format(self.location, self.house_type, self.deal_type\
                , self.price, self.completion_year ))

ex1 = House("강남","아파트","매매","10억","2010년")
ex2 = House("마포","오피스텔","전세","5억","2007년")
ex3 = House("송파","빌라","월세","500/50","2000년")

ex_list = []
ex_list.append(ex1)
ex_list.append(ex2)
ex_list.append(ex3)

print("총 {0}대의 매물이 있습니다. ".format(len(ex_list)), end ="\n\n")
for ex in ex_list:
    ex.show_detail()