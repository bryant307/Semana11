import matplotlib.pyplot as plt

modelo = ['MackBook Pro - Apple', '250 G6 - HP', 'Aspire3 - Acer', 'Zenbook - ASUS','Ispiron 3567 - Dell', 'Ideapad - Lenovo']
precio = [1339.69, 575.00, 400.00, 1158.70, 745.00, 2558.00]

plt.bar(modelo, precio)

plt.title('Precios de Laptops por modelo')
plt.xlabel('Modelo y Marca')
plt.ylabel('Precio')

plt.show()