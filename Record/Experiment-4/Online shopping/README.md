# Shopping Cart & Billing System – Python

A modular, menu-driven Python application that simulates a basic retail shopping cart experience through a command-line interface (CLI). It supports product management (add, display, update, delete), real-time cart handling, and final billing with GST and discount calculations.

---

##  Features

-  **Product Management**: Add, display, update, and delete products
-  **Cart Functionality**: Add products to a cart with quantity validation
-  **Billing System**:
  - Automatic 18% GST calculation
  - 10% discount on purchases above ₹1000
-  **Menu-Driven CLI Interface**: Intuitive user prompts and inputs
-  **Modular Code Structure**: Organized using multiple Python files for clarity and reuse

---

##  Project Structure<br>
Online shopping/<br>
├── Product_Details/<br>
│ ├── entry_display.py # Add and display products<br>
│ └── update_delete.py # Update and delete products<br>
├── Purchase_Billing/<br>
│ └── billing.py # Purchase and billing functionality<br>
└── main.py # Main driver with menu<br>


---

##  Concepts Used

- Python functions and modular programming
- Lists and dictionaries for data handling
- Loops, conditionals, and user input
- Simple business logic: GST, discounts
- Console I/O formatting

---

##  Sample Output

1.Add Product <br>
2.Display Products <br>
3.Update Product<br>
4.Delete Product<br>
5.Purchase<br>
6.Exit<br>
Enter your choice: 1<br>
Enter product name: Pen<br>
Enter product price: 10<br>
Enter product quantity: 5<br>
Product added successfully<br>

You got 10% ₹120 Discount.<br>
Your cart products are:<br>
S.No Name Price Quantity<br>

Pen 10.0 5<br>
Sub total :1200.00<br>
Tax amount :194.40<br>
Final amount:1274.40<br>


---

##  Requirements

- Python 3.x
- Runs entirely in the terminal/command line (no external libraries)

---

##  How to Run

1. Clone the repository or download the files:
   ```bash
   git clone https://github.com/Dharamveer-A/Python-Assignments.git

