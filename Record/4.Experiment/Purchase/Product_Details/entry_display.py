products=[]
def add_product():
  products.append({"name":input("Enter product name:"),"price":float(input("Enter product price:")),"quantity":int(input("Enter product quantity:"))})
  print("Product added successfully")
def display_products():
  if len(products)==0:
    print("No product available.")
    return
  i=0
  print("S.No\tName\tPrice\tQuantity")
  for product in products:
    print(f"{i+1}.",product['name'],product['price'],product['quantity'],sep='\t')
    i+=1
