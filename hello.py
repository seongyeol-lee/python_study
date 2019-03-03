'''
#----------------------------------------------------
#문자열 연습


str_a = "Hello python Programming"


str_upper = str_a.upper()
str_lower = str_a.lower()

print(str_upper)
print(str_lower)

print(str_a)



#find 함수 rfind 함수 어디에 위하는지 확인할때

output_a = str_a.find("m")
output_b = str_a.rfind("l")

print(output_a)
print(output_b)


#in 연산자

print("# 문자열 in 연산자")
print('"안녕" in "안녕하세요" =',"안녕" in "안녕하세요")
print('"잘자" in "안녕하세요" =',"잘자" in "안녕하세요")


#split() 함수 문자열을 자를때 사용

output_1 = "10 20 30 40 50"

output_2 = "10 20 30 40 50".split(" ")

print(output_1)
print(output_2)



#인치단위를 cm로 변환

inch = int(input("inch를 입력해주세요 : "))
inch_cm = inch * 2.54

print(inch_cm,"cm" )


#kg 단위를 입력받아 파운드 단위를 구하는 코드
print("kg 를 pound 변환")

kg_pound = float(input("kg을 입력해주세요")) * 2.20462262

print(kg_pound,"pound")
'''
'''
# 원의 반지름을 입력받아 원의 둘레와 넓이를 구하는 코드를 작성
print("원의 둘레와 넓이 구하는 코드")

half = int(input("원의 반지름을 입력해주세요"))

circumference = half * 2 * 3.14

tract = half * half * 3.14

print("원의 둘레 : ",circumference)

print("원의 넓이 : ",tract)


#문자 스왑하는 방법
a = input("문자열 입력> :")
b = input("문자열 입력> :")

print(a,b)

a,b = b,a

print(a,b)

'''
print(10 == 100) #fa
print(10 != 100) #tr
print(10 < 100) #tr
print(10 > 100) #fa
print(10 <= 100) #tr
print(10 >= 100) #fa
