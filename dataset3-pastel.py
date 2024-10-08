import matplotlib.pyplot as plt

modelo = ['MackBook Pro - Apple', '250 G6 - HP', 'Aspire3 - Acer', 'Zenbook - ASUS','Ispiron 3567 - Dell', 'Ideapad - Lenovo']
ventas = [1339, 575, 400, 1158, 745, 2558]

plt.pie(ventas, labels=modelo)

plt.title('Precios de Laptops por modelo')
plt.xlabel('Modelo y Marca')
plt.ylabel('Unidades Vendidas')

plt.show()