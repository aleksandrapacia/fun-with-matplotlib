import matplotlib.pyplot as plt

x_values = range(1, 201)
y_values = [x**2 for x in x_values]
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values,c=(0, 0.5, 0), s=10)

# tytuł wiersza
ax.set_title('Kwadraty liczb', fontsize=28)
# tytuły osi x i y
ax.set_xlabel('Wartość', fontsize=14)
ax.set_ylabel('Kwadraty wartości', fontsize=14)
#wielkość etykiet
ax.tick_params(axis='both', labelsize=8)

ax.axis([0, 200, 0, 40000])


plt.show()