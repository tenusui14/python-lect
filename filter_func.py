# data = [15,65,9,36,175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

#/////////////////////////////////////////////////////////
def select(f, col):
    return [f(x) for x in col]
lst = [1,2,3,5,8,15,38]
res = select(int, lst)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x*x), res)
print(res)