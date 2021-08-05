import matplotlib.pyplot as plt  

plt.style.use('seaborn-darkgrid')

fig, ax = plt.subplots()

xs = [1, 2, 3, 4, 5]
ys = [x*x*x for x in xs]

ax.set_title('cubes, ex. 15. 1', fontsize = 18)
# x = 1 , x = 2 (...) , x = 5
# f(x) = x*x*x*
ax.set_xlabel('values', fontsize=10)

ax.set_ylabel('cubes: f(x) = x*x*x', fontsize = 10)

ax.tick_params(axis='both', labelsize = 14)

ax.plot(xs, ys, linewidth=2)

plt.show()