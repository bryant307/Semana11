import matplotlib.pyplot as plt

canciones = ['Seven, Latto ft Jung kook', 'LALA, Mike Towers', 'Cruel Summer, Taylor Swift', 'vampire, Olivia Rodriguez', 'WHERE SHE GOES, Bad Bunny']
streams = ['1413817', '1337162','8008408', '13255415', '1253695']

plt.bar(canciones, streams)

plt.title('TOP STREAMS EN SPOTIFY')
plt.xlabel('Categorias')
plt.ylabel('Streams')

plt.show()