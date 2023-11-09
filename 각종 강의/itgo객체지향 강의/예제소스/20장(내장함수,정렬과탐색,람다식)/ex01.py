# 내장함수에 대한 실습
# abs() : 절대값을 반환
i = -20
print("-20의 절대값 : ", abs(i))
i = -20.55
print("-20.55의 절대값 : ", abs(i))
print("-------------------------")

# all() : 시퀀스(리스트, 딕셔너리 등)를 받아서 시퀀스의 모든 항목이 참이면 True 반환한다.
# and 조건과 유사하다. 하나라도 0인 값이 들어가면 False 리턴한다.
list1 = [1, 4, 7, 10]    # 모든 값이 참이다.
print(all(list1))
list1 = [0, 0, 0, 1]    # 하나의 값이 거짓이다.
print(all(list1))
print("-------------------------")

# any()함수 : 시퀀스 객체에 있응 한 개의 항목이라도 참인 경우에 참을 반환한다.
# or 개념과 유사하다.
list2 = [0, 7, 10, 20]   # 1개의 값이 False 이므로 True 리턴
print(any(list2))
list2 = [0, 0, 0, 0]     # 모든 값이 False 이므로 False 리턴
print(any(list2))
print("-------------------------")

# bin() 함수 : 10진수를 이진수로 표현해주는 함수. 항상 접두사 0b 로 시작한다.
y = bin(15)
print(y)
print("-------------------------")

# eval() 함수 : 전달된 수식을 구문 분석을 하고 프로그램 내에서 수식의 값을 계산하는 함수.
# exp = input("수식을 입력해주세요 : ")
# print(eval(exp))

# eval()는 전역변수의 수식도 구문을 분석해서 계산해준다.
x = 10
y = 15
print(eval("x*y"))
print("-------------------------")

# sum() : 리스트에 존재하는 항목들의 값을 전부 더하여 합계를 리턴
print(sum([1,10,100]))
print("-------------------------")

# len() : 객체의 길이를 반환하는 함수. 문자열의 길이를 계산하는데 유용하다.
# 리스트에 len() 사용하게 되면 리스트 안에 있는 항목의 개수를 리턴.
# 딕셔너리, 튜플에서도 항목의 개수를 반환
print(len("안녕하세요,hello! _"))
print(len([1,2,3,4,5,6,7]))
dic = {
    "a" : 7,
    "b" : 10,
    "c" : 15
}
print(len(dic))
tup = (2,7,5,4,3)
print(len(tup))
print("-------------------------")

# list() 함수 : 리스트를 생성하는 함수이다.
s = 'abcdefg'
print(list(s))
print("-------------------------")

# map()함수 : 반복가능한 객체(리스트, 튜플 등)의 각 항목에 주어진 함수를 적용한 후 적용 결과
# 를 반환한다.
# 적용시킬 함수 작성
def square(n) :
    return n*n
list3 = [1,2,3,4,5]
tup1 = (1,2,3,4,5)
# list3에 있는 하나하나의 값에 square 함수를 적용시키고 있다
result1 = list(map(square, list3))
# tup1에 있는 하나하나의 값에 square 함수를 적용시키고 있다
result2 = list(map(square, tup1))
print("리스트 적용 : ", result1)
print("튜플 적용 : ", result2)
print("-------------------------")

# dir()함수 : 객체가 가지고 있는 변수나 함수를 보여준다.리스트로 결과를 반환한다.
print(dir([1,2,3]))
print("-------------------------")

# max(), min() : 리스트나 튜플, 문자열에서 가장 큰 항목과 작은 항목은 반환한다.정수에서 가장
# 큰 값과 작은 값을 리턴한다.
values = [1,2,3,4,5]
print(max(values))
print(min(values))
print("-------------------------")

# enumerate() 함수 : 시퀀스 객체를 입력받아서 열거형 객체를 반환한다.열거형 객체는 첫 번째
# 요소로는 번호, 두 번째 값은 번호에 해당하는 값을 갖는 객체이다.열거형이란 한정된 값을 가지고
# 가독성을 높이고 문서화를 하는데 도움을 주는 타입이 바로 열거형이다.
seasons = ["봄", "여름", "가을", "겨울"]
# enumerate()는 start 라는 매개변수가 값을 지정하지 않는다면 0부터 시작한다.
print(list(enumerate(seasons)))
# 스타트값을 이용하면 우리가 원하는 값으로 기준값을 설정할 수가 있다.
print(list(enumerate(seasons, start=1)))
print("-------------------------")

# filter() 함수 : 조건을 제시하는 함수를 만들어서 그 조건에 해당하는 요소를 추출하고자 할 때
# 사용한다.
# 조건을 제시해주는 함수 정의
def myfilter(x):
    return x > 3

result3 = filter(myfilter, (1,2,3,4,5,6,7))
print("3을 초과한 수 : ", list(result3))
print("-------------------------")

# zip() 함수 : 2개의 리스트를 하나로 묶어주는 함수이다.
# 요소의 개수를 맞추어 주는 것이 데이터 누락에 도움이 된다.
numbers = [1,2,3,4]
list4 = ["하나", "둘", "셋", "넷"]
print(list(zip(numbers, list4)))
# for 문 이용한 방법
names = ["신은혁", "김연아", "손연재"]
scores = [100,99,95]
for n, s in zip(names, scores):
    print(n, s)






