tp = (1, 2, 3)
print(type(tp))



def calc(a, b):
    return a+b, a*b


result = calc(3, 4)
print(result)

args = (5, 6)
print(calc(*args))

print("----------------------")