import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4,9, 16, 25]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)

# tytuł wiersza
ax.set_title('Kwadraty liczb', fontsize=28)
# tytuły osi x i y
ax.set_xlabel('Wartość', fontsize=14)
ax.set_ylabel('Kwadraty wartości', fontsize=14)
#wielkość etykiet
ax.tick_params(axis='both', labelsize=8)


plt.show()