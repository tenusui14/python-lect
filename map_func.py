# list_1 = [ x for x in range(1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = " 15 156 96 3 5 8 52 5"
# print(data)

# data = list(map(int, data.split()))
# print(data)


def where(f, col):
    return [ x for x in col if f(x)]

lst = [1,2,3,5,8,15,38]
res = map(int, lst)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x*x), res))
print(res)