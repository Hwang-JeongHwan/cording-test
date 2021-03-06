'''
문제
상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

출력
첫째 줄에 상수의 대답을 출력한다.
'''

A,B = input().split()

C = int(A[2]+A[1]+A[0])
D = int(B[2]+B[1]+B[0])

if(C>D):
    print(C)
else:print(D)

# A[0],A[2] = A[2],A[0]
# B[0],B[2] = A[2],B[0]

'''
a, b = input().split()    # a, b에 문자열로 두 수를 각각 입력받습니다.
A = list(a)               # reverse함수를 이용하기 위해 리스트에 담아줍니다.
B = list(b)
A.reverse()               # reverse함수를 사용하여 거꾸로 뒤집어 줍니다.
B.reverse()
x = int(A[0]+A[1]+A[2])   # x, y에 문자열 연산을 이용하여 정수형으로 거꾸로된 수를 넣습니다. 
y = int(B[0]+B[1]+B[2])
if x > y:                 # x가 크면 x를, y가 크면 y를 출력하는 조건문을 씁니다.
	print(x)
else:
	print(y)
    ※ 사실 슬라이싱[::-1]을 이용하거나, 또는 reverse() 함수를 사용할 게 아니라 그냥 문자열의 인덱싱을 사용하여 x =int(A[2]+A[1]+A[0]) 이런 방식으로 .. 더욱 간결하게 문제를 풀 수 있습니다. 하지만 뭔가 reverse 함수를 사용하고 싶었습니다.
'''