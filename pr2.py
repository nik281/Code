import random as r
r.seed(100)
l1 = [r.randint(1,100) for _ in range(10)]
l2 = [r.randint(1,100) for _ in range(10)]
d = {i:l1.count(i)+l2.count(i) for i in set(l1) if i in set(l2)}
print(d)