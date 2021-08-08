import matplotlib.pyplot as plt 
from randomm import RandomWalk

while True:
    rndm = RandomWalk()
    rndm.walkk()

    plt.style.use('seaborn-pastel')
    fig, ax = plt.subplots()
    point_numbers = range(rndm.numberOfPoints)
    ax.scatter(rndm.xs, rndm.ys, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none',s=15)
    ax.scatter(0, 0, c='green', edgecolors='none', s=60)
    ax.scatter(rndm.xs[-1], rndm.ys[-1], c='red', edgecolors='none', s=60)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    

    keep_running = input("Do you want to create new random walk? If yes write 'Y', if no write 'N': ")
    if keep_running == 'N':
        break
