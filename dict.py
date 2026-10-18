
# students = {
#     "Ravi": 75,
#     "Kiran": 88,
#     "Priya": 92,
#     "Suresh": 68,
#     "Anil": 80
# }

# # 1. Print all student names and marks
# for name, marks in students.items():
#     print(name, ":", marks)

# # 2. Add a new student
# students["Satwik"] = 85

# # 3. Update Ravi's marks
# students["Ravi"] = 90

# print("\nAfter adding and updating:")

# for name, marks in students.items():
#     print(name, ":", marks)

# # 4. Find the highest scorer
# highest_student = max(students, key=students.get)

# print("\nHighest scorer:", highest_student)
# print("Highest marks:", students[highest_student])

# # 5. Calculate average marks
# average = sum(students.values()) / len(students)

# print("Average marks:", average)

# l=[9,6,3,12,4,5]
# z=3
# max=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         c=sum=0
#         p=[]
#         for k in range(i,j+1):
#             p.append(l[k])
#             sum+=l[k]
#         if len(p)==z:
#             if max>sum:
#                 max=sum
#         print(max)     

'''Anagram'''

def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        d={}    
        for i in range(0,len(s)):
            d[s[i]]=d.get(s[i],0)+1
            d[t[i]]=d.get(t[i],0)-1
