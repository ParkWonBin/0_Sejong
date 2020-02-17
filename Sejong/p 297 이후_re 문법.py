import re
p = re.compile('ab*')

# m = p.match("ab")
# print(m)

m1 = p.match("abb")
print(m1)

import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

import re
p = re.compile("([가-힣])[가-힣][가-힣]")
m = p.match("신동욱")

if m:
    print("Match found : ", m.group(0))
    print("Match found : ", m.group(1))
else:
    print("No match")

# 이벤트 페이지 신*욱
import re
p = re.compile("([가-힣])([가-힣])([가-힣])")
m = p.match("신동욱")

if m:
    print("Match found : ", m.group(0)) # 전체
    print("Match found : ", m.group(1)) # 첫 번째 괄호
    print("Match found : ", m.group(2)) # 두 번째 괄호
    print("Match found : ", m.group(3)) # 세 번째 괄호

    print(m.group(1)+ "*" +m.group(3))
else:
    print("No match")

# 이벤트 페이지 휴대폰(대한민국) 번호 010-2731-2579 => 01\d-\d{3,4}-\d{4}, 01[0-9]-\d{3,4}-\d{4}
# 010-2731-2579
# 010-****-2579
# 2579 신*욱

import re
p1 = re.compile("(01\d)-(?P<FN>\d{3,4})-(\d{4})")
m1 = p1.match("010-2731-2579")

p2 = re.compile("([가-힣])([가-힣])([가-힣])")
m2 = p2.match("신동욱")

if m2:
    re_name = m2.group(1) + "*" + m2.group(3)

    if m1:
        print("Match found : ", m1.group(0)) # 전체
        print(m1.group(0))  # 전체
        print(p1.sub("\g<1>", str(m1)))
        print(p1.sub("\g<2>", str(m1)))
        print(p1.sub("\g<3>", str(m1)))
        print(p1.sub(str("\g<1>"+"-"+"****"+"-"+"\g<3>"), str(m1)))

        print(str(m1.group(3)) + " " + re_name)

        tel_group3 = p1.sub("\g<3>",str(m))

        tel_group3 = tel_group3.replace(tel_group3,'****')
        print(tel_group3)

    else:
        print("No match")

tel = "2579"
tel_rep = tel.replace(tel,'****')
print(tel_rep)

import re
p = re.compile('[a-z]+')
m = p.search("python")
print(m)

import re
p = re.compile('[a-z]+')
m = p.search("3 python")
print(m)

import re
p = re.compile('[a-z]+')
result = p.findall("life is too short")
print(result)

import re
p = re.compile('[a-z]+')
result = p.finditer("life is too short")
print(result)
for r in result:
    print(r)

import re
p = re.compile('[a-z]+')
m = p.match("python")

print(m.group())
print(m.start())
print(m.end())
print(m.span())

import re
p = re.compile('[0-9a-zA-Z]+')
m = p.match("2019092928Sunny")

# print(m.group())

year = m.group()[0:4]
print(year)

month = m.group()[4:6]
print(month)

day = m.group()[6:8]
print(day)

temper = m.group()[8:10]
print(temper)

condition = m.group()[10:]
print(condition)

import re
p = re.compile('[a-zA-Z]+')
m = p.search("2019092928Cloudy1578")

# print(m.group())

condition = m.group()
print(condition)

print(m.start())
print(m.end())
print(m.span())

m[m.start():m.end()]

import re
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

import re

data = """신
동욱
"""

p = re.compile('신.동욱', re.DOTALL)
m = p.match(data)
print(m)

import re

p = re.compile('[a-z]+', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

import re

p = re.compile('[a-z]+', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

# 대문자로 변환하는 upper 함수
passport = "shindongwook"
# passport = "ShinDongWook"
# passport = "SHINDONGWOOK"

passport = passport.upper()
print(passport)

import re
passport = "shindongwook"

passport = passport.upper()

p = re.compile('[A-Z]+')
print(p.match(passport))

import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

import re
p1 = re.compile("^신 동욱", re.MULTILINE)
p2 = re.compile("신.동욱", re.DOTALL)

data = """python one
동욱
life is too short
python two
you need python
신 동욱"""

# print(p1.findall(data))
p1 = p1.findall(data)
print(p1)

p2 = p2.findall(data)
print(p2)

p_all = p1 + p2
print(p_all)

# if, replace => \n 없애기

charref = re.compile(r"""
&[#]                # 숫자 데이터 시작시 # 붙이기
(
    0[0-7]+         # 8진수
    |[0-9]+         # 10진수
    |x[0-9a-fA-F]+  # 16진수
)
;                   # 마침표
""", re.VERBOSE)

import re
p = re.compile('\\\\section')

p = re.compile(r'\\section')

import re

p = re.compile('Crow|Servo')
m1 = p.search('CrowHello')
print(m1)

m2 = p.search('ServoHello')
print(m2)

import re

# 아파트 주민회의
p = re.compile('신동욱|신민석|신현갑|신희영|송현숙')
m1 = p.search('장동건고소영송중기신민석')
print(m1)

m2 = p.search('ServoHello')
print(m2)

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

p = re.compile(r'\bclass')
print(p.search('no classic at all'))

p = re.compile(r'class')
print(p.search('the declassified algorithm'))

p = re.compile(r'class\b')
print(p.search('one subclass is'))

import re
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))
print(m.group(1))

import re
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(?P<fn>\d+)[-](?P<mn>\d+)[-](?P<ln>\d+))")
m = p.search("park 010-1234-5678")

# print(m.group(1))
# print(m.group(2))
# print(m.group(3))
# print(m.group(4))
# print(m.group(5))

print(m.group("name"))
print(m.group("phone"))
print(m.group("fn"))
print(m.group("mn"))
print(m.group("ln"))

import re
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m = p.search('Paris in the the spring').group()
print(m)