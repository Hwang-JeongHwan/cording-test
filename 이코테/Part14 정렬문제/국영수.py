n = int(input())
student = []

for _ in range(n):
    student.append(input().split())
#print(student)

student.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(n):
    print(student[i][0])