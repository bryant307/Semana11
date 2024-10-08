import matplotlib.pyplot as plt



peliculas = ['Eternal', 'LOKI', 'WandaVision', 'SpiderMan', 'BlackWidow', 'Captain Marvel', 'Avenger']
duracion = ['120', '110', '90', '90', '80', '125', '120']

plt.pie(duracion, labels=peliculas)
plt.title('PELICULAS DC VS MARVEL')
plt.xlabel('Peliculas')
plt.ylabel('Puntuacion')


plt.show()