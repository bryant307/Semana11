import matplotlib.pyplot as plt



peliculas = ['Eternal', 'LOKI', 'WandaVision', 'SpiderMan', 'BlackWidow', 'Captain Marvel', 'Avenger']
puntuacion = ['6', '5', '7', '8', '5', '8', '9']

plt.plot(peliculas, puntuacion)
plt.title('PELICULAS DC VS MARVEL')
plt.xlabel('Peliculas')
plt.ylabel('Puntuacion')


plt.show()