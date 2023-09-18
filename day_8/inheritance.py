# Example 1 :- Single inheritance

class A:
    def m1(self):
        print("m1 method from class A")


class B(A):
    def m2(self):
        print("m2 method from class B")


bobj = B()                      # B class obj
bobj.m1()
bobj.m2()

# Example 2 :- single inheritance

class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 100, 200

    def m2(self):
        print(self.a - self.b)


bobj = B()
bobj.m1()
bobj.m2()

# Example 3:- multilevel inheritance

class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 300, 200

    def m2(self):
        print(self.a - self.b)


class C(B):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)


cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()

# Example 4 :- Hierarchy inheritance

class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 300, 200

    def m2(self):
        print(self.a - self.b)


class C(A):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)


bobj = B()
bobj.m2()
bobj.m1()

cobj = C()
cobj.m3()
cobj.m1()

# Example 6 :- multiple inheritance

class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B():
    a, b = 300, 200

    def m2(self):
        print(self.a - self.b)


class C(A, B):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)


cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()

#  Example 7:- calling parent class method using child class ( super() )

class A:
    def m1(self):
        print("this is m1 method from class A")


class B(A):
    def m1(self):
        print("this is m2 method from class B")
        super().m1()            # invoke the parent class method throw  the child class method


bobj = B()
bobj.m1()


# Example 8 :-

class A:
    a,b = 10,20


class B(A):
    i, j = 100, 200

    def m(self, x, y):
        print(x + y)
        print(self.i, self.j)
        print(self.a, self.b)


bobj = B()
bobj.m(1000, 2000)

# Example 9:- overriding variable

class parent:
    name = "scott"

class child(parent):
    name = "john"       # overiding the variable value


cobj = child()
print(cobj.name)            # child class variable gives the latest value

# Example 10 :- overriding the methods

class bank:
    def roi(self):
        return 0

class xbank(bank):
    def roi(self):
        return 10

class ybank(bank):
    def roi(self):
        return 12


objx = xbank()
print(objx.roi())

objy = ybank()
print(objy.roi())

# Example 11 :- overloading (polymorphism)

class human:
    def sayhello(self, name=None ):
        if name is not None:
            print("hello" + name)
        else:
            print("hello")


h = human()
h.sayhello("scott")
h.sayhello()

# Example 12:- overloading 2

class cal:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)


calobj = cal()
calobj.add()
calobj.add(10,20)
calobj.add(10,20,30)
