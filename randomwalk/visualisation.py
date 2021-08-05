import matplotlib.pyplot as plt 
from randomm import RandomWalk

rndm = RandomWalk()
rndm.walkk()

plt.style.use('seaborn-pastel')
fig, ax = plt.subplots()
ax.scatter(rndm.xs, rndm.ys, s=15)
plt.show()
