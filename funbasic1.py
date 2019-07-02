#1
def a():
    return 5
print(a())
# output prediction 5

#2
def b():
    return 5
print(b()+b())
# output prediction 10

#3
def c():
    return 5
    return 10
print(c())
# output prediction 5 , wont reach 10 because of the return statement

#4
def d():
    return 5
    print(10)
print(d())
# output prediction 5 , wont reach 10 because of the return statement

#5
def e():
    print(5)
x = e()
print(x)
# output prediction 5 , None

#6
def f(b,c):
    print(b+c)
print(f(1,2) + f(2,3))
#output prediction will print 3, 5 but nothing will be returned

#7
def g(b,c):
    return str(b)+str(c)
print(g(2,5))
#output prediction 25 because it treats the numbers as a string it merges them together to make a string

#8
def h():
    i = 100
    print(i)
    if i < 10:
        return 5
    else:
        return 10
    return 7
print(h())
# output 100,10

#9
def j(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(j(2,3))
print(j(5,3))
print(j(2,3) + j(5,3))
#output 7,14,21

#10
def o(b,c):
    return b+c
    return 10
print(o(3,5))
# output 8

#11
z = 500
print(z)
def k():
    z = 300
    print(z)
print(z)
k()
print(z)
#output 500,500,300,500

#12
y = 500
print(y)
def m():
    y = 300
    print(y)
    return y
print(y)
m()
print(y)
#output 500,500,300,500

#13
w = 500
print(w)
def r():
    w = 300
    print(w)
    return w
print(w)
w=r()
print(w)
#output 500,500,300,300

#14
def s():
    print(1)
    t()
    print(2)
def t():
    print(3)
s()
#output 1,3,2 

#15
def p():
    print(1)
    x = u()
    print(x)
    return 10
def u():
    print(3)
    return 5
v = p()
print(v)
#output 1,3,5,10