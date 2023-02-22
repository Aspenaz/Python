# Example:
""" 
def xxx():
        a=10
        b=15
        c=20

def yyy():
        xxx()
        print(a)        ### value a from xxx()
        print(b)       ### value b from xxx()

yyy()


 """
print()
# ===========================================================
# Answers 1:

def xxx():   # type: ignore
    a=10
    b=15
    c=20
    return a, b

def yyy():   # type: ignore
    a, b = xxx()
    print(a)        ### value a from xxx()
    print(b)        ### value b from xxx()

yyy()
# 10
# 15



print()
# ===========================================================

# Answers 2:

print('global 2\n') 
def xxx():   # type: ignore
    global a, b
    a=110   # type: ignore
    b=115   # type: ignore
    c=220

def yyy():   # type: ignore
    print (a)
    print (b)

xxx()
yyy()
# 10
# 15


print()
# ===========================================================

# Answers 3:

print('global 3\n')
global a, b, c
# global b
# global c 

a = 0   # type: ignore
b = 0   # type: ignore
c = 0

def xxx():
    a=101
    b=151
    c=202
    return a, b

def yyy():
    print ('a=', a)
    print ('b=', b)
    xxx()

print(yyy())
print('xxx=', xxx())
yyy()
 

 
print()
# ===========================================================

# Answers 4:

print('MyClass 1\n')
class MyClass(object):   # type: ignore
    x = [1, 2, 3]
    def xxx(self):
        self.a = 100
        self.b = 200
        self.c = 300

    def yyy(self):
        self.xxx()
        self.d = 400
        print (self.a)
        print (self.b)

obj = MyClass()  # Create an instance of the class
obj.yyy()

print()
print(obj.a) 
print(obj.b) 
print(obj.c)  # 200
print(obj.d)  # 300



print()
# ===========================================================


print('MyClass 2 \n')
class MyClass(object):
    x = [1, 2, 3]
    def xxx(self):
        self.a = 100
        self.b = 200
        self.c = 300

    def yyy(self):
        self.xxx()
        self.d = 400
        # print ('a =', self.a)
        # print ('b =', self.b)
        self.e = self.a
        self.f = self.b

obj = MyClass()  # Create an instance of the class
obj.yyy()  # 100  150

# obj.xxx()  # If not execute xxx() method don't start and initialize variables a, b, c. 
print('a=', obj.a)  # 200
print('b=', obj.b)  # 300
print('c=', obj.c)  # 200
print('d=', obj.d)  # 300  # AttributeError: 'MyClass' object has no attribute 'd'. # In this case if not execute yyy() method.
print('e=', obj.e)  # 200
print('f=', obj.f)  # 300
# print(obj.xxx.get.x)  # Extract innner scope variable!!!!!!!! How is it? 
# print(MyClass.c)



print()
# ===========================================================
#
# ===========================================================


def a():   # type: ignore 
	a.i="variable1"  # function attribute  
	 
def b():   # type: ignore 
	a()         # call the function  
	print(a.i)  # acess the variable  
	 
b()  # variable1



print()
# ===========================================================




def a(): 
	global i 
	i="variable2"  # global variable  
	 
def b(): 
	a()  # since we are declaring i as global in a() we need to call a() 
	print(i) 
	 
b()  # variable2




print()
# ===========================================================

