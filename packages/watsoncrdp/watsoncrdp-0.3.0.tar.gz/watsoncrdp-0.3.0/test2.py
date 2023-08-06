import random

from watsoncrdp import rdp as wrdp

meas = [random.random() for i in range(100)]

res, o, d = wrdp(list(zip(range(100), meas)), epsilon=0.1, min_points=1000,)
print(res)
