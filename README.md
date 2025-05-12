# prueba_desempe-o_m1
# Inventory management system
![Mi imagen](control-inventario-erp-2.jpg)
##
This is a basic inventory management code in python,It allows the user to have basic management of their inventory, contains several functions and a main menu through which the different functions can be accessed. Such as adding, searching, updating, and deleting products, as well as an option to generate a report of the total inventory.
# Requirements:
Python 3.x installed in your system.
### How to run this code
Download or clone the repository.
Open a terminal and navigate into the project directory 
# Features: 
## Add products: 
Contains a function to add products with their name, quantity and price.
### Example Add products:
input:
```python
Choose an option (1-6): 1
Enter product name: agua
Enter the quantity of products: 100
Enter price: 1500
```
output:
```python
Product'agua'registered successfully. 
```
## Search products: 
Contains the option to search for products in the inventory, showing their basic information.
### Example search product:
input:
```python
Choose an option (1-6): 2
Enter product name to search: sal
```
output:
```python
Product found:
name: sal
Quantity available: 100
Price: $2550
```
## Update products:
You have the option to update information on already registered products, such as price or quantity.
### Example Update product:
input:
```python
Choose an option (1-6): 3
Enter product name to update: sal
What do you want to update? (price/quantity): quantity
Enter the new quantity: 200
```
output:
```python
Quantity updated successfully to 200.
```
## Delete products:
You can remove products that are no longer available. Request a last-minute confirmation if you wish to remove the product.
### Example Delete product:
input:
```python
Choose an option (1-6): 4
Enter product name to delete: bocadillo
Are you sure you want to delete 'bocadillo'? (yes/no): yes
```
output:
```python
Product 'bocadillo' deleted successfully.
```
## Generate inventory report:
You can generate inventory reports, calculating the quantity of each product by its unit price, thus showing the total inventory of all products.
### Example Generate report
input:
```python
Choose an option (1-6): 5
```
output:
```python
Total inventory value: $3997000.00
```
## Notes
### The inventory starts with 5 default products
### All inputs are validated to prevent negative or incorrect values.
### All comments are written in English as required.
