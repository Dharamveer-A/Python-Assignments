from Product_Details.entry_display import products, display_products
def update_product():
  display_products()
  prod_name=input("Enter the product Name:")
  i=0
  for product in products:
    if product['name'].lower() == prod_name.lower():
      products[i]['name']=input("Enter new name:")
      products[i]['price']=float(input("Enter new Price:"))
      products[i]['quantity']=int(input("Enter new Quantity:"))
      print("Product updated.")
      break
    i+=1
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

