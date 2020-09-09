class A(object):
    def method(self):
        print('A Class method')
        super().method()
class B(object):
    def method(self):
        print('B Class method')
        super().method()
class C(object):
    def method(self):
        print('C Class method')
class X(A,B):
    def method(self):
        print('X Class method')
        super().method()
class Y(B,C):
    def method(self):
        print('Y Class method')
        super().method()
class P(X,Y,C):
    def method(self):
        print('P Class method')
        super().method()
p=P()
p.method()
print(P.mro())