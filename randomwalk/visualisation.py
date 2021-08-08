import matplotlib.pyplot as plt 
from randomm import RandomWalk

while True:
    rndm = RandomWalk(5000)
    rndm.walkk()

    plt.style.use('seaborn-pastel')
    fig, ax = plt.subplots(figsize=(15,9))
    ax.set_title('flower pollen path on the water')
    point_numbers = range(rndm.numberOfPoints)
    ax.plot(rndm.xs, rndm.ys, linewidth=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rndm.xs[-1], rndm.ys[-1], c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    

    keep_running = input("Do you want to create new random walk? If yes write 'Y', if no write 'N': ")
    if keep_running == 'N':
        break
