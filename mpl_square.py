import matplotlib.pyplot as plt 

plt.style.use('fivethirtyeight')# wybranie stylu

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # lista
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# tytuł wiersza
ax.set_title('Kwadraty liczb', fontsize=28)
# tytuły osi x i y
ax.set_xlabel('Wartość', fontsize=14)
ax.set_ylabel('Kwadraty wartości', fontsize=14)
#wielkość etykiet
ax.tick_params(axis='both', labelsize=14)


plt.show() # funkcja wywoławcza