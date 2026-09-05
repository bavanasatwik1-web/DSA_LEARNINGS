'''Basic List Questions'''

'''1. Write a program to create a list by taking input from the user and print the list.'''
# l=list(map(int,input().split()))
# print(l)
'''2. Write a program to insert an element at a specific index in a list.'''
# l=[10,20,30,40,50]
# k=60
# i=3
# l.insert(i,k)
# print(l)
'''3. Write a program to merge two lists into a single list.'''
# l1=[10,20,30,40,50]
# l2=[60,70,80,90]
# l=l1+l2
# print(l)
# l1.extend(l2)
# print(l1)
'''4. Write a program to remove a specific element from a list.'''
# l=[10, 20, 30, 40, 50, 60, 70, 80, 90]
# l.remove(30)
# print(l)
'''5. Write a program to remove an element from a list using its index.'''
# l=[10, 20, 30, 40, 50, 60, 70, 80, 90]
# i=3
# l.pop(i)
# print(l)
'''6. Write a program to find the index of a given element in a list.'''
# l=[10, 20, 30, 40, 50, 60, 70, 80, 90]
# k=80
# i=l.index(k)
# print(i)
'''7. Write a program to count the number of occurrences of an element in a list.'''
# l=[10, 20, 30, 40, 50, 60, 70, 80,80,90]
# k=80
# c=0
# for i in l:
#     if i==k:
#         c=c+1
# print(k,'->',c)
'''8. Write a program to find the sum of the first and last elements of a list.'''
# l=[10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(l[0]+l[-1])
'''9. Write a program to calculate the sum of list elements up to a given index.'''
# l=[10, 20, 30, 40, 50, 60, 70, 80, 90]
# i=6
# sum=0
# for j in range(0,i+1):
#     sum=sum+l[j]
# print(sum)
'''10. Write a program to calculate the average of odd numbers in a list.'''
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum=c=0
# for i in l:
#     if i%2==1:
#         sum=sum+i
#         c=c+1
# print(sum//c)
'''11. Write a program to print all prime numbers present in a list.'''
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i>1:
#             print(i,end=" ")
'''12. Write a program to print the next prime number for each element in the list'''
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in l:
#     i=i+1
#     b=0
#     while b==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             if i>1:
#                 print(i,end=" ")
#                 b=1
#         i=i+1
'''13. Write a program to print the list in reverse order.'''
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# l.reverse()
# print(l)
# print(l[: : -1])
'''14. Write a program to find sum of any two elements which is equal to key value'''
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# k=9
# for i in l:
#     for j in l:
#         if i+j==k:
#             print(i,j)

'''Maximum & Minimum'''

'''15. Write a program to find the largest number in a list.'''
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# s=0
# for i in l:
#     if i>s:
#         s=i
# print(s)
'''16. Write a program to find the second largest number in a list.'''
# l=[10,20,30,15,45,35]
# k=2
# l.sort()
# print(l[len(l)-k])
# h1=float("-inf")
# h2=h1
# for i in range(len(l)):
#     if l[i]>h1:
#         h2=h1
#         h1=l[i]
#     elif l[i]>h2 and l[i]<h1:
#         h2=l[i]
# print(h2)
'''17. Write a program to find the third largest number in a list.
18. Write a program to sort a list without using any built-in sorting functions.
19. Write a program to find the Nth largest element in a list.
20. Write a program to print the first four smallest missing elements from a list
Searching
21. Write a program to perform linear search on a list.
22. Write a program to perform binary search on a sorted list.
23. Write a program to return all index positions of a searched element in a list.
24. Write a program to check whether a list is sorted or not.
Math on arrays
25. Write a program to find the LCM of all numbers in the list.
26. Write a program to find the GCD of all numbers in the list.
27. Write a program to find the factorial of each element in a list
Frequency
28. Write a program to find the frequency of each element in a list.
29. Write a program to calculate the backward frequency of elements in a list.
30. Write a program to print frequencies of each element without repetition.
31. Write a program to find the most frequently repeated element in a list.'''