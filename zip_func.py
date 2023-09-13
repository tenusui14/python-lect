# применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных
# например: zip([1,2,3], ["o","d","t"], ["е","с","т"]) == [(1,"o","e"), (2, "d","c"), (3,"t","e")]

# users = ["user1", "user2", "user3", "user4"]
# ids = [4,5,9,14]
# data = list(zip(users,ids))
# print(data)            # ----------------> [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14)]

#функция пробегает по меньшему входящему набору
users = ["user1", "user2", "user3", "user4"]
ids = [4,5,9,14]
salary = (111,222)
data = list(zip(users,ids,salary))
print(data)                # -----------------> [('user1', 4, 111), ('user2', 5, 222)]