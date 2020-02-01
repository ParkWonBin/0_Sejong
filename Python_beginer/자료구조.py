# steak Test ======================
# >>> first in last out
word = input("input a word: ")
word_list = list(word)
print(word_list)
result = []
for _ in range(len(word_list)):
    result.append(word_list.pop())
print(result)

# que Test ==========================
# >>> first in first out
a= [1,2,3,4,5]
a.append(10)
print(a)
a.pop(0)
# pop(i)는 i번쨰 요소를 빼고 반환한다.
print(a)

# tuple Test ==========================
# >>> 읽기 전용으로 만듬.
# 옛날에 명세서를 그냥 주니까 0 하나 더 써서 돌려줌.
# 수정이 불가능한 형태로 주고 받기 위해 읽기전용을 만듬.
t=(1,2,3)
print(t+t,t*2)

# set Test ==============================
# : 중복을 허용하지 않을 때 사용한다. 삭제,변경 가능
# 집합 연산이 가능하다.
s = set([1,2,3,4,1,2,3])
print(s)
# >>> {1,2,3,4}
s.clear()
print(s)
s = set([1,4,6,78,3])
s.update([1,2,3,4])
# 중복되는 부분은 무시하고 달라진 부분만 업데이트 된다.
print(s)

s1 = set([1,2,3,4,5])
s2 = set([2,4,6,8,10])
print(s1.union(s2)) # 합집합
print(s1|s2)
print(s1.intersection(s2)) # 교집합
print(s1&s2)
print(s1.difference(s2)) # 차집합
print(s1-s2)

# dictionary Test ============================
# dic  선언 및 사용
student_info = {201500012:'Sungchul',2014005:'Juing'}
print(student_info[2014005])
print(student_info)
# dic 요소 추가 및 전체 출력
country_code = {"America":1, "Korea":82, "China":56, "Japan":81}
print(country_code["Korea"])
country_code["German"] = 49
print(country_code.keys())
print(country_code.values())
# dic을 사용한 반복문
for k,v in country_code.items():
    print("Key :", k)
    print("Value :", v)

# dic을 사용한 자료 정리
data = {"name":["갑","을","병","정"],"age":[34,24,26,23] }
print(data["name"][0])
for i in range(len(data["name"])):
    print("이름 :",data["name"][i] ,"/ 나이 :", data["age"][i])
# dic을 이요한 조건
print("Korea" in country_code.keys()) # key 와 value로 묶어놓은 두 개의 리스트 같다.
