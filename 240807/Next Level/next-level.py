class save:
    def __init__ (self,ID = "codetree", Level = "10"):
        self.ID = ID
        self.Level = Level
Pl1 = save()
print(f"user {Pl1.ID} lv {Pl1.Level}")
level, data = tuple(input().split())
Pl2 = save(level, data)
print(f"user {Pl2.ID} lv {Pl2.Level}")