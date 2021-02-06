
#QUESTION 1:
my_list=[3,6,12,15,18,21]
list1=my_list[:3]
list2=my_list[3:]
new_list=list2+list1
print(new_list)

#QUESTION 2:
s = int(input('Please write a single digit integer:\n'))
evenNumers=[]
if s>=0:
    print("Even numbers :")
    for i in range(s+1):
        if i % 2 == 0:
            evenNumers.append(i)
    print(evenNumers)      
