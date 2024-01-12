list1=[1,2,3,4,5,6]
print(list1)

range1=range(1,8)
print(range1)

for i in range1:
    print(i)














#Example 1
def my_gen():
    yield 5
    yield 10
    yield 4

x=my_gen()
for i in x:
    print(i)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))  
  
#Example 2

def my_gen2():
    for i in range(5):
        yield i
a=my_gen2()
print(next(a))
print(next(a))
print("stop")
for i in a:   #Using an iterator to generate values
    print(i)
