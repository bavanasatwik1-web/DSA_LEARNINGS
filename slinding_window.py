'''First-negative in a window of sixe K'''
# l=[-8, 2, 3, -6, 10] 
# k = 2
# result=[]
# for i in range(len(l)-k+1):
#     sub=l[i:i+k]
#     for i in sub:
#         if i<0:
#             result.append(i)
#             break
#     else:
#         result.append(0)
# print(result)            

'''max-sum of distinct subarray of k'''


n=[1,5,4,2,9,9,9]
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
k = 3
max=0
for i in range(len(n)-k+1):
    s=n[i:i+k]
    ss=set(s)
    if len(ss)==k:
        sum1=sum(s)
        if sum1>max:
            max=sum1
print(max)            
