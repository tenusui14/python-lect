# lst = [1,2,3,5,8,15,38]

# def calc(x):
#     new_lst = []
#     for i in x:
#         if i % 2 == 0:
#             new_lst.append((i, i*i))
#     return new_lst
        
# print(calc(lst))
# /////////////////////////////////////////////////////
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [ x for x in col if f(x)]

lst = [1,2,3,5,8,15,38]
res = select(int, lst)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x*x), res)
print(res)