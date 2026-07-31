
"""
Topic: Python Dictionaries & Parallel Lists
Difficulty: Beginner to Intermediate

Challenge Description:
You are given a dictionary containing store inventory details. 
The lists inside the dictionary align by index position.
"""


inventory = {
    "item_id": [101, 102, 103],
    "product_name": ["Wireless Mouse", "Mechanical Keyboard", "Gaming Headset"],
    "stock_details": [{"stock": 15, "price": 25.0}, {"stock": 8, "price": 75.0}, {"stock": 20, "price": 50.0}],
    "is_available": [True, True, True]
}

# ==============================================================================
# 🎯 TASKS TO IMPLEMENT:
# ==============================================================================

# Task 1: Print the product name of the item at index position 2.
# Expected Output: Gaming Headset
print("\n--- Task 1 ---")
# Your code here:
print(inventory["product_name"][2])  # Output: Gaming Headset


# Task 2: Find the index position of "Mechanical Keyboard" using the .index() method.
# Then, use that index to print its entire 'stock_details' dictionary.
# Expected Output: {'stock': 8, 'price': 75.0}
print("\n--- Task 2 ---")
# Your code here:
ind = inventory["product_name"].index("Mechanical Keyboard")
print(inventory["stock_details"][ind])  # Output: {'stock': 8, 'price': 75.0}

# Task 3: Insert a new product name "USB-C Cable" into the "product_name" list 
# at index position 1. Print the updated product name list.
# Expected Output: ['Wireless Mouse', 'USB-C Cable', 'Mechanical Keyboard', 'Gaming Headset']
print("\n--- Task 3 ---")
# Your code here:
inventory['product_name'].insert(1, "USB-C Cable")
print(inventory['product_name'])  # Output: ['Wireless Mouse', 'USB-C Cable', 'Mechanical Keyboard', 'Gaming Headset']

# Task 4: Add a new key-value pair to the main 'inventory' dictionary called "store_location".
# Set its value to a tuple containing: ("New York", "Los Angeles")
# Print the full inventory dictionary to verify.
print("\n--- Task 4 ---")
# Your code here:
inventory['store_location'] = ("New York", "Los Angeles")
print(inventory)  # Output: Full inventory dictionary with the new key-value pair
