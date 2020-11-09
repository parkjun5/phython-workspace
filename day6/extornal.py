# glob : 경로 내의 폴더 / 파일 목록 조의
# import glob
#  ## 확장자가 py인 모든 파일
# print(glob.glob("*"))

#os  운영체제에서 제공하는 기본 기능

import os

# print(os.getcwd())##현재 디렉토리

# floder = "sample_dir"

# if(os.path.exists(floder)):
#     print("이미 존재하는 폴더입니다,.")
#     os.rmdir(floder)
#     print(floder, " 폴더 삭제안료 ")
# else: 
#     os.makedirs(floder) ## 폴더 생성
# #     print(floder, " 폴더 생성안료 ")

# print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d -%H:%M:%S"))

import datetime

print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격

today = datetime.date.today()

td = datetime.timedelta(days =100)

print(" 우리가 만난니 100일은 ", today+td)