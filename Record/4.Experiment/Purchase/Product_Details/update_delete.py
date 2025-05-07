from Product_Details.entry_display import products, display_products
def update_product():
  display_products()
  prod_name=input("Enter the product Name:")

  for product in products:
    if product['name'].lower() == prod_name.lower():
      products['name']=input("Enter new Name:") or product['name']
      products['price']=float(input("Enter new Price:")) or product['price']
      products['quantity']=int(input("Enter new Quantity:")) or product['quantity']
      print("Product updated.")
      break

  else:
    print("Product not found.")
def delete_product():
  display_products()
  prod_name=input("Enter the product Name:")

  for product in products:
    if product['name'].lower() == prod_name.lower():
      products.remove(product)
      print("Product deleted.")
      break

  else:
    print("Product not found.")

