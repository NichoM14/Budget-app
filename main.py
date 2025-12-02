from budget import Category
from budget import create_spend_chart

food = Category("Food")
entertainment = Category("Entertainment")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(150.25, "groceries")
entertainment.deposit(500, "initial deposit")
entertainment.withdraw(200, "movies")
clothing.deposit(200, "initial deposit")
clothing.withdraw(50, "shirts")

print(create_spend_chart([food, entertainment, clothing]))
