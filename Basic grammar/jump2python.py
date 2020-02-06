import re

p2 = re.compile("^python\s\w+", re.MULTILINE)
# /s는 space, 띄어쓰리랑 줄바꾸기 의미
# /w는 world, 단어
# re.compile은 원래 한 라이만 갖고오기 때문에, 여러 줄 찾으려면 re.MULTILINE 필요

data = '''
life is too short
python two 
you need python
python three
'''

print(p2.findall(data))

# =====================

charref = re.compile(r"""
&[#]                    # ㅅ숫자 개체 시작시 참고
(
    o[0-7]+             # 8진수
    | [0-9]+            # 10진수
    | x[0-9a-fA-F]      # 16진수
)
;                       # 마치는 세미콜론 기호
""", re.VERBOSE)
# re.VERBOSE 역할 : 문자열 안에 주석 있다.

import re
p3=re.compile('Crow|Servo')
m = p3.match('ServoHelloCrow')
# 겹치는 게 있으면 먼저 나온 거 하나만 인식
print(m)

print(re.search('^Life','Life is too short'))
print(re.search('Life$','my Life'))

# \A 첫 문자
# \Z 마지막 문자
# \b 바운더리 (white space로 구분됨)
# \B 바운더리 \b와는 반대로, white space로 구분되지 않는 것들만 인식
# r""를 쓰지 않으면 '\'하나를 입력할 떄 '\\'이렇게 두번씩 입력해야함.

p4 = re.compile(r"\bclass\b")  # class 앞뒤로 띄어써야 인식
print(p4.search("the declassfied algorithm"))
print(p4.search("one subclass is"))
print(p4.search("one class is"))

p5 = re.compile(r"\Bclass\B")
print(p5.search("the declassfied algorithm"))
print(p5.search("one subclass is"))
print(p5.search("one class is"))

p6 = re.compile(r"\b신\B")
m = p6.findall("신동욱 강사가 신발을 신고 당신이라고 불렀습니다.")
print(len(m)) # '신'으로 시작하는 단어가 몇개인지 세는 것


p7 = re.compile('(ABC)+')
m = p7.search('ABCABCABCABCABC OK?')
print(m)
print(m.group(0))   # 0 : 전체
print(m.group(1))   # 1 : 첫번쨰 괄호
# compile할 떄 괄호로 묶은 게 Group이 된다.

p8 = re.compile(r'(\w+)\s+(\d+[-]\d+(\d[-]))')
m = p8.search("park 010-1234-1234")
print(m)
print(m.group(0))
print(m.group(3))

p9 = re.compile(r'(\b\w+)\s+\1')
print(p9.search('Paris in the the spring').group())

# Group에 이름을 지을 수 있다.

p11 = re.compile(r'(?<word>\b\w+)\s+(?P=word)')

# 정규식에서 '.'은 줄바꿈을 제외한 모든 문자, '+'는 연결 연산자.
p12 = re.compile(".+:")
# 이렇게 표시하면, ':' 앞에 있는 모든 문자를 선탁한 것
m = p12.search("http://google.com")
print(m.group())
# re 오브젝트는 문자열에서 처럼 split를 사용할 수 없음

p13 = re.compile(".+(?=:)")
m = p13.search("http://google.com")
print(m.group())

p14 = re.compile(".+(?=:)")
m = p14.search("ftp://sam123.dothome.co.kr")
print(m.group())

if m.group() == "ftp":
    print("파일 전송 프로토콜입니다.")
elif m.group() == "http":
    print("http 페이지입니다. ")
else :
    print("제대로된 파일을 올려주세요.")

# ^의 의미는 두 가지다.
# [^b] 는 b가 아닌 것.
# ^[b] 는 b로 시작하는 것

# ======================
# 부정형 탐색자

p15 = re.compile(".*[.](?!bat$|exe$).*$")
m = p15.search("응용 소프트웨어.auto")
print(m.group())


# ==================
p17 = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p17.sub("\g<phone> \g<name>","park 010-1234-1234"))

