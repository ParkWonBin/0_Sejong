import re

# import
# 파이썬 개발자가 만든 패키지 import
# - 내장 : 파이선 설치시 같이 설치되는 패키지
# - 외장 : 파이선 설치시 설치되지 않는 패키지
# File - Settings - Project 탭 - project interpreter
# 내가 만든 패키지 import

data = """
park 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# re.compile : regular express 패키지 하위에 compile 함수 이용
# (\d{6})[-]\d{7}
# () : 그룹
# \d : 숫자 데이터
# {} : 강제
# {6} : 강제로 6자리
# [-] : 무조건 - 문자가 있어야 됨
# \d : 숫자 데이터
# {} : 강제
# {7} : 강제 7자리

# pat.sub("\g<1>-*******", data))
# sub : substitute
# <1> : 그룹의 첫번째
# -******* : 이 문자 그대로