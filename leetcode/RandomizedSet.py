# import random as rd
import random as rd

class RandomizedSet:
    def __init__(self):
        self.set1 = set()
        self.ans = []

    def insert(self, val: int) -> bool:
        if val in self.set1:
            self.ans.append(False)
        else:
            self.set1.add(val)
            self.ans.append(True)

    def remove(self, val: int) -> bool:
        if val in self.set1:
            self.set1.remove(val)
            self.ans.append(True)
        else:
            self.ans.append(False)

    def getRandom(self) -> int:
        self.ans.append(rd.choice(list(self.set1)))


if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))
    print(rs.remove(2))
    print(rs.insert(2))
    print(rs.getRandom())
    print(rs.remove(1))
    print(rs.insert(2))
    print(rs.getRandom())

