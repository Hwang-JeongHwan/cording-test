'''
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109
'''
N = int(input())

l = list(map(int, input().split()))

l1 = list(set(l)) #중복을 제거 하기 위해 set으로 list를 만듬
l1.sort() 
# l1 = list(sorted(set(l))) 으로 대처 가능

'''
for i in range(len(l)):
    l[i]=l1.index(l[i]) # 입력받은 숫자의 정렬된 index 출력

print(*l) 
시간 초과

''' 

dic = {l1[i]:i for i in range(len(l1))}

#print('dic',dic)
#입력: 2 4 -10 4 -9
#dic {-10: 0, -9: 1, 2: 2, 4: 3} 이런식으로 저장됨 

# 딕셔너리 형태 안에서 이런식으로 key value값 설정 가능
# key = l1[i] i인덱스 안의 값, value = i 즉 인덱스임
for i in l : 
    
    print(dic[i],end = ' ') #key i에 대한 value출력


'''
파이썬 기초 자료형 리스트 딕셔너리

이번 포스팅에서는 파이썬에서 기초적으로 다루는 자료형인 리스트와 딕셔너리에서 많이 사용하는 기능들에 대한 예제를 간단히 살펴보도록 하겠습니다.

​

리스트와 딕셔너리의 용도 차이에 대한 감을 다음 예시로 잡아보시면 좋을 듯 합니다.

​

리스트 : 첫 학생은 85점이고, 두번째 학생은 92점이고, 세번째 학생은 15점이고, ...

딕셔너리 : A 학생은 85점이고, B 학생은 92점이고, C 학생은 15점이고, ...


리스트는 순서만 있는 자료형이고, 딕셔너리는 해당 value의 주인공이 어떤 key인지를 나타낸다 정도의 차이라고 보시면 좋을 듯 합니다. 그렇다면 이제부터 파이썬에서 실제 사용 예제를 간단히 살펴보도록 하겠습니다.

​

파이썬 리스트 사용 예제 코드

​

파이썬 리스트 선언하기

리스트 선언은 간단합니다. 원하는 자료들을 순서대로 넣어주면 되는데, 이 때, 다른 프로그래밍 언어와는 달리 한 리스트 안에 들어가는 원소들의 자료형이 일치할 필요는 없습니다. 심지어 리스트 안에 리스트를 넣는 것도 가능합니다.

# 총 6개의 자료로 구성된 리스트 예시
list_a = [1, 3, 'a', 'bcd', [1, 2], (1, 5)]
​

파이썬 리스트 자료 가져오기(인덱싱, 슬라이싱)

파이썬 리스트는 자료의 순서가 몇 번째인지를 기준으로 저장된 값을 가져올 수 있습니다.

저장된 순서의 값에 해당하는 숫자는 0부터 시작한다는 점에 주의해주세요.

통상 자료 1개만 가져오는 경우는 인덱싱이라하고, 2개 이상을 가져오는 경우는 슬라이싱이라고 합니다.

​

다음 코드에서 몇 가지 인덱싱 및 슬라이싱의 예시를 나타내보았습니다.

list_a = [1, 3, 'a', 'bcd', [1, 2], (1, 5)]

# 인덱싱
list_a[0] # 1
list_a[3] # 'bcd'
list_a[4][0] # [1, 2]의 0번째 -> 1

# 슬라이싱
list_a[1:3] # 1~2 번째 -> [3, 'a']
list_a[:4] # 처음부터 ~ 3번째 -> [1, 3, 'a', 'bcd']
list_a[1::2] # 1번부터 2개씩 건너뛰며 -> [3, 'bcd', (1, 5)] 
list_a[::-1] # 순서 거꾸로 -> [(1, 5), [1, 2], 'bcd', 'a', 3, 1]
​

파이썬 리스트 자료 변경, 추가(append, extend), 삭제(remove)

이번에는 리스트 내의 자료를 변경하거나 추가, 삭제하는 방법의 예시를 다루어보겠습니다. 자료 추가는 append 함수, 자료 삭제는 remove 함수로 진행하면 됩니다. 자료 여러개를 동시에 추가하고 싶은 경우는 extend 메소드를 추천합니다.

list_a = [1, 3, 'a', 'bcd', [1, 2], (1, 5)]

# 자료 변경
list_a[2] = 'b' # [1, 3, 'b', 'bcd', [1, 2], (1, 5)]
list_a[2:4] = 'bc' # [1, 3, 'bc', [1, 2], (1, 5)]

# 자료 추가
list_a = [1, 3, 'a', 'bcd', [1, 2], (1, 5)]

list_a.append(2) # [1, 3, 'a', 'bcd', [1, 2], (1, 5), 2]
list_a.append([1, 2]) # [1, 3, 'a', 'bcd', [1, 2], (1, 5), 2, [1, 2]]
list_a.extend([1, 2]) # [1, 3, 'a', 'bcd', [1, 2], (1, 5), 2, [1, 2], 1, 2]

# 자료 삭제
list_a = [1, 3, 'a', 'bcd', [1, 2], (1, 5)]

list_a.remove(1) # [3, 'a', 'bcd', [1, 2], (1, 5)]
list_a.remove([1, 2]) # [3, 'a', 'bcd', (1, 5)]
파이썬 리스트 덧셈, index, reverse, sort

마지막으로 가장 많이 사용하는 리스트 기능들 몇가지를 추가 소개하고 리스트에 대한 설명을 마치겠습니다.

​

리스트는 자료 덧셈이 가능한데, extend 함수와 같은 기능을 합니다. 또한 같은 원소를 여러번 가진 리스트를 곱셈을 이용해서도 선언이 가능합니다.

list_a = [1, 2, 3]
list_b = [4] * 3 # [4, 4, 4]

list_a + list_b # [1, 2, 3, 4, 4, 4]
리스트 내에서 해당 원소의 위치가 몇 번째인지를 알려주는 기능은 index 함수가 제공합니다.

또한, reverse 메소드로 리스트 원소의 순서를 거꾸로 뒤집을 수 있으며, sort 메소드로 리스트 원소를 간단하게 순차적으로 정렬할 수 있습니다.

list_a = [1, 9, 8, 2]

list_a.index(2) # 3
list_a.index(0) # ValueError(없는 원소)

list_a.reverse() # [2, 8, 9, 1]
list_a.sort() # [1, 2, 8, 9]
[출처] 파이썬 리스트, 딕셔너리 (기초 자료형) 예제|작성자 jimmy
파이썬에서 사용하는 기초 자료형인 딕셔너리를 사용하는 방법에 대해 간단히 다루어보겠습니다.

 

딕셔너리 자료형에서는 다른 프로그래밍 언어의 해쉬맵, 해쉬테이블 자료형을 대신하는 역할을 하는데요,

데이터를 key : value pair 형태 로 저장하여 key 값이 주어지면 이에 매칭되는 value를 반환하는 역할을 하는 자료형입니다.

딕셔너리(dict 자료형) 선언
value에는 문자열, 정수, 실수, 리스트, 튜플, 데이터프레임 등 다양한 자료형이 거의 제한없이 들어갈 수 있으나, key에는 리스트 등 자료형은 들어갈 수 없습니다.(튜플은 가능합니다.)

 

key : value 형태로 : 로 구분하여 pair를 지정하고, 쉼표( , )로 pair를 구분해주시면 됩니다.

# 가능한 원소 예시
dict_1 = {'a' : 1, 2 : 'b', 3.5 : [1, 2], (1, 2, 3) : 6.5}

# 불가능한 원소 예시 (TypeError: unhashable type: 'list')
dict_2 = {[1, 2] : 3}
 

딕셔너리 값 찾기, get 함수, 새로운 값 추가, 값 수정, 값 삭제
우선, 기본적으로 key에서 value를 찾는 방법을 설명해보겠습니다.

[] 모양으로 key를 감싸주거나 get 함수를 이용하는 방법도 있습니다.

dict_a = {'a' : 12, 'b' : 89, 'c' : 75}

print(dict_a['a']) # 12 출력
print(dict_a.get('b')) # 89 출력
get 함수는 없는 원소에 대해서는 None을 반환합니다. []로 없는 key 탐색 시에는 error를 반환합니다.

dict_a = {'a' : 12, 'b' : 89, 'c' : 75}

print(dict_a.get('d')) # None 출력
print(dict_a['d']) # KeyError 발생
새로운 원소를 추가하거나 수정, 삭제하는 것은 다음 코드처럼 진행할 수 있습니다.

dict_a = {'a' : 12, 'b' : 89, 'c' : 75}

# 기존 값 수정
dict_a['b'] = 34

# 새로운 값 선언
dict_a['d'] = 56

# 값 삭제
del dict_a['a']

print(dict_a) # {'b': 34, 'c': 75, 'd': 56}

 
딕셔너리 순회(keys, values, items), 역방향 탐색(value to key)
마지막으로 딕셔너리 내 자료들을 순회하는 방법과 역방향 탐색을 하는 예시 코드를 보여드리겠습니다.

딕셔너리 내 key는 keys()로, value는 values()로, key - value pair는 items()로 조회할 수 있으며, for 문 등을 통한 순회가 가능합니다.

dict_a = {'a' : 12, 'b' : 89, 'c' : 75}

# key 나열
print(dict_a.keys()) # dict_keys(['a', 'b', 'c'])

# value 나열
print(dict_a.values()) # dict_values([12, 89, 75])

# key : value pair 나열
print(dict_a.items()) # dict_items([('a', 12), ('b', 89), ('c', 75)])

# key 순회 예시(a, b, c 차례로 출력)
for key in dict_a.keys():
    print(key)
마지막으로 value에서 key 방향으로 역방향 탐색을 하는 예시를 보여드리며, dict자료형에 대한 포스팅을 마무리하도록 하겠습니다. 이 경우는 여러 가지 방법이 있지만, 가장 간단한 방법은 역방향 딕셔너리를 생성한 뒤에, 기존 value를 가지고 key를 탐색해주면 됩니다.

dict_a = {'a' : 12, 'b' : 89, 'c' : 75}

# 역방향 딕셔너리 생성(key와 value가 뒤집힌 형태)
dict_b = {v:k for k, v in dict_a.items()}

print(dict_b[89]) # b 출력
'''