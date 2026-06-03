'''a=int(1)
print(a)
print(type(a))
a=str('a')
print(type(a))'''


'''a=input(' Enter your age')
a=float(a)
print('User age',a+5)
print(type(a))'''

'''a=10
a=float(a)
print(a)
print(type(a))'''

'''a=19.6
a=int(a)
print(a)
print(type(a))'''

'''a = str('23')
b = str('25')
a=int(a)
b=int(b)
print('Number is',a+b)'''

'''x= str('Vikas')
print(x[2:5])'''

# LIST TOPIC 

# Create list 
'''mylist = ['apple','Banana','mango','graps','kewi']
print(mylist)

# Access fiste and last element 
print(mylist[0])
print(mylist[-1])

#Add element 
mylist.append('mango')
print(mylist)

# Insert element 
mylist.insert(1, 'Orange')
print(mylist)

#Remove Element 
mylist.remove('mango')
print(mylist)

#length of list
print(len(mylist))

#loop through list 
for i in mylist:
    print(i)
    print('apple' in mylist)'''

# Create tupple 
num=(2,4,6,8,2,2,2,2)
print(num)

# print type of tupple 
print(type(num))

# access 3rd element 
print(num[3])

# find lenghth 
print(len(num))

'''# Loop Through Tuple
for i in num:
    print(i)
 # Count Occurrence
    for i in num:
        if i == 2:
            print(i)'''
'''count=0
for i in num:
    if i == 2:
        count = count+1
print(count)'''
i = 0
count = 0
while i < len(num):
    if num[i] == 2:
        count=count+1
    i = i+1 
print(count)

