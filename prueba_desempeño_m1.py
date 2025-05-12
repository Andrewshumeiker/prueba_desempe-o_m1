#dictionary with 5 default products
products = [
    {"name":"sal","quantity":"100","price":"2550"},
    {"name":"bocadillo","quantity":"200","price":"4990"},
    {"name":"galletas","quantity":"150","price":"6250"},
    {"name":"desodorante","quantity":"50","price":"4490"},
    {"name":"electrolit","quantity":"250","price":"8700"},
]
def register(): #function to register products
  print ("\n---Register a new product---")
  name = input("Enter product name ").strip()
  try: #If an invalid value is entered, it will display an error.
     quantity = int(input("Enter the quantity of products "))
     if quantity < 0: #tests whether the quantity is a positive integer
        print("Invalid quantity. Please enter a valid quantity")
        return
  except ValueError:
     print("Invalid input. quantity must be a number. ")
  try: #If an invalid value is entered, it will display an error.
     price = float(input("Enter price: "))
     if price <= 0:  #validates that the entered value is a positive decimal
        print("Invalid price. Price must be a positive number")
        return
  except ValueError:
     print("Invalid input. price must be a number. ")
  for product in products: #Validates if the entered name already appears in the inventory, in which case it will display a message
      if product['name'].lower() == name.lower():
          print(" product already exist in the inventory. ")
          return
  new_product = { #add the product to the dictionary
      "name": name,
      "quantity": quantity,
      "price": round(price,2)
  }    
  products.append(new_product) #shows that the product has already been registered
  print(f"\nProduct'{name}'registered successfully. ")
  main()
def search(): #function to search for a product
   print("\n---Search Product---")
   ask = input("Enter product name to search: ").strip().lower()
   found = False
   for product in products: #Request the product name, if the name appears in the dictionary keys, it will display the product information
      if ask in product['name'].lower():
         print(f"\nProduct found: \n"
               f"name: {product['name']}\n"
               f"Quantity available: {product['quantity']}\n"
               f"Price: ${product['price']}\n")
         found = True
   if not found: #If the product does not exist, ask if the user wants to register it.
      print("product not found. Do you want to register it? (yes/No)")
      answer = input().strip().lower()
      if answer == "yes":
         register()
      elif answer == "no":
         main()
   main()
def update(): #the same search function for a product, and then gives the option to update the product price
    name = input("Enter the product name to update: ")
    for product in products:
        if product['name'].lower() == name.lower():
            field = input("What do you want to update? (price/quantity): ").lower()#Validate what information you want to update, price or quantity
            if field == 'price':
                try:
                    new_price = float(input("Enter the new price: "))
                    if new_price <= 0:
                        print("Price must be a positive number.")
                        return
                    product['price'] = new_price
                    print(f"Price updated successfully to {new_price}.")
                except ValueError:
                    print("Invalid price.")
                return
            elif field == 'quantity':
                try:
                    new_quantity = int(input("Enter the new quantity: "))
                    if new_quantity < 0:
                        print("Quantity must be zero or a positive number.")
                        return
                    product['quantity'] = new_quantity
                    print(f"Quantity updated successfully to {new_quantity}.")
                except ValueError:
                    print("Invalid quantity.")
                return
            else:
                print("Invalid option. Choose 'price' or 'quantity'.")
                return
    print(f"Product '{name}' not found in inventory.")      
def delete(): #function to delete products
   name = input("Enter the product name to delete: ")
   for product in products:
        if product['name'].lower() == name.lower(): #look up if the product is in the dictionary
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").lower() #asks if he wants to delete the product
            if confirm == 'yes':
                products.remove(product)
                print(f"Product '{name}' deleted successfully.")
            else:
                print("Deletion cancelled.")
            return
   print(f"Product '{name}' not found in inventory.")
def generate(): #function to generate the inventory report
   total = 0
   for product in products:
        total += float(product['price']) * int(product['quantity'])
   print(f"Total inventory value: ${total:.2f}")
def main():
    # Main menu function
    while True:
        print("\n---Options Menu---")
        print("1. Register new products")
        print("2. Search product")
        print("3. Update information")
        print("4. Delete product")
        print("5. Generate inventory report")
        print("6. Exit")

        option = input("Choose an option (1-6): ")
        #calls the others functions
        if option == "1":
            register()
        elif option == "2":
            search()
        elif option == "3":
            update()
        elif option == "4":
            delete()
        elif option == "5":
            generate()
        elif option == "6":
            print("See you later!")
            break
        else:
            print("Invalid option. Try again.")

main()