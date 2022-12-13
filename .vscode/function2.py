# function2.py

# def setValue(newValue):
#     x = newValue
#     print(x)

# retValue = setValue(5)
# print(retValue)



g = 1
print("--------------- 1")
print(id(g))
print(g)

def testScope(a):
    global g
    g = 2
    print("--------------- 2")
    print(id(g))
    print(g)

testScope(5)
print("--------------- 3")
print(id(g))
print(g)