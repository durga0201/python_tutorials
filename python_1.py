# variables 
#------------
#list
values = [9.5,'anurag',34]    #list is muatable
values.append(45)
print(values)

# break
av = 5
x =20
i = 1 
while i <=x :
    if i > av:
        break  #--> jump out of while loop
    print("candy")
    i+=1

# continue
for i in range(1,100):
    if i%3==0:
        continue    #-->skip the loop
    print(i)

# pass
for i in range(1,10):
    if (i%2 !=0):
        pass           # does nothing
    else:
        print(i)

# for else loop
nums = [12,16,18,20,25]
for num in nums:
    if num % 5 ==0:
        print(num)
        break
else:
    print("not found")

# arrays 
import array as arr

vals = arr.array('i',[3,41,3,5,3]) #'B' -->unsinged integer
vals.buffer_info   #information about array

#dynamic array
ar = array('i',[])
n = int(input('enter length of array'))
for i in range(n):
    x = int(input("enter the value"))
    ar.append(x)

#print index number 
val =12
ar.index(val)

#multi dimension array (from numpy()
import numpy as np

multi_dimensional_array = np.array([1,2,3,4,5,6])
lin  = np.linspace(0,16,10)
aran = np.arange(1,24,2)
log  = np.logspace(1,40,5)     #five step part in log space 
one  = np.ones(5)
zero = np.zeros(3)