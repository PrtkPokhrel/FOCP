print("BPP Price Calculator")
print('=======================')


# Function starts here. 
def calculate(number_of_Pizza, isTuesday='n', delivery='n', appUse='n'):
    """the function calculate() calculates the price of pizza.
    There are 3 variable named tuesdayPrice,deliveryPrice,appPrice variables with default value of 0 
    and 2 variable  per_pizzaPrice,deliveryCharge which has its own respective value. """
    
    tuesdayPrice = 0
    deliveryPrice = 0
    appPrice = 0
   # default prices of pizza and delivery
    per_pizzaPrice = 12
    deliveryCharge = 2.50

   #  """Calculates the total price of pizza"""
    pizzaPrice = number_of_Pizza * per_pizzaPrice

   #  """ Checks if day is Tuesday or not and the calculated price is stored on 'tuesdayPrice' """
    while True:
        if isTuesday.lower() == 'y':
            tuesdayPrice = pizzaPrice / 2
            break
        elif isTuesday.lower() == 'n':
            tuesdayPrice = pizzaPrice
            break

   #  """Checks if delivery is required or not and the calculated price is stored on variable 'deliveryPrice' """"
    while True:
        if delivery.lower() == 'y':
            deliveryPrice = tuesdayPrice + deliveryCharge
            # If more than 5 pizza ordered delivery is free
            if number_of_Pizza >= 5:
               deliveryPrice = tuesdayPrice
            else:
             deliveryPrice = tuesdayPrice + deliveryCharge
            break
         
        elif delivery.lower() == 'n':
            deliveryPrice = tuesdayPrice
            break

   #  """Checks if app is used and calculates the total value and store on variable 'appPrice' """"
    while True:
        if appUse.lower() == 'y':
            appPrice = deliveryPrice * 0.75
            break
        elif appUse.lower() == 'n':
            appPrice = deliveryPrice
            break

    
    return float(appPrice)   #Returns the final calculated value

# function calculate() ends here


# Inputs the data from the user and handles the error at the same time

while True:
    try:
        number_of_Pizza = int(input("How many pizzas ordered?: "))
        if number_of_Pizza < 0 or number_of_Pizza==0:
            print("Please correctly enter number of pizza")
        else:
            break
    except ValueError:
        print("Please enter a valid integer for the number of pizzas.")


while True:
    delivery = input("Is delivery required?: ")
    if delivery.lower()=='y'or delivery.lower()=='n':
        break  
    else:
        print("Please enter correct value ")

while True:
    isTuesday = input("Is it Tuesday?: ")
    if isTuesday.lower()=='y'or isTuesday.lower()=='n':
        break  
    else:
        print("Please enter correct value")

while True:
    appUse = input("Did customer use the app?: ")
    if appUse.lower()=='y' or appUse.lower()== 'n':
        break  
    else:
        print("Please enter 'Y' or 'N'.")



# Calls the function calculate
total_price = calculate(number_of_Pizza, isTuesday, delivery, appUse)
formatted_price = "£{:.2f}".format(total_price)
print("The total price is", formatted_price)


