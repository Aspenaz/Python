# Example:

def xxx():
        a=10
        b=15
        c=20

def yyy():
        xxx()
        print(a)        ### value a from xxx()
        print(b)       ### value b from xxx()

yyy()




# ===========================================================
# Answers 1:

def xxx():
    a=10
    b=15
    c=20
    return a, b

def yyy():
    a, b = xxx()
    print(a)        ### value a from xxx()
    print(b)        ### value b from xxx()

yyy()
# 10
# 15



# ===========================================================
# Answers 2:

def xxx():
    global a, b
    a=10
    b=15
    c=20

def yyy():
    print (a)
    print (b)

xxx()
yyy()
# 10
# 15


# ===========================================================
# Answers 3:
""" 
global a=0
global b=0
global c=0

def xxx():
    a=10
    b=15
    c=20
    return a,b

def yyy():
    print (a)
    print (b)
    xxx()

 """
# ===========================================================
# Answers 4:

class MyClass(object):
    x = [1, 2, 3]
    def xxx(self):
        self.a = 100
        self.b = 150
        self.c = 200

    def yyy(self):
        self.xxx()
        self.d = 300
        print (self.a)
        print (self.b)


obj = MyClass()  #Create an instance of the class
obj.yyy()
# 100
# 150
print()
print(obj.c)  # 200
print(obj.d)  # 300
# print(obj.xxx.get.x)  # Extract innner scope variable!!!!!!!! How is it? 
# print(MyClass.c)



# ===========================================================
# ===========================================================


def a(): 
	a.i="variable1"  # function attribute  
	 
def b(): 
	a()         # call the function  
	print(a.i)  # acess the variable  
	 
b()  # variable1

# ===========================================================

def a(): 
	global i 
	i="variable2"  # global variable  
	 
def b(): 
	a()  # since we are declaring i as global in a() we need to call a() 
	print(i) 
	 
b()  # variable2



