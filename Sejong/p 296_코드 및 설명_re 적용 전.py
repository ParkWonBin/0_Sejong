data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split('\n'): # data.split('\n') : [park 800905-1049118, kim 700905-1059119]
# for 1회, line : park 800905-1049118
# for 2회, line : kim 700905-1059119
    word_result = []

    for word in line.split(" "): # line.split(" ") : [park 800905-1049118, kim 700905-1059119]
# for 1회, word : park
# for 2회, word : 800905-1049118
# for 3회, word : kim
# for 4회, word : 700905-1059119

        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
# len(word) : 1번째 len("park") : 4 == 14 : false(X) : 실행하지 않음
# len(word) : 2번째 len("800905-1049118") : 14 == 14 : true(O) : 실횅
# len(word) : 3번째 len("kim") : 4 == 14 : false(X) : 실행하지 않음
# len(word) : 4번째 len("700905-1059119") : 14 == 14 : true(O) : 실행

# and 함수 (논리곱) : 조건1과 조건2가 모두 만족해야 실행
# 조건1 조건2 결과 0 : false, 1 : true
#  0    0    0
#  0    1    0
#  1    0    0
#  1    1    1

# word[:6] => word[0:6] : 0번지부터 6미만의 번지까지, 주민번호 앞 6자리를 확인하는 용도의 코드
# for 1회, word : park : 제외
# for 2회, word : 800905-1049118 : 선택
# for 3회, word : kim : 제외
# for 4회, word : 700905-1059119 : 선택

# .isdigit()
# .     : 하위의
# is    : 있냐?
# digit : 10진수(숫자)
# ()    : 함수

# word[7:] => word[7:14] : 7번지부터 14미만의 번지까지, 주민번호 뒤 7자리를 확인하는 용도의 코드

# .isdigit()
# .     : 하위의
# is    : 있냐?
# digit : 10진수(숫자)
# ()    : 함수

# if 조건문:
# 조건문 참   : 실행 구문 동작
# 조건문 거짓 : 실행 구문 스킵

            word = word[:6] + "-" + "*******"

# for 2회, word : 800905-*******
# for 4회, word : 700905-*******
# + : 문자열 연결 연산자

        word_result.append(word)

# word_result = ["park", "800905-*******", "kim", "700905-*******"]
# .            : 하위의
# append(word) :
# ap           : after
# pend         : 덧붙이다.

    result.append(" ".join(word_result))
# result = [park 800905-*******, kim 700905-*******]
# join : 합치다.

print("\n".join(result))
# park 800905-*******
# kim 700905-*******


