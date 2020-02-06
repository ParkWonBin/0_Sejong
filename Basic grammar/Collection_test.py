from collections import Counter

text = """ 
lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
""".lower().split()
# lower()로 대소문자 구분 없애고, split()으로 나눠줘야 단어별로 구분을 할 수 있다.
print(text)
print(Counter(text))
print(Counter(text[1]))

# ===================================

from collections import Counter

c = Counter(cats=4,dogs= 8)
print(c) # 딕셔너리로 출력된다.

print(list(c.elements())) # value에 숫자만큼 반복하여 출력됨.
# value 값이 0 이하인 것은 출력하지 않는다.

# ===============================

from collections import Counter

c = Counter(a=4,b=2,c=0,d=-2)
d = Counter(a=1.5,b=2,c=3,d=4)
print(c+d) # value를 더한다.
print(c&d) # 교집합된다. list로 폈을 때 몇 개가 겹치는지로 이해하면 편함

# ================================

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(x=11.6,y=22)
print(p)         # >>> Point(x=11.6, y=22)
print(p.x,p.y)   # >>> 11.6 22    //그냥 숫자로 호출
p.x,p.y          # >>> (11.6, 22) //튜플로 나옴
print(p[0]+p[1]) # >>> 33.6       //주소로 부를 수 있음

# ===================================