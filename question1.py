# Question 1 Task 1 

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Coffee": 2.99, "fountain drink": 2.49}

# Question 1 Task 2
restaurant_menu["Main Course"]["Steak"] = 17.99

# Question 1 Task 3
del restaurant_menu["Starters"]["Bruschetta"]

# Printing the new menu
print("Updated Restaurant Menu:")
for category, items in restaurant_menu.items():
    print(f"{category}:")
    for item, price in items.items():
        print(f"  {item}: ${price:.2f}")