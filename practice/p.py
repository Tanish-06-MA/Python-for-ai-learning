name = input()
print(f"hello {name}")

"""Celsius to farenheit"""


def convert(cel):
    f=(cel*9/5)+32
    
    return f

celsius=int(input())
print(convert(celsius))

#finding larget between 3

nums = [3,1,2]
largest = nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        largest=nums[i]
    
print(largest)
    
    
# even numbers from 1 to 100

for i in range(1,100):
    if i%2==0:
        print(i)
        

# table

n=int(input())

for i in range(1,11):
     print(n ,"*", i ,"=", n*i)
     

#string reverse
name = "marco"
rev=[]

for i in reversed(name):
    rev.append(i);

print("".join(rev))