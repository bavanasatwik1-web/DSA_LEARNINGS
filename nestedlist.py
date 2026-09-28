'''write a program to print all the even numbers in given nested list'''
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
# for i in numbers:
#     for j in i:
#         if j % 2 == 0:
#             print(j)
'''prime numbers in given nestedlist'''
# r=int(input("enter row:"))
# nl=[]
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         fc=0
#         for k in range(1,nl[i][j]+1):
#             if nl[i][j]%k==0:
#                 fc+=1
#         if fc==2:
#             print(nl[i][j])    
'''sum of all elements in the nl'''
# r=int(input("enter row&coloumn:"))
# nl=[]
# sum=0
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl)):
#     for j in range(len(nl)):
#         sum+=nl[i][j]
# print(sum)    
'''search an element in nl'''
# r=int(input("enter search element:"))
# n=int(input())
# nl=[]
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl)):
#     for j in range(len(nl)):
#         if nl[i][j]==n:
#             print(nl[i][j])
'''max element in nl'''
# n=int(input())
# nl=[]
# for i in range(n):
#     nl.append(list(map(int,input().split())))
# max=float("-inf")    
# for i in range(0,len(nl)):
#     for j in range(len(nl)):
#         if nl[i][j]>max:
#             max=nl[i][j]
# print(max)        
'''2nd max element in nl'''
# n=int(input())
# nl=[]
# max1=float("-inf")
# max2=max1
# for i in range(n):
#     nl.append(list(map(int,input().split())))
# for i in range(0,len(nl)):
#     for j in range(len(nl)):
#         if nl[i][j]>max1:
#             max2=max1
#             max1=nl[i][j]
# print(max2)            
'''sum of each inner list of a nl'''
# r=int(input("enter row:"))
# nl=[]
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))   
# for i in range(0,len(nl)):
#     sum=0
#     for j in range(len(nl)):
#         sum+=nl[i][j]
#     print(sum)        
'''max of diagnol elements'''
# r=int(input("enter row:"))
# nl=[]
# max=float("-inf")
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl)):
#     for j in range(len(nl)):
#         if i==j:
#             if nl[i][j]>max:
#                 max=nl[i][j]
# print(max)            
'''sum of both diagnol elements'''
# r=int(input("enter row:"))
# nl=[]
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))
sp=ss=0
# for i in range(len(nl)):
#     sp+=nl[i][i]
#     ss+=nl[i][(len(nl)-1-i)]
# print(sp,ss)
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         if i==j:
#             sp+=nl[i][j]
#         if i+j==len(nl)-1:
#             ss+=nl[i][j]
# print(sp,ss)
'''identity matrix'''
# r=int(input("enter row:"))
# nl=[]
# b=True
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         if i==j:
#             if nl[i][j]!=1:
#                 b=False
#         else:
#             if nl[i][j]!=0:
#                 b=False
# if b:
#     print("Identity")
# else:
#     print('Not Identity')
'''Traverse the matrix elements coloumn wise'''
# r=int(input("enter row:"))
# nl=[]
# for i in range(0,r):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl[0])):
#     for j in range(0,len(nl)):
#         print(nl[i][j])    
'''surrounded or neighbour elements'''
r=int(input("enter row:"))
nl=[]
for i in range(0,r):
    nl.append(list(map(int,input().split())))
for i in range(len(nl)):
    for j in range(len(nl[i])):
        # print(nl[i][j],end=" ")
        if i!=0:
            print(nl[i-1][j],end=' ')
        if j!=len(nl[0])-1:
            print(nl[i][j+1],end=" ")
        if i!=len(nl)-1:
            print(nl[i+1][j],end=" ")
        if j!=0:
            print(nl[i][j-1],end=" ")            