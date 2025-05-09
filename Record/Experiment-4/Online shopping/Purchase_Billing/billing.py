from Product_Details.entry_display import products, display_products

def adding_product():
  cart=[]
  amount=0
  tax=0.18
  discount=0
  display_products()
  while True:
    prod_name=input("Enter product Name(0 for billing):")
    if prod_name=='0':
      break
    for product in products:
      if product['name'].lower() == prod_name.lower():
        quantity=int(input("Enter the quantity:"))
        if quantity<=product['quantity']:
          cart.append({'name':product['name'],'price':product['price'],'quantity':quantity})
          amount+=quantity*product['price']
          product['quantity']-=quantity

          break
        else:
          print(f"Only {product['quantity']} of {product['name']} available")
          break
    else:
      print("Product not found.")    
  '''Billing the added products'''
  if len(cart)==0:
    print("No product added")
    return
  print("\n_____Billing_____\n")
  if amount>1000:
    discount=0.1*amount
    print(f"You got 10% ₹{discount} Dicsount.")
  discount_amount=amount-discount
  tax_amount=tax*discount_amount
  final=discount_amount+tax_amount
  print("Your cart products are:")
  i=1
  print("S.No\tName\tPrice\tQuantity")
  for product in cart:
    print(f"{i}.\t{product['name']}\t{product['price']}\t{product['quantity']}")
    i+=1
  print("Sub total\t:%.2f"%amount)
  print("Tax amount\t:%.2f"%tax_amount)
  print("Final amount\t:%.2f"%final)
