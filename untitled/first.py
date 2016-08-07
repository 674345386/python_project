def calc(numbers):
    sum1=0
    for x in numbers:
        sum1 =sum1+x*x
    return  sum1
x=[1,2,3]
print(calc([1,2,3,4]))
print(calc(x))

def calc2(*numbers):
    sum1=0
    for x in numbers:
        sum1 =sum1+x*x
    return  sum1
y=[2,2,3]

print(calc2(1,2,3))
print(calc2(1,2,3,4))
print(calc2(*y))
print(calc2())


def person(name,age,**kw):
    print('name: ',name,'age: ',age,'other: ',kw)

person('Bob',23)
person('Bob',23,city='chengdu')
person('Bob',23,city='chengdu',marry='no')

z={'city':'chengdu','marry':'no'}
person('Bob',23,**z)