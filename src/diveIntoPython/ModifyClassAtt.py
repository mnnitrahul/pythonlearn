__author__ = 'rahul.ka'
class counter:
    count = 0
    def __init__(self):
        self.__class__.count += 1

print counter
print counter.count
c = counter()
print c.count
print counter.count