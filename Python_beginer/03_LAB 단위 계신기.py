print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")

Celsius =float(input("변환하고 싶은 섭씨온도를 입력하세요"))
Fahrenheit = 32 + 1.8*Celsius
print("섭씨온도 :", round(Celsius,1))
print("화씨온도 :", round(Fahrenheit,2))

print("본 프로그램은 킬로미터를 마일로 변환하는 프로그램입니다.")
Kilo = float(input("변환하고 싶은 킬로미터를 입력하세요."))
Mile = Kilo/1.609
print("km :", round(Kilo,3))
print("mile :", round(Mile,3))

print("본 프로그램은 Cm를 inch, feet로 변환하는 프로그램입니다.")
Cm = float(input("변환하고 싶은 Cm값을 쓰시오."))
Inch = Cm/2.54
Feet = Cm/30.48
print("cm :", round(Cm,1))
print("ft :", round(Feet,3))
print("inch :", round(Inch,3))