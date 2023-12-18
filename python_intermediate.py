
# lists
mylist = ["banana","cherry","apple"]

if "banana" in mylist:
    print("yes")

len(mylist)               #--> length of list
mylist.append("lemon")    #--> insertion at last
mylist.insert(1,"blueberry")   # insert at particular index, in this case at 1 index
mylist.pop()              # removes and returns last item
mylist.remove("cherry")  # if not throws "value error"
mylist.reverse()         # reverse the list
mylist.sort()            # sort the list  sorted(list) --> doesn't change the list
mylist.clear()    # --> empty list 

mylist = [0]*5    # [0,0,0,0,0]


list1 = [2,3,4,5,6] 
list2 = [1,3,4,6,7]

new_list = list1 + list2 

#slicing 
mylist = [1,2,3,4,5,6,7,8,9]
mylist[1:5] #[2,3,4,5]  
mylist[1::2]       # step index
mylist[::-1]       # reverse

# copy 

list_org = ["banana","cherry","apple"]

list_cpy = list_org.copy()  #list(list_org); list_org[:]

# list comprehension

a = [1,2,3,4,5,6,7]
b = [i*i for i in a]
 

 #-------------------------------------------
 # tuples: ordered, immutable, allows duplicate elements

 mytuple = ("max",24,"bangalore")

# access elemets

item = mytuple[0]   # index 

for i in mytuple:
   print(i)

mytuple = ("P","q","P","s","A","f")
len(mytuple)
mytuple.count('P')
mytuple.index("P")   # first occurance of element "P"

my_list = list(mytuple)
my_tuple = tuple(my_list)

#slicing
mytuple = (1,2,3,4,5,6,7,8,9)
mytuple[2:5]


 mytuple = ("max",24,"bangalore")
name,age,city = mytuple   #unpack tuple

mytuple = (1,2,3,4,5,6,7,8,9)
i1,*i2,i3 = mytuple 

#compare tuple and list

import sys
mylist = [1,2,3,4,5,6]
my_tuple = (1,2,3,4,5,6)

print((sys.getsizeof(mylist),"bytes"),sys.getsizeof(my_tuple),"bytes")


##-----------------------------------------------------------------------------
#Dictionary

mydict = {"name":"Max",
          "age":24,
          "city":"blr"}

mydict2 = dict(name="mama",age=45,city="rrke")

value = mydict["name"]

mydict["email"] = "anuragk8345@gmail.com"  #overwrite if keys exist

del mydict["name"]
mydict.pop("age")

if "name" in mydict:
  print(mydict["name"])

try:
  print(mydict["name"])
except:
  print("error")

for key in mydict:
  print(key)

for key in mydict.keys():
  print(key)

for key,valye in mydict.items():
  print(key,value)

mydict_cpy = mydict    #modifying copy will modify originak

mydict_cpy = mydict.copy() ; mydict_cpy = dict(mydict)
#---
mydict = {"name":"Max",
          "age":24,
          "city":"blr"}

mydict2 = dict(name="mama",age=45,email="rrke@com")
my_dict.update(mydict2)

my_tuple = (8,7)
mydict = {my_tuple:15}  #list is mutable and unhashable


##-------------------------------------------------------------------
##set 

myset = {1,2,3,4,2,2}   #does now allow duplicate and unordered

empty_set = set()
empty_set.add(1)
empty_set.add(2)
empty_set.add(4)

empty_set.remove(2)   #throws error if not find the methid
empty_set.discard(1)   # doesnt throw error 

empty_set.clear()

odds = {1,3,5,7,9}
even = {2,4,6,8,0}
primes = {2,3,5,7}

u = odds.union(even)
i = even.intersection(prime)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)

sym_diff = setA.symmetric_difference(setB)

setA.update(setB)

setA.intersection_update(setB)

setA.difference_update(setB)

set.symmetric_difference_update(setB)

setA.issubset(setB)
setA.issuperset(setB)
setA.isdisjoint(setB)

s = frozenset([1,2,3,4,5,6])  #immutable set

##-----------------------------------------------------
#collections
from collections import Counter

a = 'aaaaaaaabbbbxxxx'
mycounter = Counter(a)

mycounter.items()
mycounter.keys()
mycounter.values()

mycounter.most_common(1)

list(mycounter.elements())

from collections import namedtuple

Point = namedtuple('Point','x,y')   #create class called point with field x and y 
pt = Point(1,-5)
pt.x,pt.y

from collections import OrderedDict  #dictionary remebers order

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4


from collections import defaultdict   #has default type

d = defaultdict(int)

d['a']=1
d['b']=2

from collections import deque   #double ended queue

d= deque()

d.append(1)
d.append(2)

d.appendleft(3)
d.popleft()
d.clear()
d.extend([4,5,6])
d.extendleft([14,15,16])
d.rotate(2) # rotate all elements 2 place 


# -----------------------------------------------------------------------------------
# itertools

from itertools import product,permutations,combinations,accumulate,groupby ; 
import operator
a = [1,2]
b = [3]

prod = product(a,b,repeat=2)  #cartesian product

permut = permutations(a,2)
combination = combinations(a,3)

acc = accumulate(a)
mul = accumulate(a,func=operator.mul)

def smaller_than_3(x):
  return x<3
a =[1,2,3,4]

group = group_by(a,key=smaller_than_3)   #keys = lambda x: x['xyz']

for key,value in group:
  print(key,list(value))

from itertools import count,cycle,repeat   #---> looping till stop condition

##---------------------------------------------------------------------------------------------------------
## Lambda function

""" lambda arg : exps """

add10 = lambda x:x+10
mult = lambda x,y : x*y

points2D = [(1,2),(2,3),(14,12),(21,22)]
points2D_sorted = sorted(points2D,key = lambda x:x[1])   # sorted according to y index

#map(func,seq)

a = [1,2,3,4,5,6]
b = map(lambda x:x*2,a)


#filter(func,seq)
a = [1,2,3,4,5,6]
b = filter(lambda x:x%2==0,a)

#reduct(func,seq)
from functools import reduce
a = [1,2,3,4,5,6]
b = reduce(lambda x,y:x*y,a)

##---------------------------------------------------------------------------------------------------------
## errors & exception

x = -5
if x<0:
  raise Exception('x should be positive')    

assert (x>=0),"x is not positive"

try:
  a = 5/0
except Exception as e:
  print(e)

try:
  a=5/0
except ZeroDivisionError as e:
  print(e)
else: 
  print('everything is fine')
finally:
  print('cleaning up....')



class ValueTooHighError(Exception):   # define our own exception
    pass
  
##---------------------------------------------------------------------------------------------------------
## logging

import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datafmt='%m/%d/%Y %H:%M:%S')
logging.debug('this is debug msg')
logging.info('this is info msg')
logging.warning('this is warning msg')     #only warning. error. critical are printed
logging.error('this is error msg')
logging.critical('this is critical msg')

# create own internal logger
# helper.py
logger = logging.getLogger(__name__)
logger.propagate=False
logger.info("hello from module name = __name__")

#lock handler
import logging
logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#set level and format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is a error')

# different config method --> login.conf


####------------------------------------------------------------
#JSON

import json

class user:
  
  def __init__(self,name,age):
    self.name = name
    self.age = age

u = user('Anurag',23)

def encode_user(o):
  if isinstance(o,User):
    return {'name':o.name,'age':o.age,o.__class__.__name__:True}
  else:
    raise TypeError('no serialization')
  
userJson = json.dumps(u,default=encode_user)

####------------------------------------------------------------
# Decoraters 

@mydecorater
def dosomething():
  pass

import functools

def start_end_decorator(func):
   @functools.wraps(func)     
   def wrapper(*args,**kwargs):
      # do something
      result = func(*args,**kwargs)
      return result
      # do something
   return wrapper


def print_name(): 
  print('anurag')

print_name = start_end_decorator(print_name)

@start_end_decorator
def add10(x):
  return x+10

print(help(add10))
print(add10.__name__)


#decorater with arguements

@start_end_decorator
def print_name():
  print('anurag')


def repeat(num_times):
    def decorater_repeat(func):
            @functools.wraps(func)  
            def wrapper(*args,**kwargs):
                    for _ in range(num_times):
                        result = func(*args,**kwargs)
                    return result
            return wrapper
    return decorater_repeat


@repeat(num_times=3)
def greet(name):
   print(f'Hello {name}')

#nested decorator  --> tbd

#class decorator 

class CountCalls:
   def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self,*args,**kwargs):
        self.num_calls+=1
        print('executed')
        return self.func(*args,**kwargs)


#cc = CountCalls(None)
#cc()

@CountCalls
def say_hello():
   print('hello')


# time, debug, check , register functions, cache , update using decorators

####------------------------------------------------------------
# Generators


def mygenerator():
   yield 1
   yield 2
   yield 3 

g  = mygenerator()

value = next(g)  # return and pause 
sum(g)
sorted(g)  # return sorted list

#memory efficiency of generator 


def first(n):
        nums = []
        num = 0
        while num<n:
           nums.append(num)
           num+=1
        return nums

def first_gen(n):
        num = 0
        while num<n:
           yield num
           num+=1

mygen = (i for i in range(10) if i%2==0)



###---------------------------------------------------------------------------------------
# thread  & process
"""
process : an instance of a program
        uses multiple thread inside process

thread : an entity within a process that can be scheduled

-all threads withn a process share the same memory
- lightwight
-starting a thread is faster than process
- great for i/o bound tasks
"""

from multiprocessing import Process
import os

def square():
   for i range(100):
      i*i
   



process = []
num_processess = os.cpu_count()


#create processes
for i in range(num_processess):
   p = Process(target = square)
   process.append(p)


#start
for p in process:
   p.start()

#join

for p in process:
   p.join()

print('end main')


from threading import Thread

threads = []
num_threads = 10

#create thread
for i in range(num_threads):
   p = Thread(target = square)
   threads.append(p)


#start
for p in threads:
   p.start()

#join

for p in threads:
   p.join()

print('end main')


### threadssssssssss


from threading import   Thread,Lock
import time

database = 0    #global variable


def increase(lock):
   global database 

   lock.acquire()                   #with lock:  -->context manager
   local_copy = database

   #processing
   local_copy+= 1 
   time.sleep(0.1)
   database_value = local_copy
   lock.release()


if __name__ == '__main__':
        lock =Lock()
        print('start value', database)


        thread1 = Thread(target=increase,args = (lock,))
        thread2 = Thread(target=increase)      #race condition, tw/more threads chaning same varibale at same time

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        print('end value',database)

        print('end main')



## que -> thread safe for data exchanges 

import threading import Thread,Lock,current_thread 
from queue import Queue          #follows fifo , type of data structure

def worker(q,lock):
   while True:
      value = q.get()

      # processing..
      with lock:
         print(f'in {curent_thread()} got {value}')
      q.task_done()
      print(value)


if __name__ = "__main__":
    q=Queue()
    lock = Lock()

    q.put(1)
    q.put(2)
    q.put(3)
#    3 2 1 --->
    first = q.get()
    #some process
    q.task_done()   # tells we are done with q process
    q.join # block the main thread till all elements are processed
    #   q.empty()

    num_threads = 10

    for i in range(num_threads):
       thread = Thread(target=worker,args=(q,lock))
       thread.daemon = True    #background thread when the main thread dies, 
       thread.start()
    
    
    for i in range(1,20):
            q.put(i)

    q.join()

    print('end main')


# multiprocessing detail 

from multiprocessing import Process,Value, Array,Lock
import os 


def add100(number,lock):
   time.sleep(0.01)
   with lock:
      number.value + 100
   
def process2():
   pass


if __name__=="__main__":
   shared_number  = Value('i',0)    #(data type , value)
   shared_array = Array('d',[0.0,100.0,200.0])
   print('number at begin',shared_number.value)
   print('number at begin',shared_array[:])

   
   lock = Lock()
   p1 = Process(target=add100,args=(shared_number,lock))
   p2 = Process(target = add100,args= (shared_number,))

   p1.start()
   p2.start()

   p1.join()
   p2.join()
   print('arrat at end',shared_array[:])

#pool and queue in multiprocessing --> tbd


###--------------------------------------------------------------------------------------------------------------------------------

def foo(a,b,*args,**kwargs) :  # args --> normal arguements, kwargs --> key word arguements
   print(a,b)
   for arg in args:
      print(arg)
    for key in kwargs:
      print(key,kwargs[key])

# forced keyword arguements
def foo(a,b,*,c,d):
   print(a,b,c,d)

foo(1,2,c=3,d=4)

def foo(**args,c,d):
   for arg in args:
      print(arg)
    print(c,d)
   
## unpacking arguements
def foo(a,b,c):
   print(a,b,c)

mylist = [1,2,3]
foo(*mylist)

mydict = {'a':1,'b':2,'c':3}
foo(**mydict)










