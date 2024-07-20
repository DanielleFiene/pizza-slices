# creating a toppings list
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# creating a price list
prices = [2, 6, 1, 3, 2, 7, 2]

# counting the occurence of 2 in the prices list
num_two_dollar_slices = prices.count(2)

# finding the length of toppings ans saving them as a new variable
num_pizzas = len(toppings)

print('We sell', num_pizzas, 'different kinds of pizza!')

# creating a 2-dimensional list
pizza_and_prices = [
                  [2, 'pepperoni'],
                  [6, 'pineapple'],
                  [1, 'cheese'],
                  [3, 'sausage'],
                  [2, 'olives'],
                  [7, 'anchovies'],
                  [2, 'mushrooms']
]

# sorting the pizzas in order by price (ascending), When sorting a two-dimensional list using .sort(), the list by default will be sorted by the first element in each sublist. In this case, this will mean it is sorted by the price.
pizza_and_prices.sort()
#checking if it sorted right by printing pizza_and_prices
#print(pizza_and_prices)

# storing the first element of pizza_and_prices in a variable called cheapest_pizza
cheapest_pizza = pizza_and_prices[0]
# checking if the cheapest pizza (cheese pizza) is stored as expected
#print(cheapest_pizza)

# storing the last element of pizza_and_prices to get the most expensive pizza and store it in a variable called priciest_pizza
priciest_pizza = pizza_and_prices[-1]
# checking if the priciest pizza (anchvoies pizza) is stored as expected
#print(priciest_pizza)

# removing the anchovies pizza from the lizza_and_prices list
pizza_and_prices.pop()
# checking the new pizza_and_prices list 
# print(pizza_and_prices)

# adding a new pizza called peppers for $2.5 to the pizzas_and_prices list relative to the rest of items stored in the list so it is still ordered (after pepperoni (3rd index) but before sausage pizza (4th index) so i need to use index-position 4)
# first define a new pizza variable
new_peppers_pizza = (2.5, 'peppers')
#checking the new variable
# print(new_peppers_pizza)
# inserting the new variable at the 3rd index position of pizza_and_prices
pizza_and_prices.insert(4, new_peppers_pizza)
# checking the new pizza_and_prices list
#print(pizza_and_prices)

# slicing the pizza_and_prices list, storing the 3 lowest pizzas in a new variable called three_cheapest starting at index position 0, ending at index-posiiton 3
three_cheapest = pizza_and_prices[:3]
# checking the new variable three_cheapest
print(three_cheapest)



