# 🛒 Shopping Cart & Billing System – Python

A modular, menu-driven Python application that simulates a basic retail shopping cart experience through a command-line interface (CLI). It supports product management (add, display, update, delete), real-time cart handling, and final billing with GST and discount calculations.

---

## 🚀 Features

- 📦 **Product Management**: Add, display, update, and delete products
- 🛍️ **Cart Functionality**: Add products to a cart with quantity validation
- 💰 **Billing System**:
  - Automatic 18% GST calculation
  - 10% discount on purchases above ₹1000
- 📋 **Menu-Driven CLI Interface**: Intuitive user prompts and inputs
- 🧩 **Modular Code Structure**: Organized using multiple Python files for clarity and reuse

---

## 📁 Project Structure
Online shopping/
├── Product_Details/
│ ├── entry_display.py # Add and display products
│ └── update_delete.py # Update and delete products
├── Purchase_Billing/
│ └── billing.py # Purchase and billing functionality
└── main.py # Main driver with menu


---

## 🧠 Concepts Used

- Python functions and modular programming
- Lists and dictionaries for data handling
- Loops, conditionals, and user input
- Simple business logic: GST, discounts
- Console I/O formatting

---

## 📷 Sample Output

1.Add Product
2.Display Products
3.Update Product
4.Delete Product
5.Purchase
6.Exit
Enter your choice: 1
Enter product name: Pen
Enter product price: 10
Enter product quantity: 5
Product added successfully

You got 10% ₹120 Discount.
Your cart products are:
S.No Name Price Quantity

Pen 10.0 5
Sub total :1200.00
Tax amount :194.40
Final amount:1274.40


---

## ✅ Requirements

- Python 3.x
- Runs entirely in the terminal/command line (no external libraries)

---

## 📌 How to Run

1. Clone the repository or download the files:
   ```bash
   git clone https://github.com/Dharamveer-A/Python-Assignments.git

