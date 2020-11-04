"""
당신의 회사에서 매주 1회 작성해야하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 한다!

 - X 주차 주간보고 -
 부서 :
 이름 :
 업무 요약 :

 1~ 50주차까지의 보고서 파일을 만드는 프로그램 작성

 조건 파일명은 1주차.txt , 2주차.txt로 해야할것


"""
## 내가 이겼당~
for i in range(1,51):
    # bogosyo_maker = open(f"{i}주차.txt", "w", encoding="utf8")
    #     bogosyo_maker.write(" - {0}주차 주간보고 -\n".format(i))
    # bogosyo_maker.write("부서 : \n")
    # bogosyo_maker.write("이름 : \n")
    # bogosyo_maker.write("업무 요약 : \n\n")
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        report_file.write(" - {0}주차 주간보고 -\n".format(i))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n\n")


