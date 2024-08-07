class save:
    def __init__(self,name="codetree",code=88):
        self.name = name
        self.code = code
info = tuple(input().split())
pr1 = save()
print(f"product {pr1.code} is {pr1.name}")
pr2 = save(info[0], int(info[1]))
print(f"product {pr2.code} is {pr2.name}")