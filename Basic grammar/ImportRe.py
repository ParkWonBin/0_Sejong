# 정규식 표현 방법에서 ^, $잘 봐야함.
# 대괄호 안에 있을 때 ^는 '반대'지만, 그냥 ^The 이렇게 쓰면 The로 시작하는 문자 의미


# ====================
import re
input_id = "Sdsf123"
pat = re.compile("[a-zA-Z0-9]+")
# [a-zA-Z0-9] 만 쓰면 맨 앞에 한 글자만 체크한다.
# 뒤에 +를 써주어야 전체 글자를 체크한다.
a = pat.match(input_id)

if a : # 파이썬에서 None값이 아닌 것은 모두 True로 판단하기 때문에 쓸 수 있다.
    print(a)
    print("가입페이지")
else :
    a
    print("조건이 충족되지 않음")


pat = re.compile("(/d{6})[-]/d{7}")
# {}의 역할은 강제이다. /d{5}는 5자리 디짓인지 확인하는 부분임.

# ====================

import re
p = re.compile("[a-z]+")
k = re.compile("[a-z0-9]+")
m = p.match("python")
n = p.match("3python")    # None
l = k.match("3python")
print(l)

# =====================
import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# ================
IOT = "20191210 cloudy 5c Seoul"
import re
# p1 : 소문자 데이터
p1 = re.compile('[a-z]+')
m = p1.match(IOT)  # 해당 문자열이 모두 맞는지
n = p1.search(IOT)  # 해당 문자열에서 조건 맞는 것만 검색
print(m)
print(n)

# p2 : 날짜 데이터
p2 = re.compile('[0-9]+')
n2 = p2.search(IOT)
print(n2)

p3 = re.compile("[A-Z][a-z]+")
m3 = p3.search(IOT)
print(m3)